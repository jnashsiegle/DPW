name = raw_input ("What is your name?  ")  #get player name for use within game
#two sequence looping with zip function, questions and answers for dialog
questions = ['decision', 'answer', 'favorite food'] #question nouns
answers = ['yes', 'I think I shall', 'macaroni and cheese'] #answers REMEMBER TO ADD VERB IN STORY FOLLOWING I THINK I SHALL
for q, a in zip(questions, answers): #for statement zip function
	
	print "What is your {0}? It is {1}. ".format(q, a) #formatting printing q a

print " With a huff, " + name + " replies, 'Fine then, we need to get going anyway!'"
print "After a period of time, they arrive at the store and pick out the flour that was needed.  Larry inundates " + name + " with questions, non-stop."
print "What is your {0}? It is {1}. ".format(q, a)