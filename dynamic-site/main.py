'''
Jana Nash-Siegle
10/17/2015
DPW - 01
Dynamic Site - Project 3

*all Warcraft imagery is used via public license from World of Warcraft 
'''
import webapp2

from data import Data
from pages import CharPage


class MainHandler(webapp2.RequestHandler):
    def get(self):
    	#let's import some data		
		d = Data()
		#let's create our page
		p = CharPage()

		#GET Method - depending on class_list
		if self.request.GET:
			char = self.request.GET['char']
			#see if the correct class prints in console when image link is selected
			print char	
			#yes it is	


			

			#this should now print out character specifics to browser
			self.response.write(p.print_out_char())

		else:
			#print out landing page with nav image gallery
			self.response.write(p.print_out())  



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
