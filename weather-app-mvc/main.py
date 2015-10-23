'''
mvc weather app
'''
import webapp2
import urllib2 #python classes and code needed to open up url info (requesting info, receiving info and opening it)
#from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	p = FormPage() #still uses page attributes except for private
    	p.inputs = [['zip', 'text', 'zip code'], ['Submit', 'submit']]
	self.response.write(p.print_out())

	if self.request.GET:  
	
	#get info from API
		zip = self.request.GET['zip'] #gets the zip code out of the url by self.request.GET
		url = "http://xml.weather.yahoo.com/forecastrss?p=" + zip #
	#assemble the request
		request = urllib2.Request(url) 
		opener = urllib2.build_opener()
	#use the url to get a result - request info from the API
		result = opener.open(request)

	#parse the XML
		xmldoc = minidom.parse(result) #allows us to access the items in the xml at yahoo weather
		self.response.write (xmldoc.getElementsByTagName('title')[2].firstChild.nodeValue)  
		self.content = '<br />' 
		list = xmldoc.getElementsByTagName("yweather:forecast") 
		self._dos = [] #dos is short for data objects
		for tag in list:
			do = WeatherData() #create a data object
			do.day = tag.attributes['day'].value
			do.high = tag.attributes['high'].value
			do.low = tag.attributes['low'].value
			do.date = tag.attributes['date'].value
			do.code = tag.attributes['code'].value
			do.condition = tag.attributes['text'].value
			self._dos.append(do) #put into data object
		print self._dos


		for item in list:
			self.content += "  HIGH: "+item.attributes['high'].value
			self.content += "  LOW: "+item.attributes['low'].value
			self.content += "  CONDITION: "+item.attributes['text'].value
			self.content += ' <img src = "img/'+item.attributes['code'].value+'.png"  width = "30" />'  
			self.content += '<br />'
			self.content += '<br />'

		
class WeatherData(object):	#'''this data object holds hte data fetched by the model and shown by the view'''
	def __init__(self):
		self.day = ''
    	self.high = ''
    	self.low = ''
    	self.code = '' 
    	self.condition = ''  
    	self.date = ''

class Page(object): 
	def __init__(self):		
		self._head = '''
<!DOCTYPE HTML>
<html>
	<head>
		<title>Weather App</title>
	</head>
	<body>'''

		self._body = 'Weather App'
		self._close = '''
	</body>
</html>'''

	def print_out(self):
		return self._head + self._body + self._close

class FormPage(Page): 
	def __init__(self):
	#constructor function for the super class
		super(FormPage, self).__init__()
		self._form_open = '<form method = "GET"">'
		self._form_close = '</form>'
		self.__inputs = []
		self._form_inputs = ''
		

	@property
	def inputs(self):
		pass

	@inputs.setter
	def inputs(self, arr):
		#change my private inputs variable
		self.__inputs = arr #assigning arr (array) to my private inputs variable

		#sort through the mega array and create HTML inputs based on the info there.
		print arr #test to see if it's printing through console (mega array all on one line)
		for item in arr: #prints each array item on a separate line (alternative to above)
			self._form_inputs += '<input type = "' + item[1] + '" name = "' + item[0]
			#if there is a third item... add it in
			if len(item) > 2:
				self._form_inputs += '" placeholder = "' + item[2] + '" />'
			#otherwise.. end the tag 
			else:
				self._form_inputs += '" />'
				
			
	
	def print_out(self):
		return self._head + self._body + self._form_open  + self._form_inputs + self._form_close + self._close



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
