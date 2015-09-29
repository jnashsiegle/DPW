'''
Jana Nash-Siegle
9/28/2015
DPW - 01
Setting Up the Launcher
'''
import webapp2 #use the webapp2 library - needed for basic functionality

class MainHandler(webapp2.RequestHandler): #Declares a class
    def get(self): #function that starts everything, catalyst, invokes
        self.response.write('Hello world!')
        #code goes here

        def additional_functions(self):
        	pass
        	#code goes here

#leave alone, DO NOT TOUCH BELOW THIS LINE
app = webapp2.WSGIApplication([ 
    ('/', MainHandler)
], debug=True)
