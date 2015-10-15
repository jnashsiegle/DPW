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

	@property
	def mon_exp(self):
	    return self.__mon_exp	


	@property
	def mon_income(self):
	    return self.__mon_income	

	'''def discretion(self):
		self.discretion = self.__mon_income - self.__mon_exp
	    return self.discretion'''

	def mortgage(self):
		self.mortgage = self.__mon_income * .25
		return self.mortgage

	def annual_income(self):
		self.annual_income = self.__mon_income * 12
		return self.annual_income
		


	