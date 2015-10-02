'''
Jana Nash-Siegle
10/2/2015
DPW - 01
Simple Event Planning Form

'''
import webapp2 #use the webapp2 library - needed for basic functionality
from page import Page #from page.py import the page class

class MainHandler(webapp2.RequestHandler): #declares our class
    def get(self):  #invoking, starts everything off
    	p = Page() #setting a Page variable
    	#p.body = "Please fill out this survey." #This replaces the body text in self.body
        self.response.write(p.print_out())#so we will print out in browser



#Do not touch anything below this line:
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
