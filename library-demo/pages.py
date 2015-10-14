class Page(object):
	def __init__(self):
		self.__title = "Welcome!"
		self.css = "css/style.css"
		self.__head = """
<!DOCTYPE HTML>
<html>
	<head>
		<title>Enter your information:</title>
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

	def print_out(self):
		all = self.__head + self.body + self.__error + self.__close
		return all