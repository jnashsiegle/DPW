"""created by Jana Nash-Siegle
DPW 101501
Wainman
10/14/2015
"""
import webapp2
#import our library.py, class BudgetBreak
from library import BudgetBreak
#import our page views laid out on pages.py, 2 view classes Form and ResultsPage
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
            #call our BudgetBreak Object
            user = BudgetBreak()
            user.name = self.request.GET['name']
            user.email = self.request.GET['email']
            user.mon_exp = int(self.request.GET['monExp'])  
            user.mon_income = int(self.request.GET['monIncome'])        
            user.have_budget = self.request.GET['budget']

            #RESULTS PAGE - INFORMATION 
            #Print out if form has been submitted otherwise print out following else:
            rp.email = user.email  #setting for print out
            rp.discretion = user.discretion()
            self.response.write(rp.print_out() + '<h3>Greetings, ' +  user.name + '!</h3>')
        else:           
        	self.response.write(f.print_out())# this will print out in browser
        #DO NOT DELETE ABOVE LINE

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
