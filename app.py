from flask import Flask, render_template, request, url_for, redirect
from peewee import *
from model import *

db=MySQLDatabase('conf',user='root', passwd='***')

app=Flask(__name__)


@app.before_request
def before_request():
	db.connect()

@app.teardown_request
def after_request(exception):
	db.close()



@app.route('/')
def index():
	return render_template('home.html', confessions=Confession.select().order_by(Confession.post_date.desc()))

@app.route('/post_new/')
def post_new_function():
	return render_template('new_conf.html')

@app.route('/create', methods=['POST'])
def create():
	Confession.create(
		text=request.form['confession_text']
		)
	return redirect(url_for('index'))

if __name__=='__main__':
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(debug=True)




