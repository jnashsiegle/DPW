'''
Jana Nash-Siegle
DPW
Event-Form

This page will provide the structure for the form.  It contains the html and is divided up into 4 sections, self.head, self. header
self.body, self.close to make it easier to string together later over in main.py.
'''
class Form(object):
	def __init__(self):
		self.head = """   				
<!DOCTYPE HTML>							
<html>
	<head>
		<title>Event Planning Survey</title>
		<link rel="stylesheet" type="text/css" href="css/style.css">
	</head>
	<body>"""

		self.header = '''
		<header><h1>Acme Web Workshop Event Planning Survey</h1>
		<p><a href = "http://www.bing.com">Exit Survey</a></p>
		</header>'''
		self.body = '''<article id = "wrapper">
									
						<h3>Thank you for signing up for our next workshop.</h3> <p> Would you take a moment to fill out this survey so we may learn how to better serve you?</p>
					
					
					<form method = "GET">
						<div id = "personalInfo">
							<label>Name: </label><input type = "text" placeholder = "Enter Your Name" name = "attendee" />
							<label>Email: </label><input type = "email" placeholder = "yourname@domain.com" name = "email" />
						</div>
						<div id = "workshops">
							<label>Which workshop will you be attending?</label>
								<select name = "workshops">
									<option value = "">Click here to see options</option>
									<option value = "css">CSS</option>
									<option value = "html">HTML</option>
									<option value = "js">JavaScript</option>
									<option value = "python">Python</option>
								</select>
							
						</div>

						<div id = "registration">
							<label>How did you hear about this event?</label><input type = "text" placeholder = "online/word of mouth" name = "hear" required />
							<p>How easy was the registration process for this event?</p>
							<label>Very Easy</label><input type = "radio" name = "rp" value = "very easy" checked/>
							<label>Easy</label><input type = "radio" name = "rp" value = "easy"/>
							<label>Slightly Confusing</label><input type = "radio" name = "rp" value = "slightly confusing"/>
							<label>Hard</label><input type = "radio" name = "rp" value = "hard"/>
							<label>Very Hard</label><input type = "radio" name = "rp" value = "very hard" />
							<p></p>
							<label>Comments about the registration process: </label><input type = "text" placeholder = "Make comments here" name = "rpComments" value = "none"/>
						</div>
						<div id = "diet">
							<p>Do you have any dietary restrictions?
							<label>Yes</label><input type = "radio" name = "diet" value = "do"/>
							<label>No</label><input type = "radio" name = "diet" value = "don't" checked/>
							<p>if yes, please enter details: </p>
							<label>Details: </label><input type = "text" placeholder = "Restrictions" name = "dietDetails" value = "none"/></p>
						</div>
						<div id = "misc">
							<label>Who will be paying for you to attend this event?</label><input type = "text" placeholder = "company" name = "payment" value = "none">
							<p>What is the preferred method of contacting you in regards to this event?</p>
							<label>E-Mail</label><input type = "radio" name = "communication" value = "email" checked/>
							<label>Phone</label><input type = "radio" name = "communication"  value = "phone"/>
							<label>Snail Mail</label><input type = "radio" name = "communication" value = "snail mail" />
							<p>What is your interest in these workshops?</p>
							<label>Career</label><input type = "checkbox" name = "purpose" value = "career" checked />
							<label>Passion</label><input type = "checkbox" name = "purpose" value = "passion" />
							<label>Hobby</label><input type = "checkbox" name = "purpose" value = "hobby" />
						</div>						
						<p><input type = "submit" value = "Submit" /></p>
		'''
		self.close = '''
					</form>
				</article>
	</body>
</html>'''
		
	    
	
	def print_out(self):			#defines a method to print out the form that we will call over in main.py
		all =  self.head + self.header +  self.body + self.close  #sets the variable all to be all the sections.
		all = all.format(**locals())   #uses a dictionary-based string formatting
		return all