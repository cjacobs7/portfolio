'''
This is a Flask, App Engine, Bootstrap, JS portfolio. Check out my other projects!

Flask renders our pages from the static folder. They only dynamically generated page is 
display.ejs where we pass our calculated results in with a little formatting. I used ejs 
because I thought at the onset of the project that flask might need to pass variables and ejs
is what I'm familiar with from working with Node.


@author Christopher Jacobs
@updated 12/12/17


'''

from __future__ import print_function, division

import traceback, sys, random

from flask import Flask, render_template, request, redirect

from google.appengine.ext import ndb

app = Flask(__name__)

    
@app.route('/', methods = ("GET", "POST"))
def landing():
    return render_template("landing.ejs")

@app.route('/java', methods = ("GET", "POST"))
def java():
    return render_template("java.ejs")

@app.route('/bitquery', methods = ("GET", "POST"))
def bitquery():
    return render_template("bitquery.ejs")

@app.route('/webapp', methods = ("GET", "POST"))
def webapp():
    return render_template("webapp.ejs")

@app.route('/site', methods = ("GET", "POST"))
def site():
    return render_template("site.ejs")
    
        
#static about page
@app.route('/about')
def about():
    return render_template("about.ejs")
#static contact page
@app.route('/contact')
def contact():
    return render_template("contact.ejs")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.ejs'), 404

@app.errorhandler(500)
def server_error(e):
    print (traceback.format_exc())
    return traceback.format_exc(), 500, {'Content-Type': 'text/plain charset=utf-8'}