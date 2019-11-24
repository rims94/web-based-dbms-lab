from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def serve_index():
    return render_template("index.html")
@app.route('/hello')
def serve_hello():
    return "hello world"
@app.route('/post/<post_id>')
def serve_post(post_id):
    return render_template('post.html', id = post_id)
@app.route('/login')
def serve_login():
    return render_template('login.html')
@app.route('/auth', methods= ['POST'])
def login_check():
    username = request.form['username']
    password = request.form['password']
    if username == 'rims94' and password == 'rimo1234@':
        return render_template('auth.html', action = True)
    else:
        return render_template('auth.html', action = False)
if __name__ == '__main__':
    app.run(port = 8090, debug =True)
