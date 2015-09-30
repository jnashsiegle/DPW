name = raw_input ("What is your name?  ")  #get player name for use within game
ran_num = raw_input("Choose a number between 1 and 100: ")#this number will be used to determine the end of the range a random number is generated from

from random import randint
print(randint(0,int(ran_num))) #generate a random number
if int(ran_num) < 50:  #let's use the random generated number to decide
	print "With slumped shoulders and a sly grin, Chris holds out the small bauble for all to see." #the fate of the story
else:
	if int(ran_num) >= 50:
		print " With a huff, " + name + " replies, 'Fine then, we need to get going anyway!'"