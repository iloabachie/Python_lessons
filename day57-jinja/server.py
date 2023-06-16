from flask import Flask, render_template, request
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    randomnum = random.randint(1, 15)
    year = datetime.date.today().year
    return render_template("index.html", num=randomnum, year=year)

@app.route('/guess/<name>')
def guess_page(name):
    year = datetime.date.today().year
    response = requests.get(f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    data = response.json()
    gender = data['gender']
    probability = data['probability']
    response = requests.get(f"https://api.agify.io?name={name}")
    response.raise_for_status()
    data = response.json()
    age = data['age']    
    # name = name.capitalize() #this can also be done int eh Jinja syntax in the html file    
    print(name, gender, age, probability, year)
    return render_template("guess.html", year=year, name=name, gender=gender, age=age, probability=probability)


@app.route(f'/processed_form', methods=['POST'])
def guess_form(): 
    name = request.form.get('name')  
    year = datetime.date.today().year
    response = requests.get(f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    data = response.json()
    gender = data['gender']
    probability = data['probability']
    response = requests.get(f"https://api.agify.io?name={name}")
    response.raise_for_status()
    data = response.json()
    age = data['age']    
    return render_template("guess.html", year=year, name=name, gender=gender, age=age, probability=probability)

@app.route('/blog')
def blog_page():    
    year = datetime.date.today().year
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    data = response.json() 
    return render_template("blog.html", year=year, allposts=data)

@app.route('/blog/<int:num>')
def blog_display(num):    
    year = datetime.date.today().year
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    data = response.json() 
    return render_template("blogdisplay.html", year=year, allposts=data, num=num)

if __name__ == "__main__":
    app.run(debug=True)
