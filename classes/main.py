'''
Jana Nash-Siegle
10/1/2015
DPW - 01
Setting Up the Launcher
'''
import webapp2 #use the webapp2 library - needed for basic functionality

class MainHandler(webapp2.RequestHandler): #Declares a class.  this is our APPLICATION CLASS
    def get(self): #function that starts everything, catalyst, invokes
        about_button = Button() #simple variable
        contact_button = Button() #these (about and contact) are both instances of the Button() class

       	about_button.label = "About Us"#if we were outside this function we could call by using button.click
       									#button.label is adding an attribute to button
       	about_button.show_label()
       	contact_button.label = "Contact Us"
       	contact_button.show_label()
class Button(object):
	def __init__(self):  #method -contstructor method or the initializor
		self.label = ""  #public attribute
		self.__size = 60 #private attribute - two underscores
		self._color = "0x00000" #protected attribute - one underscore
		#self.on_roll_over("Hello!")#this hello fills in below as message

	def click(self):  #self is the = to .this in javascript. this is the click method 
		print "I've been clicked"

	def on_roll_over(self, message):
		print "You've rolled over my button" + message #this is the rollover method

	def show_label(self):
		print "My label is " + self.label #self.label shows ALL instances of label
        



#leave alone, DO NOT TOUCH BELOW THIS LINE
app = webapp2.WSGIApplication([ 
    ('/', MainHandler)
], debug=True)
