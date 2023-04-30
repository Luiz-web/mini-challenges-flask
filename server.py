from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

genderize_response = requests.get("https://api.genderize.io/?name=luiz")
agify_response = requests.get("https://api.agify.io")

genderize_response
# genderize_data = genderize_request.text

@app.route('/guess/<name>')
def show_statistic(name):
    param = {
        "name": name
    }
    genderize_response = requests.get(url="https://api.genderize.io/", params=param)
    agify_response = requests.get("https://api.agify.io", params=param)

    genderize_data = genderize_response.json()
    agify_data = agify_response.json()

    user_name = genderize_data["name"].capitalize()
    gender = genderize_data["gender"]
    age = agify_data["age"]

    return render_template("index.html", user_name=user_name, age=age, gender=gender)

@app.route("/blogs")
def show_posts():
    response = requests.get("https://api.npoint.io/d6a80c7d0fbbabdc0f2d")
    posts = response.json()
    return render_template("blogs.html", posts=posts)
    
@app.route('/')
def hello_world():
    current_year = datetime.datetime.today().year
    return render_template("home.html", current_year=current_year)

