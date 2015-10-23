'''
etree weather app
'''
import webapp2
import urllib2 #python classes and code needed to open up url info (requesting info, receiving info and opening it)
#from xml.dom import minidom
from xml.etree.ElementTree import QName
import xml.etree.ElementTree as ET #so we don't have to retype the whole long string any longer


class MainHandler(webapp2.RequestHandler):
    def get(self):
    	p = FormPage() #still uses page attributes except for private
    	p.inputs = [['zip', 'text', 'zip code'], ['Submit', 'submit']]
	self.response.write(p.print_out())

	if self.request.GET:  #this makes it so that it works only if there is a zip variable in the url otherwise it stays blank...otherwise it would generate an error
	
	#get info from API
		zip = self.request.GET['zip'] #gets the zip code out of the url by self.request.GET
		url = "http://xml.weather.yahoo.com/forecastrss?p=" + zip #zip comes out of url using the following request.GET
	#assemble the request
		request = urllib2.Request(url) #requesting the url
	#use the urllib2 to create object to get the url
		opener = urllib2.build_opener()
	#use the url to get a result - request info from the API
		result = opener.open(request)

	#parse the XML - this will change depending on if using minidom, etree whatever API
		xmldoc = ET.parse(result)
		root = xmldoc.getroot()

		namespace = "http://xml.weather.yahoo.com/ns/rss/1.0"    #comes from the xml page of yweather

		content = "<br />" #content variable
		content = root[0][12][7].attrib['day'] + "<br />"  #root is the rss, the xml for this title is an array in an array (channel is first array of items)| It needs the .text in order to print out what's between the tags here.
		for i in root.iter("{"+namespace+"}forecast"):    #this asks for it to iterate through all the things in forecast on the xml page of yweather
			content += i.attrib['day'] + "---HIGH:" + i.attrib['high'] + "  " + "--LOW:" + i.attrib['low']
			content += "<br />" 
		self.response.write(content)

        

class Page(object):  #borrowing stuff from the object class  | ABSTRACT CLASS ONLY EXISTS TO BE THE SUPER TO THE SUBS THERE IS NO INSTANCE OF PAGE
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

class FormPage(Page): #subclass of Page, which is why Page is in ()
	def __init__(self):
	#constructor function for the super class
		super(FormPage, self).__init__()
		self._form_open = '<form method = "GET"">'
		self._form_close = '</form>'
		self.__inputs = []
		self._form_inputs = ''
		#<label>First Name:  </label><input type = "text" value = "" name = "first_name" placeholder = "First Name" /> 
		#['first_name', 'text', 'First Name']
		#<label>Last Name:  <input type = "text" value = "" name = "last_name" placeholder = "Last Name/>
		#<input type = "submit" value = "Submit" />

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
				
			'''	An alternative to the above is the try and except method			
			try:
				self._form_inputs += '" placeholder = "' + item[2] + '" />'
			#otherwise.. end the tag 
			except:
				self._form_inputs += '" />'
				'''
		print self._form_inputs

	#POLYMORPHISM ALERT!!!!! -----METHOD OVERRIDING  | SAME AS ABOVE, THIS IS LAST SO OVERRIDES THE ABOVE
	def print_out(self):
		return self._head + self._body + self._form_open  + self._form_inputs + self._form_close + self._close



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
