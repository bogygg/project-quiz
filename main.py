from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result")
def result():
    user_answer = request.args.get("answer")
    return render_template("result.html", user_answer= user_answer)

app.run(debug=True)