import webbrowser

class Movie():
    """ Class for storing Movie information """
    VALID_RATINGS = ["PG", "PG-13", "G", "NC-17", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_video):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_video_url = trailer_video

    def show_trailer(self):
        webbrowser.open(self.trailer_video_url)
