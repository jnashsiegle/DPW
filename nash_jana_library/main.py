
import webapp2
#from library import 
from pages import ResultsPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	rp = ResultsPage()
    	#lib =  #instance for the FavoriteMovies
        #movie title  (this is part of our assignment, making it user input)
        #year movie was made(this is part of our assignment)(this is our assignment)
        #director of the film (this is part of our assignment)
        #for this demo we will be hard-coding the above three line values do not normally do this
        #page for class (if/else for 2 different page views for assignment)

        '''
        ***** example data
        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.year = 1989  #actually calling a function 
        md1.director = "Rob Reiner"
        lib.add_movie(md1) #causes title to print out when print m.title is added to method def addMovie
        '''
        
        '''
        ***** call and run function examples
        lib.calc_time_span()    #adds this to run but we need to add it to the printing out list below
        p.body = lib.compile_list() + lib.calc_time_span() #adds the compile list to the body tag of the html in the page.py
        self.response.write(p.print_out()) #sends the info out to browser as a big string
        '''




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
