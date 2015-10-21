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
		self.pet = ''

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
		warrior.desc = '<p>Warriors are melee fighters highly trained in the art of weaponry. Melee combat is the warrior\'s strongest skill. They are strong and quick on the battlefield. Depending on their specialization, a warrior can often deal very high damage or be tough to kill. Warrior abilities depend on rage generation. This is different to all but one melee class, the bear form druid. Rage is generated through damage being dealt to and by the warrior and is capped at 100 (can be increased with Glyph of Unending Rage).</p><p>Warriors can change between three combat stances: [Battle Stance], [Defensive Stance], and, if you have chosen the level 100 talent Gladiators Resolve, [Gladiator Stance]. Stances give the class a fluid play style, allowing the player a variety of responses to any given PvE or PvP situation. </p>'
		#second instance of CharClass	
		paladin = CharClass()
		paladin.title = 'Paladin'
		paladin.type = 'Tank, Healer, Melee Damage Dealer'
		paladin.standard = 'Health, Mana'
		paladin.armor = 'Cloth, Mail, Leather, Plate, Shields'
		paladin.weapons = 'One-Handed Axes, One-Handed Maces, One-Handed Swords, Polearms, Two-Handed Axes, Two-Handed Maces, Two-Handed Swords'
		paladin.image = 'img/paladin.png'
		paladin.desc = '<p>The paladin is a hybrid class with the ability to play a variety of different roles including healing, tanking, and DPS. They have auras, blessings, and seals that provide useful buffs for other players while withstanding heavy physical damage with plate armor and strong defensive abilities. Paladins are considered to be holy knights or blood knights.</p><p>Paladins are extremely effective against undead and demons - however contrary to popular belief, unless specifically stated their attacks do not do extra damage to either - its main bonus is that no race has any special resistance to it. A good Paladin player is always useful in a group, but in an Undead/Demon infested area, they are invaluable.</p>'
		#third instance of CharClass	
		hunter = CharClass()
		hunter.title = 'Hunter'
		hunter.type = 'Ranged Physical Damage Dealer'
		hunter.standard = 'Health, Focus'
		hunter.armor = 'Cloth, Leather, Mail'
		hunter.weapons = 'Bows, Crossbows, Guns'
		hunter.image = 'img/hunter.png'
		hunter.desc = '<p>Hunters pull, use threat redirection, crowd control, and primarily ranged damage. Hunters have pets that add to their DPS, add group- and raid- wide buffs, and help manage aggro. They can also track, tame, and train animals and beasts found in the wild. The well trained pet, on countless occasions, has saved a hunter\'s life. They are the only class that can name, feed, and &apos;train&apos; their pets; they can also be &apos;trained&apos; to have one of three specializations: Ferocity for burst DPS, Cunning for utility, and Tenacity for tanking. This specialization can be switched at any time when not in combat or dead.</p>'
		hunter.pet = '<p>Hunters utilize a pet to help them in combat</p>'#my POLYMORPH EXAMPLE
		#fourth instance of CharClass
		rogue = CharClass()
		rogue.title = 'Rogue'
		rogue.type = 'Melee Damage Dealer'
		rogue.standard = 'Health, Energy'
		rogue.armor = 'Cloth, Leather'
		rogue.weapons = 'Daggers, Fist Weapons, One-Handed Axes, One-Handed Maces, One-Handed Swords'
		rogue.image = 'img/rogue.png'
		rogue.desc = '<p>Rogues are melee damage dealers. They have access to a wide range of specials that depend on their constantly refilling pool of energy. Unlike other classes, such as the ranged hunter, rogues should be in close to attack.</p><p>The primary advantage rogues have is their ability to stealth. Unless the rogue is very close and in a 180 degree arc in front of them or much lower level, players are usually unable to see them.</p>'
		#fifth instance of CharClass
		priest = CharClass()
		priest.title = 'Priest'
		priest.type = 'Healer, Ranged Magic Damage Dealer'
		priest.standard = 'Health, Mana'
		priest.armor = 'Cloth'
		priest.weapons = 'Daggers, One-Handed Maces, Staves, Wands'
		priest.image = 'img/priest.png'
		priest.desc = '<p>Priests are masters of healing and preservation, infused with the light they can restore their wounded allies, shield them in battle, and even resurrect them from death. While they have a variety of protective and enhancement spells to bolster their allies, they can also wreak terrible vengeance on their enemies, using the grand powers of the Holy Light to smite and purge them, or the devastating powers of the shadow to decimate their minds. The priest is a diverse and powerful class, highly desirable in any group, and capable of fulfilling multiple roles.</p>'
		#6th instance of CharClass
		death_knight = CharClass()
		death_knight.title = 'Death Knight'
		death_knight.type = 'Tank, Melee Damage Dealer'
		death_knight.standard = 'Health, Runic'
		death_knight.armor = 'Cloth, Leather, Mail, Plate'
		death_knight.weapons = 'One-Handed Axes, One-Handed Maces, One-Handed Swords, Polearms, Two-Handed Axes, Two-Handed Maces, Two-Handed Swords'
		death_knight.image = 'img/deathknight.png'
		death_knight.desc = '<p>Death knights (introduced in Wrath of the Lich King) boast powerful melee abilities, as well as plate armor. These warriors supplement their strength with dark magic. Calling upon a rune system of magic, the death knight may summon unholy, blood, and frost spells. The criterion for creating a death knight is the existence of a level 55+ character on the player\'s account on any realm.</p>'
		#7th instance of CharClass
		shaman = CharClass()
		shaman.title = 'Shaman'
		shaman.type = 'Healer, Ranged Magic Damage Dealer, Melee Damage Dealer'
		shaman.standard = 'Health, Mana'
		shaman.armor = 'Cloth, Leather, Mail, Shields'
		shaman.weapons = 'Daggers, Fist Weapons, One-Handed Axes, One-Handed Maces, Staves, Two-Handed Axes, Two-Handed Maces'
		shaman.image = 'img/shaman.png'
		shaman.desc = '<p>Shaman is a hybrid class and can specialize in offensive spellcasting, melee damage dealing, or healing. As such, the class is considered one of the most adaptable and versatile in the game. Shaman can also provide group support in the form of stationary totems that, when placed on the ground by the shaman, either provide benefits to party members or deal damage to enemies.</p>'
		#8th instance of CharClass
		mage = CharClass()
		mage.title = 'Mage'
		mage.type = 'Ranged Magic Damage Dealer'
		mage.standard = 'Health, Mana'
		mage.armor = 'Cloth'
		mage.weapons = 'Wands, Daggers, One-Handed Swords, Staves'
		mage.image = 'img/mage.png'
		mage.desc = '<p>The Mage is a DPS caster that specializes in burst damage and area of effect spells. Their primary role in a group is damage dealing and crowd control through the use of Polymorph, temporarily changing humanoids and beasts into harmless critters. At end-game levels, mages\' damage is supplemented with spells like Counterspell, Remove Curse, and Spellsteal. Mages\' utility spells also include conjuring food and drink and the ability to teleport to major cities and open portals for party members. In PvP, mages deal ranged damage while using snare effects and Polymorph to control enemy players.</p>'
		#9th instance of CharClass
		warlock = CharClass()
		warlock.title = 'Warlock'
		warlock.type = 'Ranged Magic Damage Dealer'
		warlock.standard = 'Health, Mana'
		warlock.armor = 'Cloth'
		warlock.weapons = 'Daggers, One-Handed Swords, Staves, Wands'
		warlock.image = 'img/warlock.png'
		warlock.desc = '<p>Warlocks are former magi, or in the case of the Orcs, former shamans. In pursuit of ever-greater sources of power they have cast off their studies of the arcane or nature magics to delve deeper into the darker, fel-based magic of shadow.</p><p>Warlocks are renowned for their damage over time (DoT) spells, sinister Shadow magic, summoning demonic minions, and their ability to wreak havoc with destructive fire spells. Warlocks can specialize in any of these areas: Affliction warlocks are the masters of damage over time, draining their targets\' health with an array of powerful debuffs; Demonology warlocks summon improved demons to do their bidding, drawing power from their minions and even transforming into demons themselves; Destruction warlocks call down a rain of fire upon their enemies, specializing in potent burst damage and fire spells.</p>'
		#10th instance of CharClass
		monk = CharClass()
		monk.title = 'Monk'
		monk.type = 'Tank, Healer, Melee Damage Dealer'
		monk.standard = 'Health, Chi, Energy, Mana'
		monk.armor = 'Cloth, Leather'
		monk.weapons = 'Fist Weapons, One-Handed Axes, One-Handed Maces, One-Handed Swords, Polearms, Staves'
		monk.image = 'img/monk.png'
		monk.desc = '<p>Monks are a hybrid class. Masters of bare-handed combat, monks choose to draw their weapons only for devastating finishing moves. Monk healers bring harmony and balance to every group, healing even the most grievous of injuries with ancient remedies and focused spiritual arts. Few can hope to outlast the unquenchable prowess of the monk Brewmaster, whose empowering beverages and unpredictable combat style allow them to absorb incredible amounts of punishment.<p>'
		#11th instance of CharClass
		druid = CharClass()
		druid.title = 'Druid'
		druid.type = 'Tank, Healer, Ranged Magic Damage Dealer, Melee Damage Dealer'
		druid.standard = 'Health, Mana, Rage, Energy'
		druid.armor = 'Cloth, Leather'
		druid.weapons = 'Daggers, Fist Weapons, One-Handed Maces, Polearms, Staves, Two-Handed Maces'
		druid.image = 'img/druid.png'
		druid.desc = '<p>The druid is a shapeshifting, hybrid class and also one of the most versatile classes in the game. As with other hybrids, druids need to specialize in a single role for the best results. Due to their need to shape-shift to fulfill roles, they can only perform one role at a time; they must switch between the different shapes to adapt to changing situations.<p>'



	#array of Data Objects from CharClass Instances used on main.py
		self.class_arr = [warrior, paladin, hunter, rogue, priest, death_knight, shaman, mage, warlock, monk, druid]
		

				
	