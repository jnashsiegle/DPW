
import webapp2
from library import MovieData, FavoriteMovies
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	p = Page()
    	lib = FavoriteMovies() #instance for the FavoriteMovies
        #movie title  (this is part of our assignment, making it user input)
        #year movie was made(this is part of our assignment)(this is our assignment)
        #director of the film (this is part of our assignment)
        #for this demo we will be hard-coding the above three line values do not normally do this
        #page for class (if/else for 2 different page views for assignment)

        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.year = 1989  #actually calling a function 
        md1.director = "Rob Reiner"
        lib.addMovie(md1)

        md2 = MovieData()
        md2.title = "Dune"
        md2.year = 1986  #actually calling a function 
        md2.director = "David Lynch"

        self.response.write(p.print_out()) #sends the info out to browser as a big string

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
