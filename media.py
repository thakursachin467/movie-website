import webbrowser
class Movie():
    def _init_(self,movie_title,movie_storyline,movie_posterimage,movie_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=movie_posterimage
        self.trailor_youtube_url=movie_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    
