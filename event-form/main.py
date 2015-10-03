'''
Jana Nash-Siegle
10/2/2015
DPW - 01
Simple Event Planning Form

'''
import webapp2
from page import Page #from pages.py import the page class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.body = "Miss Piggy likes Kermit de Frog" #this will replace the body text below in self.body
        #print p.print_out()#this will print out in the google engine console
        self.response.write(p.print_out())# this will print out in browser









app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
