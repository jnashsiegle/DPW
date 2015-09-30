print "Welcome to Madlibs!  A fantasy world created by your words and imagination" #Welcome message

name = response = raw_input ("What is your name?  ")  #get player name for use within game

verb = response = raw_input(name+", please pick a verb: ") #grab a verb to use in story

meal = response = raw_input("What is your favorite meal? ")  #choose a meal

dessert = response = raw_input("Thank you " + name+", now what is your favorite dessert? ") #and an dessert

color = response = raw_input(name+", what is your favorite color: ") #what's a story without a color

animal = response = raw_input("Name an animal that lives on a farm. ") #and the animal

clothing = response = raw_input(name+", What article of clothing are you wearing right now: ") #not getting too personal are we?  nawwww

ran_num = response = raw_input("Choose a number between 1 and 100: ")#this number will be used to determine the end of the range a random number is generated from

from random import randint
print(randint(0,int(ran_num))) #generate a random number

friend = response = raw_input("What is your favorite name, " +name +"? ") #lets add a name for another character

vehicle = response = raw_input(name+", name any type of vehicle, land, air, or water please? ")
print vehicle   #what vehicle will the verb utilize in the story?

players = ["Mike", "John", "Chris", "Larry", "Moe"]  #and some friends or students
players.append(friend)
print players

cookies = response = raw_input(name+", How many cookies in a baker's dozen? ") #how many know a baker's dozen

even = response = raw_input("Quick!  What is the first even number you can think of? ") #I just need an even number

u_fruit = response = raw_input(name+", Choose one fruit, apple, lime or banana.  Please use all lowercase in your answer ") #let's use UI in order to pick the fruit for the color that will be used in the story!!
fruit = dict()
fruit = {"apple":"red", "lime":"green", "banana":"yellow"}  #what is more colorful than fruit?
print fruit[u_fruit]

weight = response = raw_input(name+", How much do you weigh? ")  #we need a weight to use in our stone conversion

weight = int(weight)		#turn our given weight back into an integer as the input made it a string

stone_weight = 0.0714285714 #stone weight to 1 pound

def calcStone(stone_weight,weight): #calculate pound to stone
   x = stone_weight*weight
   floatx = int(x)		#let's remove the decimals later in the story
   return floatx						#return stone

print calcStone(stone_weight,weight) 


#print(ran_num)   #checking to make sure I can call ran_num

if ran_num < 50:  #let's use the random generated number to decide
	#print "some statement here of the story" #the fate of the story
		pass
else:
	if ran_num > 50:
		#print ran_num + " then this is going to happen instead"
		pass
if cookies < 5:					#using if / else to determine if story uses bridge or ferry to get home
	#print "Then you can pass over the bridge"
		pass
else:
	if cookies > 4:
		#print "Then you must go down the river to the ferry"
		pass

#two sequence looping with zip function, questions and answers for dialog
questions = ['decision', 'answer', 'favorite food'] #question nouns
answers = ['yes', 'I think I shall', 'macaroni and cheese'] #answers REMEMBER TO ADD VERB IN STORY FOLLOWING I THINK I SHALL
for q, a in zip(questions, answers): #for statement zip function
	pass
	pass
	pass
	#print "What is your {0}? It is {1}. ".format(q, a) #formatting printing q a


print name+", would you " + verb + " to the store and pick up " + str(calcStone(stone_weight,weight)) + " pounds of flour so I can make " + dessert + " for " + meal + "?"
print name + " grabbed a " + color + " " + clothing + " to slip on while picking up the leash so the family " + animal + " named " + " " + friend + " could go along for the journey."
print "Hopping into the " + vehicle + " " + name + " calls " + players[2] + '"Meet me at the bridge" as the '  + str(fruit[u_fruit]) + " " + vehicle + " speeds off in that direction." 

