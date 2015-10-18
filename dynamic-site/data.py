'''
Jana Nash-Siegle
10/17/2015
DPW - 01
Dynamic Site - Project 3
'''
#Data Objects

class CharClass(object): #modified name slightly to differentiate between WoW classes and Python classes
	def __init__(self): #flipping the switch on our class
	#attributes of each character
		self.title = ''
		self.type = ''
		self.standard = ''
		self.armor = ''
		self.weapons = ''
		self.image = ''

#Data for our Class Template
class Data(object):
	def __init__(self): #crank it up
	#first instance of CharClass
		warrior = CharClass()
		warrior.title = 'Warrior'
		warrior.type = 'Tank, Melee, Damage Dealer'
		warrior.standard = 'Health, Rage'
		warrior.armor = 'Cloth, Leather, Mail, Plate, Shields'
		warrior.weapons = 'Daggers, Fist Weapons, One-Handed Axes, One-Handed Maces, One-Handed Swords, Polearms, Staves, Two-Handed Axes, Two-Handed Maces, Two-Handed Swords'
		warrior.image = 'img/warrior.png'
		
	#second instance of CharClass
	
		paladin = CharClass()
		paladin.title = 'Paladin'
		paladin.type = 'Tank, Healer, Melee Damage Dealer'
		paladin.standard = 'Health, Mana'
		paladin.armor = 'Cloth, Mail, Leather, Plate, Shields'
		paladin.weapons = 'One-Handed Axes, One-Handed Maces, One-Handed Swords, Polearms, Two-Handed Axes, Two-Handed Maces, Two-Handed Swords'
		paladin.image = 'img/paladin.png'


	#array of Data Objects from CharClass Instances
		self.class_arr = [warrior, paladin]
	