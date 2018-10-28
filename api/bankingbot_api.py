import os
import uuid
import json
import sys
import requests

current_dir = os.path.dirname(os.path.realpath(__file__))
target_dir = os.path.sep.join(current_dir.split(os.path.sep)[:-1])
sys.path.insert(0,target_dir)

from flask import Flask, render_template, request, redirect, jsonify
from common.fbmq import Page, Template, Attachment, Payload, QuickReply, NotificationType
from config import CASA_LINK,FACEBOOK_TOKEN, VERIFY_TOKEN

print FACEBOOK_TOKEN
app = Flask(__name__)
page = Page(FACEBOOK_TOKEN)
data = None

@app.route('/about')
def about():
    return 'PhilipBank Team'

@app.route('/contact')
def contact():
    return ''

@app.route('/', methods = ['GET', 'POST'])
def index():
	return ''

@app.route('/webhook', methods=['GET'])
def validate():
    """
    validate webhook
    """
    if request.args.get('hub.mode', '') == 'subscribe' and \
					request.args.get('hub.verify_token', '') == VERIFY_TOKEN:

		print("Validating webhook")

		return request.args.get('hub.challenge', '')
    else:
		return 'Failed validation. Make sure the validation tokens match.'

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Handling webhook every transaction
    """
    data = request.get_json()
    print "DATA: ",data
    page.handle_webhook(request.get_data(as_text=True)) 
    return "ok", 200

@app.route('/login/authorize', methods=['GET'])
def getLogin():
	"""
	Account Linking Token is never used in this demo, however it is
	useful to know about this token in the context of account linking.
	It can be used in a query to the Graph API to get Facebook details
	for a user. Read More at:
	https://developers.facebook.com/docs/messenger-platform/account-linking	
	"""

	redirect_uri = request.args.get('redirect_uri')
	account_linking_token = request.args.get('account_linking_token')
	
	return render_template('login.html', 
                error='', 
                redirect_uri=redirect_uri, 
                account_linking_token=account_linking_token)

@app.route('/login/authorize', methods=['POST'])
def postLogin():
	"""
	Account Linking Token is never used in this demo, however it is
	useful to know about this token in the context of account linking.
	It can be used in a query to the Graph API to get Facebook details
	for a user. Read More at:
	https://developers.facebook.com/docs/messenger-platform/account-linking	
	"""

	redirectURI = None
	linkToken = None
	error = None

	if request.method == 'POST':
		if request.form['submit'] == "btn_login":
			username = request.form.get('username')
			password = request.form.get('password')
			redirectURI = request.form.get('redirectURI')
			linkToken = request.form.get('linkToken')
			
			if username == "admin" and password == "admin":
				return redirect('{0}&authorization_code={1}'.format(redirectURI, uuid.uuid1().hex))
			else:
				error = "username or password incorrect!"
	return render_template('login.html', 
                error=error, 
                redirect_uri=redirectURI, 
                account_linking_token=linkToken)

@page.handle_message
def handle_message(event):
	pass

@page.after_send
def after_send(payload, response):
	print "RESPONSE: ", response.json()

"""
Facebook Messenger Threading Setup
"""
import threading_setup

"""
main application to start up
running port 5101 for serve API point to Facebook Graph APIs
"""
if __name__ == '__main__':
	HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
	PORT = 5101
	try:
	    PORT = int(os.environ.get('SERVER_PORT', 5101))
	except ValueError:
		PORT = 5101

	app.debug = False
	app.run(HOST, PORT)