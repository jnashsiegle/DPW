'''
created by Jana Nash-Siegle
DPW 101501
Wainman
'''

print "Welcome to Madlibs!  A fantasy world created by your words and imagination" #Welcome message

name = raw_input ("What is your name?  ")  #get player name for use within game

verb = raw_input(name+", please pick a verb: ") #grab a verb to use in story

meal = raw_input("What is your favorite meal, breakfast lunch or dinner? ")  #choose a meal

dessert = raw_input("Thank you " + name+", now what is your favorite dessert? ") #and an dessert

color = raw_input(name+", what is your favorite color: ") #what's a story without a color

animal = raw_input("Name an animal that lives on a farm. ") #and the animal

clothing = raw_input(name+", What article of clothing are you wearing right now: ") #not getting too personal are we?  nawwww

ran_num = raw_input("Choose a number between 1 and 100: ")#this number will be used to determine the end of the range a random number is generated from

friend = raw_input("What is your favorite name, " +name +"? ") #lets add a name for the family pet

vehicle = raw_input(name+", name any type of vehicle, land, air, or water please? ")
#print vehicle   #what vehicle will the verb utilize in the story?

players = ["Mike", "John", "Chris", "Larry", "Moe"]  #and some friends or students or pets, it's a name pool
players.append(friend)
#print players

cookies = raw_input(name+", Pick a number between 1-10? ") #need it to determine bridge access

u_fruit = raw_input(name+", Choose one fruit, apple, lime or banana.  Please use all lowercase in your answer ") #let's use UI in order to pick the fruit for the color that will be used in the story!!
fruit = dict()
fruit = {"apple":"red", "lime":"green", "banana":"yellow"}  #what is more colorful than fruit?
#print fruit[u_fruit] will be used to color the user's vehicle

weight = raw_input(name+", How much do you weigh? ")  #we need a weight to use in our stone conversion
weight = int(weight)		#turn our user given weight back into an integer as the input made it a string
stone_weight = 0.0714285714 #stone weight to 1 pound
def calcStone(stone_weight,weight): #calculate pound to stone
   x = stone_weight*weight
   floatx = int(x)		#let's remove the decimals later in the story
   return floatx						#return stone

#print calcStone(stone_weight,weight) 
print "++++++++++++===================================++++++++++++++++++"
print "++++++++++++===================================++++++++++++++++++"
print "++++++++++++===================================++++++++++++++++++"
print "++++++++++++===================================++++++++++++++++++"
print "++++++++++++===================================++++++++++++++++++"
print "++++++++++++===================================++++++++++++++++++"
print "A Trip To the Store" # title of our story

print "     " + name+", would you " + verb + " to the store and pick up " + str(calcStone(stone_weight,weight)) + " pounds of flour so I can make " + dessert + " for " + meal + "?"
print name + " grabs a/some " + color + " " + clothing + " to slip on while picking up the leash so the family " + animal + " named" + " " + friend + " could go along for the journey."
print "Hopping into the " + vehicle + " " + name + " calls " + players[3] + " " + '"Meet me at the bridge" as the '  + str(fruit[u_fruit]) + " " + vehicle + " speeds off in that direction." 
print "Arriving at the bridge the troll guard demands the toll be paid."
#I need if else results here to determine course of story

if int(cookies) < 5:		#need str() to make an int again | using if / else to determine if story uses bridge or ferry to get across
	print "'I refuse to pay the toll!' is the response.  'Then you must go down the river to the ferry, you may not use the bridge or air-space!'" + name + " proceeds down to the ferry."
else:
	if int(cookies) >= 5: #upon user entry it's a str and it needs to be an int
		print "'I will gladly pay your toll, kind Sir!'" + name + " replies and is allowed to pass."

print "     As the bridge becomes a small feature in the distance " + name + " finally finds " + players[3] + " who appears to be holding a small stone in his hand.  'What is that you have?,' " + name + " asks while reaching for the small object.  Hand jerking away a loud, if childish reply can be heard 'Do not touch! It is mine!'" + players[3] + " shouts out.  A collective sigh can be heard from all the other players, " + ', '.join(players) + " at this childish display."
from random import randint
#print(randint(0,int(ran_num))) #generate a random number (for test use only)
if int(ran_num) < 50:  #let's use the random generated number to decide
	print "With slumped shoulders and a sly grin, Chris holds out the small bauble for all to see." #the fate of the story
else:
	if int(ran_num) >= 50:
		print " With a huff, " + name + " replies, 'Fine then, we need to get going anyway!'"

		#two sequence looping with zip function, questions and answers for dialog
questions = ['favorite dessert', 'mom making then today?', 'favorite food'] #question nouns
answers = ['Strawberry Cake', ' hmmm, I honestly do not know', 'macaroni and cheese'] #answers 

print "After a period of time, they arrive at the store and pick out the flour that was needed.  Larry all of a sudden gets all excited thinking about the upcoming treats and inundates " + name + " with questions, non-stop."
for q, a in zip(questions, answers): #for statement zip function	
	print "What is your {0}? It is {1}. ".format(q, a) #formatting printing q a  list out questions

print "With a hand held high " + name + " interrupts " + players[3] + " hold on there big fella, why don't we just wait until we get home, give mom time to cook us up some yummy vittles and we can discuss this like the good cowpokes we are?, " + name + " replies with a laugh and fake accent.  With that the two head home and are treated to a wonderful " + meal + "."

print "++========== THE END =========++"






		
