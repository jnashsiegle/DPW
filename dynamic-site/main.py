'''
Jana Nash-Siegle
10/17/2015
DPW - 01
Dynamic Site - Project 3

*all Warcraft imagery is used via public license from World of Warcraft 
'''
import webapp2

from data import Data, CharClass
from pages import Page, CharPage


class MainHandler(webapp2.RequestHandler):
    def get(self):
    	#let's create our page
		p = CharPage()
    	#let's import some data		
		d = Data()
		#need to determine printout
		x = Page()
		

		#GET Method - depending on class_arr
		if self.request.GET:
			char = self.request.GET['char']
			#see if the correct class prints in console when image link is selected
			print char	
			#yes it is	
			if char == "warrior":
				#let's test with a print to console
				#if the url has the above keyword in it from the image link, match to the array and pull that instances attributes and load them into the html
				#print d.class_arr[0].title, d.class_arr[0].armor, d.class_arr[0].weapons
				p.title = d.class_arr[0].title
				p.type = d.class_arr[0].type
				p.standard = d.class_arr[0].standard
				p.armor = d.class_arr[0].armor
				p.weapons = d.class_arr[0].weapons
				p.image = d.class_arr[0].image
				p.desc = d.class_arr[0].desc
			elif char == "paladin":
				p.title = d.class_arr[1].title
				p.type = d.class_arr[1].type
				p.standard = d.class_arr[1].standard
				p.armor = d.class_arr[1].armor
				p.weapons = d.class_arr[1].weapons
				p.image = d.class_arr[1].image
				p.desc = d.class_arr[1].desc
			elif char == "hunter":				
				p.title = d.class_arr[2].title
				p.type = d.class_arr[2].type
				p.standard = d.class_arr[2].standard
				p.armor = d.class_arr[2].armor
				p.weapons = d.class_arr[2].weapons
				p.image = d.class_arr[2].image
				p.desc = d.class_arr[2].desc
			elif char == "rogue":				
				p.title = d.class_arr[3].title
				p.type = d.class_arr[3].type
				p.standard = d.class_arr[3].standard
				p.armor = d.class_arr[3].armor
				p.weapons = d.class_arr[3].weapons
				p.image = d.class_arr[3].image
				p.desc = d.class_arr[3].desc
			elif char == "priest":				
				p.title = d.class_arr[4].title
				p.type = d.class_arr[4].type
				p.standard = d.class_arr[4].standard
				p.armor = d.class_arr[4].armor
				p.weapons = d.class_arr[4].weapons
				p.image = d.class_arr[4].image
				p.desc = d.class_arr[4].desc
			elif char == "death_knight":				
				p.title = d.class_arr[5].title
				p.type = d.class_arr[5].type
				p.standard = d.class_arr[5].standard
				p.armor = d.class_arr[5].armor
				p.weapons = d.class_arr[5].weapons
				p.image = d.class_arr[5].image
				p.desc = d.class_arr[5].desc
			elif char == "shaman":				
				p.title = d.class_arr[6].title
				p.type = d.class_arr[6].type
				p.standard = d.class_arr[6].standard
				p.armor = d.class_arr[6].armor
				p.weapons = d.class_arr[6].weapons
				p.image = d.class_arr[6].image
				p.desc = d.class_arr[6].desc
			elif char == "mage":				
				p.title = d.class_arr[7].title
				p.type = d.class_arr[7].type
				p.standard = d.class_arr[7].standard
				p.armor = d.class_arr[7].armor
				p.weapons = d.class_arr[7].weapons
				p.image = d.class_arr[7].image
				p.desc = d.class_arr[7].desc
			elif char == "warlock":				
				p.title = d.class_arr[8].title
				p.type = d.class_arr[8].type
				p.standard = d.class_arr[8].standard
				p.armor = d.class_arr[8].armor
				p.weapons = d.class_arr[8].weapons
				p.image = d.class_arr[8].image
				p.desc = d.class_arr[8].desc
			elif char == "monk":				
				p.title = d.class_arr[9].title
				p.type = d.class_arr[9].type
				p.standard = d.class_arr[9].standard
				p.armor = d.class_arr[9].armor
				p.weapons = d.class_arr[9].weapons
				p.image = d.class_arr[9].image
				p.desc = d.class_arr[9].desc
			elif char == "druid":				
				p.title = d.class_arr[10].title
				p.type = d.class_arr[10].type
				p.standard = d.class_arr[10].standard
				p.armor = d.class_arr[10].armor
				p.weapons = d.class_arr[10].weapons
				p.image = d.class_arr[10].image
				p.desc = d.class_arr[10].desc
				

			#this should now print out character specifics to browser
			self.response.write(p.print_out())

		else:
			#print out landing page with nav image gallery
			self.response.write(x.print_out())  



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
