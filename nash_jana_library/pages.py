class Form(object):
	def __init__(self):
		self.css = "css/style.css"
		self.__head = """ 				
<!DOCTYPE HTML>							
<html>
	<head>
		<title>Where does my money go?</title>
		<link rel="stylesheet" type="text/css" href="css/style.css">
	</head>
	<body>

		
		<header><h1>Where does my money go?</h1>
		<p><a href = "http://www.bing.com">Exit Form</a></p>
		</header>"""
		self.body = '''<article id = "wrapper">
						<img src = "img/budget.png" alt = "picture of house on scale">				
						<h3>Input Expenses</h3> 
					
					
					<form method = "GET">
						<div id = "payee">
							<label>Name: </label><input type = "text" placeholder = "Payee:  " name = "payee" />
							<label>Amount: </label><input type = "text" placeholder = "Amount:  " name = "amount" />
							<label>Date: </label><input id="dot" name="dot" type="date">
						</div>
						<div id = "category">
							<label>Category of Expense</label>
								<select name = "category">
									<option value = "">Click here to see options</option>
									<option value = "food">Food</option>
									<option value = "clothing">Clothing</option>
									<option value = "personal">Personal</option>
									<option value = "fun">Fun</option>
									<option value = "medical">Medical</option>
								</select>							
						</div>					
						
						<div id = "misc">
							
							<p>What type of transaction is this?</p>
							<label>Household Budget</label><input type = "radio" name = "budget" value = "household" checked />
							<label>Discretionary / Recreational</label><input type = "radio" name = "budget"  value = "discretionary"/>
							
						</div>	
										
						<p><input type = "submit" value = "Submit" /></p>
		'''
		self.__close = '''
					</form>
				</article>
	</body>
</html>'''

	#def print_out needs to be made a utility class in library
	def print_out(self):
		all = self.__head + self.body + self.__close
		return all

class ResultsPage(object):
	def __init__(self):
		self.__title = "Welcome!"
		self.css = "css/style.css"
		self.__head = """
<!DOCTYPE HTML>
<html>
	<head>
		<title>Where does my money go?</title>
		<link href = "css/style.css" rel = "stylesheet" type = "text/css" />
	</head>
	<body>
		"""

		self.body = ""
		self.__error = '' #this won't be used, just comes with Page Class
		self.__close = """
	</body>
</html>
		"""
	#def print_out needs to be made a utility class in library
	def print_out(self):
		all = self.__head + self.body + self.__error + self.__close
		return all