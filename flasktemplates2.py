from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello"

@app.route("/hello/<user>")
def hello_name(user):
	return render_template("hello.html", user = user)

@app.route("/welcome/<name>")
def welcome_name(name):
	return render_template("welcome.html", name = name, gg = "gg")

@app.route("/scorepage/<int:score>")
def score_result(score):
	return render_template("score.html", marks = score)

@app.route("/result")
def result():
	dict = {"phy":60, "che":60, "maths":70}
	return render_template("resultexam.html", results = dict)

if __name__ == "__main__":
	app.run(debug=True, port = 5151)