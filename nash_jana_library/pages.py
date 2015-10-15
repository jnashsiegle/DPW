class Form(object):
	def __init__(self):
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
						<div name = "tran1" id = "tran1">
						<div class = "payee">
							<label>Name: </label><input type = "text" placeholder = "Payee:  " name = "payee" />
							<label>Amount: </label><input type = "text" placeholder = "Amount:  " name = "amount" />
							<label>Date: </label><input id="dot" name="dot" type="date">
						</div>
						<div class = "category">
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
						<div class = "misc">							
							<p>What type of transaction is this?</p>
							<label>Household Budget</label><input type = "radio" name = "budget" value = "household" checked />
							<label>Discretionary / Recreational</label><input type = "radio" name = "budget"  value = "discretionary"/>
							
						</div>
						<hr>
						</div>

						<div name = "tran2" id = "tran2">
						<div class = "payee">
							<label>Name: </label><input type = "text" placeholder = "Payee:  " name = "payee" />
							<label>Amount: </label><input type = "text" placeholder = "Amount:  " name = "amount" />
							<label>Date: </label><input id="dot" name="dot" type="date">
						</div>
						<div class = "category">
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
						<div class = "misc">							
							<p>What type of transaction is this?</p>
							<label>Household Budget</label><input type = "radio" name = "budget" value = "household" checked />
							<label>Discretionary / Recreational</label><input type = "radio" name = "budget"  value = "discretionary"/>
							
						</div>
						<hr>
						</div>	

						<div name = "tran3" id = "tran3">
						<div class = "payee">
							<label>Name: </label><input type = "text" placeholder = "Payee:  " name = "payee" />
							<label>Amount: </label><input type = "text" placeholder = "Amount:  " name = "amount" />
							<label>Date: </label><input id="dot" name="dot" type="date">
						</div>
						<div class = "category">
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
						<div class = "misc">							
							<p>What type of transaction is this?</p>
							<label>Household Budget</label><input type = "radio" name = "budget" value = "household" checked />
							<label>Discretionary / Recreational</label><input type = "radio" name = "budget"  value = "discretionary"/>
							
						</div>
						<hr>
						</div>	

						<div name = "tran4" id = "tran4">
						<div class = "payee">
							<label>Name: </label><input type = "text" placeholder = "Payee:  " name = "payee" />
							<label>Amount: </label><input type = "text" placeholder = "Amount:  " name = "amount" />
							<label>Date: </label><input id="dot" name="dot" type="date">
						</div>
						<div class = "category">
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
						<div class = "misc">							
							<p>What type of transaction is this?</p>
							<label>Household Budget</label><input type = "radio" name = "budget" value = "household" checked />
							<label>Discretionary / Recreational</label><input type = "radio" name = "budget"  value = "discretionary"/>
							
						</div>
						<hr>
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
	</head>
	<body>		
		<header><h1>The many outputs of my budget.</h1>
		<p><a href = "http://www.bing.com">Exit Form</a></p>
		</header>

		 <article id = "wrapper">
						<img src = "img/budget.png" alt = "picture of house on scale">				
						<h3>Transaction Results</h3> """


						
		self.result = ""
		self.__close = """
	</body>
</html>
		"""
	
	def print_out(self):
		all = self.__head + self.__close
		all = all.format(**locals())   #uses a dictionary-based string formatting
		return all