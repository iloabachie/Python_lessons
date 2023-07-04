from flask import Flask, render_template, request
import random
import datetime
import requests

app = Flask(__name__)

year = datetime.date.today().year

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", year=year, e=e), 404

# Internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", year=year, e=e), 500

@app.route('/')
@app.route('/home')
def home_page():
    randomnum = random.randint(1, 15)    
    return render_template("index.html", num=randomnum, year=year)

@app.route('/guess/<name>')
def guess_page(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    data = response.json()
    print(type(data), data)
    gender = data['gender']
    probability = data['probability']
    response = requests.get(f"https://api.agify.io?name={name}")
    response.raise_for_status()
    data = response.json()
    age = data['age']    
    # name = name.capitalize() #this can also be done int eh Jinja syntax in the html file    
    print(name, gender, age, probability, year)
    return render_template("guess.html", year=year, name=name, gender=gender, age=age, probability=probability)

@app.route('/processed_form', methods=['POST'])
def guess_form(): 
    name = request.form.get('name')  # can use this or the method below to tap into the form data that is dictionary like
    name = request.form['name']
    print(1111111111, type(request.form), request.form)
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
    # response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response = requests.get("https://api.npoint.io/88838b326e7274d04e53")    
    response.raise_for_status()
    data = response.json() 
    # print(type(data), data)
    return render_template("blog.html", year=year, allposts=data)

@app.route('/blog/<int:num>')
def blog_display(num):    
    # response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response = requests.get("https://api.npoint.io/88838b326e7274d04e53")
    response.raise_for_status()
    data = response.json() 
    return render_template("blogdisplay.html", year=year, allposts=data, num=num)

if __name__ == "__main__":
    app.run(debug=True)
