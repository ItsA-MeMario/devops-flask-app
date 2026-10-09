from flask import Flask
app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>This ia another string!<br>I am a Flask app!</p><p><a href="/contact">Contact</a></p><p><a href="/about">About</a></p>'

@app.route('/contact')
def contact():
	return '<p>Email: C24711569@mytudublin.ie <br>My phone number: 083XXXXXXX</p>'

@app.route('/about')
def about():
	return '<p>My name is Mario</p>'

