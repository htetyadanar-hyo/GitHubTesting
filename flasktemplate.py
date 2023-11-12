from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello(user):
	return render_template('hello.html',user=user,name='ggg')

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug = True,port = 5252)