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
            user.mon_income = self.request.GET['monIncome']         
            user.have_budget = self.request.GET['budget']
            #Print out if form has been submitted otherwise print out following else:
            #self.response.write(rp.print_out())
            self.response.write(rp.print_out() + 'Your name is: ' +  user.name + '<br />' +  'Your email is: ' + user.email + '<br />' + 'The total of your recurring monthly expenses is: ' + user. mon_bud + '<br />' + ' Your total monthly income is: ' + user.mon_income + '<br />' + 'You do ' + user.have_budget + ' use a budget to track your expenses and income.'  )
        else:           
        	self.response.write(f.print_out())# this will print out in browser
        #DO NOT DELETE ABOVE LINE

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
