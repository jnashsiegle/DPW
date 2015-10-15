
import webapp2
from library import TranInfo
from pages import Form, ResultsPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	#create our form page
    	f = Form()
    	#create the results view
    	rp = ResultsPage()
    	#lib =  #instance for the FavoriteMovies
        #movie title  (this is part of our assignment, making it user input)
        #year movie was made(this is part of our assignment)(this is our assignment)
        #director of the film (this is part of our assignment)
        #for this demo we will be hard-coding the above three line values do not normally do this
        #page for class (if/else for 2 different page views for assignment)

        #GET Method to grab variables from user input
        if self.request.GET:
            #storing our info from the user inputs
            tran = TranInfo()
            tran.payee = self.request.GET['payee']
            tran.amount = self.request.GET['amount']
            tran.category = self.request.get_all('category')            
            tran.budget = self.request.GET['budget']
            #Print out if form has been submitted otherwise print out following else:
            self.response.write(rp.print_out())
        else:           
        	self.response.write(f.print_out())# this will print out in browser
        #DO NOT DELETE ABOVE LINE
       
        
        




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
