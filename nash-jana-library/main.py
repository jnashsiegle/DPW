"""created by Jana Nash-Siegle
DPW 101501
Wainman
10/14/2015
"""
import webapp2
from library import UserInfo, BudgetBreak
from pages import Form, ResultsPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #create our form page
    	f = Form()
    	#create the results view
    	rp = ResultsPage()

    	#GET Method to grab variables from user input
        if self.request.GET:
            #storing our info from the user inputs
            #call our UserInfo Object
            user = UserInfo()
            user.name = self.request.GET['name']
            user.email = self.request.GET['email']
            user.mon_bud = self.request.GET['monBudg']           
            user.have_budget = self.request.GET['budget']
            #Print out if form has been submitted otherwise print out following else:
            self.response.write(rp.print_out())
        else:           
        	self.response.write(f.print_out())# this will print out in browser
        #DO NOT DELETE ABOVE LINE

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
