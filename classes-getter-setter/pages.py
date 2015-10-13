class Page(object):
	def __init__(self):
		self.__title = "Welcome!"
		self.__css = "css/style.css"
		self.head = """
<!DOCTYPE HTML>
<html>
	<head>
		<title>{self.title}</title>
		<link href = "{self.css}" rel = "Stylesheet" type = text/css" />
	</head>
	<body>
		"""

		self.__body = "Welcome to my OOP Python Page"
		self.close = """

	</body>
</html>
		"""

		self.whole_page = ""


	def update(self): #this replaces the print_out(self) below
		self.whole_page = self.head + self.body + self.close
		self.whole_page = self.whole_page.format(**locals())

	'''def print_out(self):
		all =  self.head + self.body + self.close
		all = all.format(**locals())
		return all''' #removing for further example of what getter/setter can do
	@property #we add this so the body will update as well! otherwise the OOP title shows up
	def body(self):
	    return self.__body

	@body.setter #
	def body(self, new_body):
		self.__body = new_body
		self.update()
	

	@property #making a setter, but setter has to have a getter (getter does not need a setter) so this will remain blank, as a placeholder for the setter below
	def title(self):
		return self.__title  #see below at self.__css for explanation

	@title.setter
	def title(self, new_title):
		self.__title = new_title
		self.update()

	@property
	def css(self):
		return self.__css  #need to add this so that we can change the title and css sheet on the main.py, otherwise they are not accessible by main.py

	@css.setter  #same as above, this is our decoration
	def css(self, new_css_file):
		self.__css = new_css_file
		self.update()

	    

	