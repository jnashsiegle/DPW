
import webapp2
from pages import Page #from pages.py import the page class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "My page!"
        p.css = "css/style.css"
        p.body = "Miss Piggy likes Kermit de Frog" #this will replace the body text below in self.body
        #print p.print_out()#this will print out in the google engine console
        #self.response.write(p.print_out())# this will print out in browser (removed for getter/setter example)
       # p.update() #replacing the above #self.response......
        #let's remove p.update() from here and add to main.py to have it auto update whenever data changes; it won't be p.update it will be self.update over there
        self.response.write(p.whole_page)







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
