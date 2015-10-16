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
            user.__mon_exp = self.request.GET['monExp']  
            user.__mon_income = self.request.GET['monIncome']         
            user.have_budget = self.request.GET['budget']

            #RESULTS PAGE - INFORMATION 
            #Print out if form has been submitted otherwise print out following else:
            self.response.write(rp.print_out() + '<h3>Greetings, ' +  user.name + '!</h3>' +  'From the information provided we have calculated the following information.<br/>' + 'Your email is: ' + user.email + '</p>' + 'The total of your recurring monthly expenses is: ' + str(user.__mon_exp) + '<br />' + ' Your total monthly income is: ' + str(user.__mon_income) + '<br />' + 'Your total monthly discretionary funds comes to ' + str(user.discretion()) + '<br />' +  'You ' + user.have_budget + ' use a budget to track your expenses and income.' + '<br />' +'Your estimated mortgage allowance should be ' + str(user.calc_mortgage()) + '<br />' + 'Your annual income is: ' + str(user.annual()))
        else:           
        	self.response.write(f.print_out())# this will print out in browser
        #DO NOT DELETE ABOVE LINE

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
