class Page(object):
	def __init__(self):
		self.title = "Welcome!"
		self.css = "css/style.css"
		self.head = """
<!DOCTYPE HTML>
<html>
	<head>
		<title>{self.title}</title>
		<link href = "{self.css}" rel = "Stylesheet" type = text/css" />
	</head>
	<body>"""

		self.page_body = '''
		<header><h1>Acme Web Workshop Event Planning Survey</h1>
		<p><a href = "bing.com">Exit Survey</a></p>
		</header>
			<article id = "wrapper">
				<section>
					<p>Thank you for signing up for our next workshop.  Would you take a moment to fill out this survey so we may learn how to better serve you?</p>
				</section>
				<section>
					<form method = "GET">

						<label>Name: </label><input type = "text" name = "attendee" />
						<label>Email: </label><input type = "text" name = "email" />

						<p>Which workshops will you be attending?</p>
						<label>HTML</label><input type = "checkbox" name = "HTML" />
						<label>JavaScript</label><input type = "checkbox" name = "JavaScript" />
						<label>Server-Side Programming</label><input type = "checkbox" name = "ssp" />
						<label>Client-Side Programming</label><input type = "checkbox" name = "csp" />

						<label>How did you hear about this event?</label><input type = "text" name = "hear" />

						<p>How easy was the registration process for this event?></p>
						<label>Very Easy</label><input type = "radio" name = "ve"  />
						<label>Easy</label><input type = "radio" name = "easy" />
						<label>Slightly Confusing</label><input type = "radio" name = "sc" />
						<label>Hard</label><input type = "radio" name = "hard" />
						<label>Very Hard</label><input type = "radio" name = "vh" />
						<label>Comments about the registration process: </label><input type = "text" name = "rp-comments" />

						<p>Do you have any dietary restrictions?</p>
						<label>Yes</label><input type = "radio" name = "diet-yes" />
						<label>No</label><input type = "radio" name = "diet-no" />
						<p>if yes, please enter details: </p>
						<label>Details: </label><input type = "text" name = "diet-details" />
						<label>Who will be paying for you to attend this event?</label><input type = "text" name = "payment">
						<p>What is the easiest way to contact you in regards to this event?</p>
						<label>E-Mail</label><input type = "radio" name = "comm-email" />
						<label>Phone</label><input type = "radio" name = "comm-phone" />
						<label>Snail Mail</label><input type = "radio" name = "comm-mail" />
						<label>Other: (Please Specify)</label>
						<input type = "text" name = "comm-other" />

						<input type = "submit" value = "Submit" />'''
		self.page_close = '''
	</body>
</html>'''
		

	 	if self.request.GET: #same as adding == True: to the end of it.  We are giving it a condition of if the variable exists then print out the following information
   		#print self.request.GET['user'] #gets the information that will be entered into the page, has to match the name of the element
   		#print "hello there" testing of print
   		#the two lines below store the information into variables
	    		#attendee = self.request.GET['attendee'] #if we want more than the above console printing let's store it in a variable called user
	    		email = self.request.GET['email']
	    		'''html = self.request.GET['HTML']
	    		javascrfipt = self.request.GET['JavaScript']
	    		ssp = self.request.GET['ssp']
	    		csp = self.request.GET['csp']
	    		hear = self.request.GET['hear']
	    		ve = self.request.GET['ve']
	    		easy = self.request.GET['easy']
	    		sc = self.request.GET['sc']
	    		hard = self.request.GET['hard']
	    		vh = self.request.GET['vh']
	    		rpComments = self.request.GET['rpComments']
	    		dietYes = self.request.GET['dietYes']
	    		dietNo = self.request.GET['dietNo']
	    		dietDetails = self.request.GET['dietDetails']
	    		payment = self.request.GET['payment']
	    		commEmail = self.request.GET['commEmail']
	    		commPhone = self.request.GET['commPhone']
	    		commMail = self.request.GET['commMail']
	    		commOther = self.request.GET['commOther']'''
	    		
	    		self.response.write(page_head + user + ' ' + email + page_body + page_close)#print  if you don't want to print form again just results, take out the page_body and it will print only the user inputs
	    	else:
	    		self.response.write(page_head + page_body + page_close)#print
