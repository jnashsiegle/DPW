'''
Jana Nash-Siegle
10/17/2015
DPW - 01
Dynamic Site - Project 3
'''
#set up our base page this will be a page in abstract.  
class Page(object):   #abstract class
	def __init__(self):
		print "Base created" #test for our base
		#invisible heading info for pages
		self._head = '''   				
<!DOCTYPE HTML>							
<html>
	<head>
		<title>Bring a little class!</title>
		<link rel="stylesheet" type="text/css" href="css/style.css">
	</head>
	<body>
	''' #repetitive header for top of all pages page
		self._header = '''
		<header><h1>Ready for a little excitement?</h1>
				<h1>Up for a challenge? Want a little class in life?</h1>
				<h1>What type of personality are you?</h1>
		</header> '''
		#repetitive main content for all pages
		self._main = '''
		<article id = "wrapper">
		<h1>Classes</h1>
		<p>A class is the primary adventuring style of a player character which determines the type of weapons and armor it can use, as well as what abilities, powers, skills, and spells it will gain throughout its adventures.</p>
		<div id = "class_display">
			<a href = "?char=warrior"><img src = "img/warrior.png" alt = "Warrior"></a>
			<a href = "?char=paladin"><img src = "img/paladin.png" alt = "Paladin"></a>
			<a href = "?char = hunter"><img src = "img/hunter.png" alt = "Hunter"></a>
			<a href = "?char = rogue"><img src = "img/rogue.png" alt = "Rogue"></a>
			<a href = "?char = priest"><img src = "img/priest.png" alt = "Priest"></a>
			<a href = "?char = death_knight"><img src = "img/deathknight.png" alt = "Death Knight"></a>
			<a href = "?char = shaman"><img src = "img/shaman.png" alt = "Shaman"></a>
			<a href = "?char = mage"><img src = "img/mage.png" alt = "Mage"></a>
			<a href = "?char = warlock"><img src = "img/warlock.png" alt = "Warlock"></a>
			<a href = "?char = monk"><img src = "img/monk.png" alt = "Monk">
			<a href = "?char = druid"><img src = "img/druid.png" alt = "Druid">
			</div>
		</article>
		'''
		#repetive footer content for all pages						
		self._footer = '''
		<footer>&copy;2015, Jana Nash-Siegle
		<small>All images of World of Warcraft are the property of <a href = "http://eu.blizzard.com/en-gb/company/about/legal-faq.html" >Blizzard Entertainment.</a><br />
		This site is in no way affiliated with World of Warcraft or Blizzard Entertainment.  It has been created for personal use fulfilling the sole purpose of fulfilling a school project.</small></footer>
		'''
		self._close = '''
	</body>
</html>
'''	
#print out landing page
	def print_out(self):			#defines a method to print out the form that we will call over in main.py
		all =  self._head + self._header + self._main + self._footer + self._close  #sets the variable all to be all the sections.
		all = all.format(**locals())   #uses a dictionary-based string formatting
		return all

#child page to Page | this will display when image is clicked and adds in class information
class CharPage(Page):
	def __init__(self):
	#subclass of Page
	#contents of char specific info
		super(CharPage, self).__init__()
		self.title = ''
		self.type = ''
		self.standard = ''
		self.armor = ''
		self.weapons = ''
		self._html = ''
		self._html_close = ''
			
		#let's make the html now
		self._html = '''
		<article id = "wrapper2">
		<p>Hellooooooo????  Yay!  We are here!</p>
		<h1> We are in an H1..there is a self.title inside this h1 too..but it doesn't want to print {self.title}</h1>
		<h1> Armor = {self.armor}</h1>
		<h1> Weapons = {self.weapons}</h1>
				
		'''	
		self._html_close = '''
		</article>
		'''
	#getters/ setters for variables
	#this one for self._html works	
	@property
	def html(self):
		return self._html
	@html.setter
	def html(self, h):
		#change my private inputs variable
		return

		#this one is not...I'm assuming I need this to fill in the h1's up there 
	@property 
	def title(self):
		return self._title
	@title.setter
	def title(self, n):
		self._title = n

#print out individual character class when called up via img click
	def print_out_char(self):			#defines a method to print out the form that we will call over in main.py
		all =  self._head + self._header  + self._html + self._html_close + self._main + self._footer + self._close  
		all = all.format(**locals())   
		return all