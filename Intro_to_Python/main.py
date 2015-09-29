print "hello world" 

#one line comments
'''
Doc Strings
this comments out multi lines
'''
first_name = "Kermit"
last_name = "De Frog"

print first_name

#Collecting info from user - raw input method

#response = raw_input("Enter your name:  ")
#print "Hello there,", response,"!"

birth_year = 1965
current_year = 2015
age = current_year - birth_year
print "You are " + str(age) + " years old"
'''
Can't mix in concatanation int and strings so make the int 
a string temporarily by adding str and putting age in ()'s.
'''

budget = 90

if budget > 100:
	brand = "nike"
	print "Yay! We can buy cool " + brand + " shoes!"
elif budget > 50:
	print "We can at least get some generic sneakers."
else:
	print "No cool shoes for me."	

#example of what pass is for
budget = 90

if budget > 100:
	brand = "nike"
	print "Yay! We can buy cool " + brand + " shoes!"
elif budget > 50:
	#print "We can at least get some generic sneakers."
	pass
else:
	pass
	'''
	pass allows the code to run even without
	the conditions.  It's a temporary "pass"
	'''
#arrays

characters = ["leia", "luke", "chewy", "lando"]
characters.append("obi wan")
print characters
print characters [1]

#associative array
#called a dictionary in python

movies = dict() #create dictionary object
movies = {"Star Wars":"Darth Vader", "Silence of the Lambs":"Hannibal Lecter"}
print movies["Star Wars"]

#while Loop
i = 0
while i<9:
	print "The count is", i, ".  Obviously less than 9."
	i = i+1

#for loop

for i in range(0,10):
	print "The count is", i, ".  Between 0 and 10."
	i = i+1
	
#for each loop

rappers = ["Tupac", "Nas", "Biggie Smalls"]
for r in rappers:
	print "One of the best rappers is " + r

#functions

def calcArea(h, w):
	area = h * w 	
	return area
 
a = calcArea(20, 40);
#print "My area is " + str(a) + "sq ft"

#locals Method

weight = 200
height = 63
title = "Contact Us"
body = "You can contact us at contact@us.com"
message = '''
Your height is {height} and your weight is {weight}
<!DOCTYPE HTML>
<html>
	<head>
		<title>{title}</title>
	</head>
	<body>
		{body}
	</body>
</html>

'''
message = message.format(**locals())
print message



