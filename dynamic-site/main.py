'''
Jana Nash-Siegle
10/17/2015
DPW - 01
Dynamic Site - Project 3

*all Warcraft imagery is used via public license from World of Warcraft 
'''
import webapp2

from data import Data, CharClass
from pages import CharPage


class MainHandler(webapp2.RequestHandler):
    def get(self):
    	#let's import some data		
		d = Data()
		#let's create our page
		p = CharPage()

		#GET Method - depending on class_arr
		if self.request.GET:
			char = self.request.GET['char']
			#see if the correct class prints in console when image link is selected
			print char	
			#yes it is	
			if char == "warrior":
				print d.class_arr[0]
				p.html = d.class_arr[0] #links p.html to the class_arr in Data(), opening up the variables to the html in pages I am hoping?
			elif char == "paladin":
				print d.class_arr[1]
				p.html = d.class_arr[1]

			#this should now print out character specifics to browser
			self.response.write(p.print_out_char())

		else:
			#print out landing page with nav image gallery
			self.response.write(p.print_out())  



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
