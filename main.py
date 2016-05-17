#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import users
from google.appengine.ext import ndb
import webapp2



Default_Note_name='default_note'

def note_key(note_name=Default_Note_name):
    return ndb.Key('Notes', note_name)



class Text(ndb.Model):
	author=ndb.UserProperty()
	content=ndb.TextProperty()
	date=ndb.DateTimeProperty(auto_now_add=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        note_name=self.request.get('note_name', Default_Note_name)
        texts_query=Text.query(
            ancestor=note_key(note_name)).order(-Text.date)
        texts=texts_query.fetch(15)
    	user=users.get_current_user()
    	if user:
            self.response.write(' Not %s?</div> <a href=%s>sign out</a>' % \
                (user.nickname(), users.create_logout_url(self.request.uri)
            ))

    	else:
    		self.redirect(users.create_login_url(self.request.uri))
   		return 

        self.response.write('<h1>Announcements Board</h1>')
        self.response.write('<h3>Welcome %s !</h3>'% (user.nickname()))
        self.response.write('''<head>
        	<link type="text/css" rel="stylesheet" href="/stylesheets/main.css" />
        	<body>
            <center><hr>
            <form action=/Notes method=post>
            <textarea name=content rows=4 cols=50 placeholder="Enter your announcement here....." autofocus></textarea>
            <br><input type=submit value="Submit">
            </form></center>
            </body>
            </head>
        ''')
        self.response.write('<h2>Announcements</h2>')
        for text in texts:
        	if text.content:
        		self.response.write('<li>(%s):' % text.author)
        		self.response.write('%s' % text.content)
        self.response.write('<meta http-equiv="refresh" content="25" >')
        
class Notes(webapp2.RequestHandler):
    def post(self):
    	note_name=self.request.get('note_name',Default_Note_name)
    	text=Text(parent=note_key(note_name))
    	users.get_current_user()
    	text.author=users.get_current_user()
    	text.content=self.request.get('content')
    	text.put()
    	query_params={'note_name':note_name}
    	self.redirect('/')
        

app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/Notes',Notes)
], debug=True)