# The course "Introduction to Python Programming helped a lot to come up \
# with this project.
# Few of the things are changed with the project that was already available.

import webbrowser

# base class that can be a parent class for children classes like, Movie, \
# Book etc.


class Library():
    ''' The class that can hold generic information about books, movies etc.'''
    def __init__(self, _title, _storyline, _genre, _rating, _poster_image_url,
                 _more_info):
        self.title = _title
        self.storyline = _storyline
        self.genre = _genre
        self.rating = _rating
        self.poster_image_url = _poster_image_url
        self.more_info = _more_info


# derived from class "Library". The only special thing that is required by \
# "Movie" class is to the trailor
# associated with the movie. Essentially, that is a link to youtube.com.
class Movie(Library):
    ''' The class that can hold information about movies '''
    def __init__(self, _title, _storyline, _genre, _rating, _poster_image_url,
                 _trailer_url, _more_info):
        Library.__init__(self, _title, _storyline, _genre, _rating,
                         _poster_image_url, _more_info)
        self.trailer_youtube_url = _trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
