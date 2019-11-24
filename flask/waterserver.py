from flask import Flask, render_template, request, url_for, redirect
app=Flask(__name__)

@app.route('/water/')
def water():
	return render_template('water.html') 


@app.route('/waterform', methods=['GET', 'POST'])
def waterform():
	return render_template('waterform.html')


if __name__ == '__main__':
	app.run(debug = True)