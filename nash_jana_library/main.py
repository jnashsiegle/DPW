
import webapp2
#from library import 
from pages import Form, ResultsPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	rp = ResultsPage()
    	f = Form()
    	#lib =  #instance for the FavoriteMovies
        #movie title  (this is part of our assignment, making it user input)
        #year movie was made(this is part of our assignment)(this is our assignment)
        #director of the film (this is part of our assignment)
        #for this demo we will be hard-coding the above three line values do not normally do this
        #page for class (if/else for 2 different page views for assignment)

        '''
        
        ***** call and run function examples
        lib.calc_time_span()    #adds this to run but we need to add it to the printing out list below
        p.body = lib.compile_list() + lib.calc_time_span() #adds the compile list to the body tag of the html in the page.py
        '''
        self.response.write(f.print_out()) #sends the info out to browser as a big string
        




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
