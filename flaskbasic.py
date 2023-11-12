from flask import Flask
app = Flask(__name__) #Object


#Flask Routing - route() decorator in Flask is used to bind URL to
@app.route('/')
def greeting():
	return "Hello"

@app.route('/welcome/')
def welcome():
	return "Welcome"

if __name__ == '__main__':
	app.run(port=5555,debug=true)