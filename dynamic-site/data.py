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
		warrior.desc = '<p>Warriors are melee fighters highly trained in the art of weaponry. Melee combat is the warrior\'s strongest skill. They are strong and quick on the battlefield. Depending on their specialization, a warrior can often deal very high damage or be tough to kill. Warrior abilities depend on rage generation. This is different to all but one melee class, the bear form druid. Rage is generated through damage being dealt to and by the warrior and is capped at 100 (can be increased with Glyph of Unending Rage).</p><p>Warriors can change between three combat stances: [Battle Stance], [Defensive Stance], and, if you have chosen the level 100 talent Gladiators Resolve, [Gladiator Stance]. Stances give the class a fluid play style, allowing the player a variety of responses to any given PvE or PvP situation. Warriors can wear any type armor; beginning at level 40 they can wear plate, and at level 50 they receive [Plate Specialization]. They are able to use shields, wear a variety of armor, and wield any weapon with the exception of wands. Warrior is the only class that can be played by every selectable race in the game.</p>'
		#second instance of CharClass	
		paladin = CharClass()
		paladin.title = 'Paladin'
		paladin.type = 'Tank, Healer, Melee Damage Dealer'
		paladin.standard = 'Health, Mana'
		paladin.armor = 'Cloth, Mail, Leather, Plate, Shields'
		paladin.weapons = 'One-Handed Axes, One-Handed Maces, One-Handed Swords, Polearms, Two-Handed Axes, Two-Handed Maces, Two-Handed Swords'
		paladin.image = 'img/paladin.png'
		paladin.desc = '<p>The paladin is a hybrid class with the ability to play a variety of different roles including healing, tanking, and DPS. They have auras, blessings, and seals that provide useful buffs for other players while withstanding heavy physical damage with plate armor and strong defensive abilities. Paladins are considered to be holy knights[1] or blood knights.</p><p>Paladins are extremely effective against undead and demons - however contrary to popular belief, unless specifically stated their attacks do not do extra damage to either - its main bonus is that no race has any special resistance to it. A good Paladin player is always useful in a group, but in an Undead/Demon infested area, they are invaluable.</p>'


	#array of Data Objects from CharClass Instances used on main.py
		self.class_arr = [warrior, paladin]
		

				
	