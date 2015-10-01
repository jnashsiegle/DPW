#used as a playground to test/debug bits of the program at a time
weight = raw_input(name+", How much do you weigh? ")  #we need a weight to use in our stone conversion
weight = int(weight)		#turn our user given weight back into an integer as the input made it a string
stone_weight = 0.0714285714 #stone weight to 1 pound
def calcStone(stone_weight,weight): #calculate pound to stone
"""Converts pounds to stones. 
	calculates pound to stone weight
	turns x back into an integer and float it to remove decimals
	return floatx
	commented out the print function which we shall use as a test
	"""
   x = stone_weight*weight
   floatx = int(x)		#let's remove the decimals later in the story
   return floatx						#return stone

#print calcStone(stone_weight,weight) 



'''
Jana Nash-Siegle
Testing and debugging file
'''