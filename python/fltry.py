from flask import Flask, redirect, url_for
app=Flask(__name__)

@app.route('/flask')
def hello_flask():
	return 'hi flask'

@app.route('/python/')
def hello_python():
	return 'hi python' 

@app.route('/admin')
def admin():
	return 'hello admin'

@app.route('/guest/<guest>')
def guest(guest):
	return 'hello %s as guest' %guest

@app.route('/user/<name>')
def user(name):
	if name == 'admin':
		return redirect(url_for('admin'))
	else:
		return redirect(url_for('guest',guest = name))




if __name__ == '__main__':
	app.run(debug = True)




