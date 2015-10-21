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
		<title>Avatars R Us!</title>
		<link rel="stylesheet" type="text/css" href="css/style.css">
	</head>
	<body>
	''' #repetitive header for top of all pages page
		self._header = '''
		<header><h1>Avatars R Us!</h1>				
		</header> '''
		#repetitive main content for all pages
		self._main = '''
		
		<div id = "wrapper">
		<h1>Classes</h1>
		<p>A class is the primary adventuring style of a player character which determines the type of weapons and armor it can use, as well as what abilities, powers, skills, and spells it will gain throughout its adventures.</p>
		<section id = "gallery">
		<ul id = "class_display">
			<li id = ""><a href = "?char=warrior"><img src = "img/warrior.png" alt = "Warrior"></a></li>
			<li><a href = "?char=paladin"><img src = "img/paladin.png" alt = "Paladin"></a></li>
			<li><a href = "?char=hunter"><img src = "img/hunter.png" alt = "Hunter"></a></li>
			<li><a href = "?char=rogue"><img src = "img/rogue.png" alt = "Rogue"></a></li>
			<li><a href = "?char=priest"><img src = "img/priest.png" alt = "Priest"></a></li>
			<li><a href = "?char=death_knight"><img src = "img/deathknight.png" alt = "Death Knight"></a></li>
			<li><a href = "?char=shaman"><img src = "img/shaman.png" alt = "Shaman"></a></li>
			<li><a href = "?char=mage"><img src = "img/mage.png" alt = "Mage"></a></li>
			<li><a href = "?char=warlock"><img src = "img/warlock.png" alt = "Warlock"></a></li>
			<li><a href = "?char=monk" ><img src = "img/monk.png" alt = "Monk" title = "monk"></a></li>
			<li><a href = "?char=druid"><img src = "img/druid.png" alt = "Druid"></a></li>			
			</ul>
		</section> <!--ends gallery-->
		</div> <!--ends wrapper -->'''
		self._submain = '''
		
		<div id = "wrapper3">
		<img id = "avatar" src = "img/main.png" alt = "pretty avatar" title = "avatar">
		</div>
		
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
		return  self._head + self._header + self._main + self._submain + self._footer + self._close  #sets the variable all to be all the sections.
		

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
		self.desc = ''
		self.image = ''
		self.footer = ''
		self._html = ''
		self._html_close = ''
			
		#let's make the html now
		self._html = '''
		<section id = "wrapper2">
		<article id = "classInfo"><h1>{self.title}</h1>
		<div id = "gradient"><img src = {self.image} alt = '{self.title}'>
		</article>
		<p>{self.desc}</p>
		<p><span>{self.title} Combat Type = </span>{self.type}</p>
		<p><span>{self.title} Standard = </span>{self.standard}</p>
		<p><span>Armor Available to {self.title} = </span>{self.armor}</p>
		<p><span>Weapons that {self.title}'s Use: </span> {self.weapons}</p>
						
		'''	
		self._html_close = '''
		</section>
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
	
		
	def print_out(self):			#defines a method to print out the form that we will call over in main.py
		all =  self._head + self._header  + self._html + self._html_close + self._main + self._footer + self._close  
		all = all.format(**locals())   
		return all