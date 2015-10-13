import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	#tommy's grade
        t = Transcript()
        t.grade1 = 90   
        t.grade2 = 100
        t.quiz1 = 75
        t.quiz2 = 99
        t.final_grade = 99 #overwriting final grade with setter BUT the calculation will still be the avg'd result
        self.response.write("Tommy's final grade is a " + str(t.final_grade)) #another example of str(t.final_grade_getter)) but removed getter as unnecessary so will need to separate calculation out under setter as def calc_grade

        #sally's grade
        s = Transcript()
        s.grade1 = 45   
        s.grade2 = 80
        s.quiz1 = 66
        s.quiz2 = 76
        s.calc_grade() #make sure sally's grade get's calculated not overwritten with tommy's 
        self.response.write ("<br />  Sally's final grade is a " + str(s.final_grade))

class Transcript(object):
	def __init__(self):
		self.grade1 = 0 #no underscores - public
		self.grade2 = 0
		self.quiz1 = 0
		self.quiz2 = 0 
		self.final_exam = 0
		self.__final_grade = 0 #two underscores - private only accessible in private class  

	@property
	def final_grade(self): #originally def final_grade_getter(self): but took out getter as unnecessary and to match up to all code
		#calculate final grade - shows us that setter can do so much more but this is handled below with the def calc_grade(self):
		#self.__final_grade = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2 + self.final_exam) / 5
		return self.__final_grade

	@final_grade.setter
	def final_grade(self, new_final_grade):
		self.__final_grade = new_final_grade

	def calc_grade(self):
		#calculate final grade but we need to make sure sally's grade get's calculated not overwritten so add s.calc_grade under sally's methods
		self.__final_grade = (self.grade1 + self.grade2 + self.quiz1 + self.quiz2 + self.final_exam) / 5



	     

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
