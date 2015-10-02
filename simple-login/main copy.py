'''
Jana Nash-Siegle
9/28/2015
DPW - 01
Setting Up the Launcher
'''
import webapp2 #use the webapp2 library - needed for basic functionality

class MainHandler(webapp2.RequestHandler): #Declares a class
    def get(self): #function that starts everything, catalyst, invokes
    	
		page_head = '''<!DOCTYPE HTML>
    <html>
    	<head>
    		<title>Simple Form!</title>
    	</head>
    		<body>'''

		page_body = '''<form method = "GET">
		    			<label>Name: </label><input type = "text" name = "user" />
		    			<label>Email: </label><input type = "text" name = "email" />
		    			<input type = "submit" value = "Submit" />'''
		page_close = '''
    		</form>
    	</body>
    </html>'''


   		if self.request.GET: #same as adding == True: to the end of it.  We are giving it a condition of if the variable exists then print out the following information
   		#print self.request.GET['user'] #gets the information that will be entered into the page, has to match the name of the element
   		#print "hello there" testing of print
   		#the two lines below store the information into variables
	    		user = self.request.GET['user'] #if we want more than the above console printing let's store it in a variable called user
	    		email = self.request.GET['email']
	    		self.response.write(page_head + user + ' ' + email + page_body + page_close)#print  if you don't want to print form again just results, take out the page_body and it will print only the user inputs
	    	else:
	    		self.response.write(page_head + page_body + page_close)#print


    #self.response.write(page) #prints our information out onto the page

        

        






#leave alone, DO NOT TOUCH BELOW THIS LINE
app = webapp2.WSGIApplication([ 
    ('/', MainHandler)
], debug=True)
