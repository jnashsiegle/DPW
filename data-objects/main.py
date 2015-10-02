#data objects
#dict(), json (javascript object notation), class is a holder of data, objects in javascript itself, 

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        luke = Character()
        luke.name = "Luke Skywalker"
        luke.profession = "Jedi Knight"
        luke.age = 26
        luke.home_planet = "Tattooine"

        leia = Character()
        leia.name = "Princess Leia"
        leia.profession = "Princess"
        leia.age = luke.age #they were twins are the same age
        leia.home_planet = "Alderan"

        yoda = Character()
        yoda.name = "Master Yoda"
        yoda.profession = "Jedi Knight"
        yoda.age = "762"
        yoda.home_planet = "Dagobah"

        chars = [luke, leia, yoda]
        print chars[0].profession #would print Luke's profession
        print chars[1].profession #should print leia's profession

class Character(object):
	def __init__(self): #constructor function
		self.name = "" #public attributes of name profession age and home_planet
		self.profession = ""
		self.age = 0
		self.home_planet = ""





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
