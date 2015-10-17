'''
Jana Nash-Siegle
10/17/2015
DPW - 01
Dynamic Site - Project 3

*all Warcraft imagery is used via public license from World of Warcraft 
'''
import webapp2
from pages import Page
p = Page()
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(p.print_out())






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
