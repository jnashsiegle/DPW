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
			'''char = Data()
			char.title = self.title	
			char.type = self.type	
			char.standard = self.standard	
			char.armor = self.armor	
			char.weapons = self.weapons	
			char.image = self.image	
			print char'''
			char = self.request.GET['char']
			print char
			#send  to setter on image
			if char == "warrior":
				print d.class_arr[0]
				p.html = d.class_arr[0]
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
