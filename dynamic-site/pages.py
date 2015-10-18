'''
Jana Nash-Siegle
10/17/2015
DPW - 01
Dynamic Site - Project 3
'''
#set up our base page this will be a page in abstract.  
class Page(object):
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
			<a href = "?char = paladin"><img src = "img/paladin.png" alt = "Paladin"></a>
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
		<p>&copy;2015, Jana Nash-Siegle</p>
		<small>All images of World of Warcraft are the property of <a href = "http://eu.blizzard.com/en-gb/company/about/legal-faq.html" >Blizzard Entertainment.</a><br />
		This site is in no way affiliated with World of Warcraft or Blizzard Entertainment.  It has been created for personal use fulfilling the sole purpose of fulfilling a school project.</small>
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
		self.__html = '''
		<h1>{self.title}</h1>
		<h1>{self.armor}</h1>
		<h1>{self.weapons}</h1>
		<img src = {self.image}>
		'''	
		self._html_close = ''

	@property
	def html(self):
		return self.__html
	@html.setter
	def html(self, h):
		#change my private inputs variable
		self.__html = h #assigning arr (array) to my private inputs variable
		#print h #test to see if it's printing through console (mega array all on one line)

#print out individual character class when called up via img click
	def print_out_char(self):			#defines a method to print out the form that we will call over in main.py
		all =  self._head + self._header +  self._main + str(self.__html) + self._html_close + self._footer + self._close  
		all = all.format(**locals())   #uses a dictionary-based string formatting
		return all