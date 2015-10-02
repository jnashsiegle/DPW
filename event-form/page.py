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








		'''
		self.page_close = '''
	</body>
</html>'''
		

	def print_out(self):
		all =  self.page_head + self.page_body + self.page_close
		all = all.format(**locals())
		return all