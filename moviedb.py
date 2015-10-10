# The course "Introduction to Python Programming helped a lot to come up \
# with this project.
# Few of the things are changed with the project that was already available.

import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Prashant's Favourite Movie DB!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            position:absolute;
            top:28%;
            left:42%;
            opacity:0.9;
            display:initial !important;
        }
        .movie-tile:hover {
            cursor: pointer;
            border:outset;
            border-color: #AAA;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body style="position: static; width: auto; margin: auto; min-width: 1008px; background: -webkit-linear-gradient(top, rgba(226,226,226,1) 0%, rgba(209,209,209,1) 20%, rgba(219,219,219,1) 55%, rgba(254,254,254,1) 100%)" >
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation" style="margin:auto; width:80%">
        <div class="container">
          <div class="navbar-header" style="width:80%">
            <a class="navbar-brand" href="#">PFMDb - Prashant's Favourite Movies</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''
# Movie table header
movie_table_header = '''
    <div class="row">
        <div class="col-md-6 text-center">
            <h1> Title </h1>
        </div>
        <div class="col-md-3 text-center">
            <h1> Genre </h1>
        </div>
        <div class="col-md-3 text-center">
            <h1> Rank </h1>
        </div>
    </div>
'''

# A single movie entry html template
movie_tile_content = '''
    <div class="row" style="margin-top:5px; background-color:{bgcolor}">
        <div class="col-md-3 text-center">
            <span>
                <img src="{poster_image_url}" width="100px" height="125px" title="{movie_storyline}" >
                <img src="http://blueforeststudios.com/azultree/wp-content/uploads/2015/01/youtube-play-button.png" width="44px" height="43px" title="Play trailer" class="movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" >
            </span>
        </div>
        <div class="col-md-3 text-center">
            <h2> <a href="{more_info}"> {movie_title} </a> </h2>
        </div>
        <div class="col-md-3 text-center">
            <h3> {movie_genre} </h3>
        </div>
        <div class="col-md-3 text-center">
            <h3> {movie_rating} </h3>
        </div>
    </div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''

    content += movie_table_header
    count = 1
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        if(count % 2 == 0):
            color = "#EAEAEA"
        else:
            color = "#BABABA"

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            more_info=movie.more_info,
            movie_genre=movie.genre,
            movie_rating=movie.rating,
            movie_storyline=movie.storyline,
            bgcolor=color
        )
        count += 1

    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('pfmdb.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    storyline = webbrowser.open('file://' + url, new=2)
