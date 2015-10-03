class Page(object):
	def __init__(self):
		self.title = "Event Planning Survey!"
		self.css = "css/style.css"

		self.page_head = """
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
						<input type = "submit" value = "Submit" />
		'''
		self.page_close = '''
	</body>
</html>'''
		

	def print_out(self):
		all =  self.page_head + self.page_body + self.page_close
		all = all.format(**locals())
		return all