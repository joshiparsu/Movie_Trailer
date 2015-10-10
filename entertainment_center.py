# The course "Introduction to Python Programming helped a lot to come up with \
# this project.
# Few of the things are changed with the project that was already available.
import moviedb
import media

# Create instances of favourite movies that will be displayed in web-page
the_godfather = media.Movie("The Godfather",
                            "The aging patriarch of an organized crime \
                            dynasty transfers control of his clandestine \
                            empire to his reluctant son.",
                            "Crime-Drama",
                            "9.2",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/1/1c/Godfather_ver1.jpg/220px-Godfather_ver1.jpg",  # noqa
                            "https://www.youtube.com/watch?v=sY1S34973zA",
                            "http://www.imdb.com/title/tt0068646")

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker, looking for a way to \
                         change his life, crosses paths with a devil-may- \
                         care soap maker forming an underground fight club \
                         that evolves into something much, much more...",
                         "Drama",
                         "8.9",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Fight_Club_poster.jpg/220px-Fight_Club_poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                         "http://www.imdb.com/title/tt0137523/")

gladiator = media.Movie("Gladiator",
                        "When a Roman general is betrayed and his family \
                        murdered by an emperor's corrupt son, he comes to \
                        Rome as a gladiator to seek revenge.",
                        "Action-Drama",
                        "8.5",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Gladiator_ver1.jpg/220px-Gladiator_ver1.jpg",  # noqa
                        "https://www.youtube.com/watch?v=icWR_kCmfUU",
                        "http://www.imdb.com/title/tt0172495")

scarface = media.Movie("Scarface",
                       "In 1980 Miami, a determined Cuban immigrant takes \
                       over a drug cartel while succumbing to greed.",
                       "Crime-Drama",
                       "8.3",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/Scarface.jpg/220px-Scarface.jpg",  # noqa
                       "https://www.youtube.com/watch?v=Q5kUTf-HBsE",
                       "http://www.imdb.com/title/tt0086250")

the_seventh_seal = media.Movie("The Seventh Seal",
                        "A man seeks answers about life, death, and the \
                        existence of God as he plays chess against the \
                        Grim Reaper during the Black Plague.",
                        "Drama-Fantasy",
                        "8.3",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/6/69/Seventhsealposter.jpg/220px-Seventhsealposter.jpg",  # noqa
                        "https://www.youtube.com/watch?v=NtkFei4wRjE",
                        "http://www.imdb.com/title/tt0050976")

stalker = media.Movie("Stalker",
                      "A guide leads two men through an area known as the \
                      Zone to find a room that grants wishes.",
                      "Drama-SciFi",
                      "8.2",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Stalker_poster.jpg/220px-Stalker_poster.jpg",  # noqa
                      "https://www.youtube.com/watch?v=GM_GOpfEQUw",
                      "http://www.imdb.com/title/tt0079944")

infernal_affairs = media.Movie("Infernal Affairs",
                       "A story between a mole in the police department and \
                       an undercover cop. Their objectives are the same: to \
                       find out who is the mole, and who is the cop.",
                       "Crime-Mystery-Thriller",
                       "8.1",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/9/98/IAmoviepost.jpg/220px-IAmoviepost.jpg",  # noqa
                       "https://www.youtube.com/watch?v=S4R3nHkqyfM",
                       "http://www.imdb.com/title/tt0338564")

memories_of_murder = media.Movie("Memories Of Murder",
                        "Two rural cops and a special detective from the capital \
                        investigate a series of brutal rape murder. Their \
                        crude measures become more desperate with each new \
                        corpse found.",
                        "Crime-Drama-Mystery",
                        "8.1",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/17/Memories_of_Murder_poster.jpg/220px-Memories_of_Murder_poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=dTnyhLywdJc",
                        "http://www.imdb.com/title/tt0353969")

the_battle_of_algiers = media.Movie("The Battle Of Algiers",
                                    "In the 1950s, fear and violence escalate as \
                                    the people of Algiers fight for \
                                    independence from the French government.",
                                    "Drama-History-War",
                                    "8.2",
                                    "https://upload.wikimedia.org/wikipedia/en/thumb/a/aa/The_Battle_of_Algiers_poster.jpg/220px-The_Battle_of_Algiers_poster.jpg",  # noqa
                                    "https://www.youtube.com/watch?v=6l1DgEYgmPY",  # noqa
                                    "http://www.imdb.com/title/tt0058946")

movies = [the_godfather, gladiator, scarface, the_seventh_seal, stalker,
          infernal_affairs, memories_of_murder, the_battle_of_algiers]


moviedb.open_movies_page(movies)
