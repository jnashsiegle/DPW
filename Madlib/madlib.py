print "Welcome to Madlibs!  A fantasy world created by your words and imagination"

name = response = raw_input ("What is your name?  ")

response = raw_input(name+", please pick a verb: ")

response = raw_input("Please pick a noun: ")

response = raw_input("Thank you " + name+", now would you please pick an adjective: ")

response = raw_input(name+", what is your favorite color: ")

response = raw_input("Name an animal that lives on a farm. ")

response = raw_input(name+", What article of clothing are you wearing right now: ")

ran_num = response = raw_input("Choose a number between 1 and 100: ")

from random import randint
print(randint(0,int(ran_num)))
