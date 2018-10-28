import requests
import sys
import os 
import json
import uuid

from datetime import timedelta
from werkzeug.exceptions import HTTPException
from flask import Flask, request, render_template, redirect, url_for, Blueprint, jsonify, session

from config import FACEBOOK_TOKEN,VERIFY_TOKEN, SECRET_KEY,CASA_LINK	
from flask_babel import Babel, refresh

app = Flask(__name__)
errors = Blueprint('errors', __name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.permanent_session_lifetime = timedelta(minutes=10)

babel = Babel(app)
ctx = app.app_context()
ctx.push()

@babel.localeselector
def get_locale():
	if 'language' in request.cookies:
		return request.cookies.get('language')
	else:
		return 'km'

@babel.timezoneselector
def get_timezone():
	return 'UTC'

@app.route('/language/<code>')
def language(code):
	session['language'] = code
	refresh()
	return redirect(url_for('admin.HomeView:home'))


@app.errorhandler(404)
def page_not_found(e):
	return render_template('/error/404.html'), 404

@errors.app_errorhandler(Exception)
def handle_error(error):
	message = [str(x) for x in error.args]
	status_code = error.status_code
	success = False
	response = {
		'success': success,
		'error': {
			'type': error.__class__.__name__,
			'message': message
		}
	}

	return jsonify(response), status_code

import register_blueprint

@app.route('/')
def index():
	return redirect(url_for('admin.HomeView:index'))


ctx.pop()