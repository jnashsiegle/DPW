"""created by Jana Nash-Siegle
DPW 101501
Wainman
10/14/2015
"""

class Form(object):
	def __init__(self):
		self.__head = """ 				
<!DOCTYPE HTML>							
<html>
	<head>
		<title>Where does my money go?</title>
		<link rel="stylesheet" type="text/css" href="css/style.css">
	</head>"""
		self.body = '''
	<body>				
		<article id = "wrapper">
		<header>
			<img src = "img/budget.png" alt = "picture of house on scale">
			<h1>Where does my money go?</h1>
			<p><a href = "http://www.bing.com">Exit Form</a></p>
		</header>
										
			<h3>Let's gather some information</h3> 
		<form method = "GET">					
						
			<div>
				<label>Your Name: </label><input type = "text" placeholder = "Name:  " name = "name" />
				<label>Your Email: </label><input type = "email" placeholder = "Email:  " name = "email" />
			</div>
				<label>Your Total Monthly Budget: </label><input type = "text" placeholder = "Total Monthly Expenses:  " name = "monExp" /><br />
				<label>Your Net Monthly Income: </label><input type = "text" placeholder = "Total Monthly Income:  " name = "monIncome" />
			<p>Current Budget Useage:</p>
				<label>Yes, I currently use a budget</label><input type = "radio" name = "budget" value = "do" checked />
				<label>Naww who needs a budget?</label><input type = "radio" name = "budget"  value = "do not"/>
			<hr>
				<input type = "submit" value = "Submit" />
		'''
		self.__results = '''
						<article id = "wrapper">
						<img src = "img/budget.png" alt = "picture of house on scale">				
						<h3>Input Expenses</h3> 
						'''

		self.__close = '''
					</form>
				</article>
	</body>
</html>'''

	#def print_out needs to be made a utility class in library
	def print_out(self):
		all = self.__head + self.body + self.__close
		all = all.format(**locals())   #uses a dictionary-based string formatting
		return all

class ResultsPage(object):
	def __init__(self):
		self.__head = """
<!DOCTYPE HTML>							
<html>
	<head>
		<title>Where does my money go?</title>
		<link rel="stylesheet" type="text/css" href="css/style.css">
	</head>"""
		self.__results = '''
	<body>				
		<article id = "wrapper">
		<header>
			<img src = "img/budget.png" alt = "picture of house on scale">
			<h1>Where does my money go?</h1>
			<p><a href = "http://www.bing.com">Exit Form</a></p>
		</header>										
			

			'''		
		self.__close = '''
					
		</article>
	</body>
</html>'''
		
	
	def print_out(self):
		all = self.__head +  self.__results
		all = all.format(**locals())   #uses a dictionary-based string formatting
		return all