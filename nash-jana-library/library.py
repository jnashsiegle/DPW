"""created by Jana Nash-Siegle
DPW 101501
Wainman
10/14/2015
"""



class BudgetBreak(object):
	def __init__(self):			
		self.name = ''
		self.email = ''
		self.__mon_exp = 0
		self.__mon_income = 0	
		self.discretion = 0
		self.annual_income = 0

	'''@property
	def mon_exp(self):
	    return self.__mon_exp	


	@property
	def mon_income(self):
	    return self.__mon_income'''	
	

	def annual_income(self):
		return self.__mon_income * 12
		

	def discretion(self):
		return self.__mon_income - self.__mon_exp

	def calcMortgage(self):
		return self.__mon_income * 0.25

		#getting monthly expense access
	@property
	def mon_exp(self):
		return self.__mon_exp	

		#setting new variable for monthly expense
	@mon_exp.setter
	def mon_exp(self, e):
		self.__mon_exp = e

		#getting monthly income access
	@property
	def mon_income(self):
	    return self.__mon_income

	@mon_income.setter
	def mon_income(self, i):
		self.__mon_income = i	


	def getIncome(self):
		return self.__mon_income

	def setIncome(self, i):
		self.__mon_income = i

		

		


	