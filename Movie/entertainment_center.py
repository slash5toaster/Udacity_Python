import media

toystory = media.Movie("Toy Story",
                       "A story of a boy's toys that come to life",
                       "https://en.wikipedia.org/wiki/File:Toy_Story.jpg#/media/File:Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=4KPTXpQehio")
# print(toystory.storyline)

avatar = media.Movie("Avatar: The Last Airbender",
                     "A magical teenager",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BZTdmY2YxYTctMTY0Mi00YmRhLWEyNzEtZDJiOTQyYTFkODVkXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg",
                     "http://www.imdb.com/title/tt0417299/videoplayer/vi2716336409")
# print(avatar.storyline)
# avatar.show_trailer()

# print(media.Movie.VALID_RATINGS)
print(media.Movie.__name__)
print(media.Movie.__module__)
print(media.Movie.__doc__)
