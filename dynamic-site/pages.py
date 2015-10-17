'''
Jana Nash-Siegle
10/17/2015
DPW - 01
Dynamic Site - Project 3
'''
class Page(object):
	def __init__(self):

		self.head = """   				
<!DOCTYPE HTML>							
<html>
	<head>
		<title>Bring a little class!</title>
		<link rel="stylesheet" type="text/css" href="css/style.css">
	</head>
	<body>"""

		self.header = '''
		<header><h1>Ready for a little excitement?</h1>
				<h1>Up for a challenge? Want a little class in life?</h1>
				<h1>What type of personality are you?</h1>
		</header>'''
		self.body = '''
		<article id = "wrapper">
		<h1>Classes</h1>
		<p>A class is the primary adventuring style of a player character which determines the type of weapons and armor it can use, as well as what abilities, powers, skills, and spells it will gain throughout its adventures.</p>
		<div id = "class_display"><img src = "img/druid.png" alt = "Druid"><img src = "img/hunter.png" alt = "Hunter"><img src = "img/mage.png" alt = "Mage"><img src = "img/monk.png" alt = "Monk"><img src = "img/paladin.png" alt = "Paladin"><img src = "img/priest.png" alt = "Priest"><img src = "img/rogue.png" alt = "Rogue"><img src = "img/shaman.png" alt = "Shaman"><img src = "img/warlock.png" alt = "Warlock"><img src = "img/warrior.png" alt = "Warrior"></div>
									
			
					
					
					
					
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