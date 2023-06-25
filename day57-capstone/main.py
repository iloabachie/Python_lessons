from flask import Flask, render_template
import requests
import datetime

response = requests.get("https://api.npoint.io/88838b326e7274d04e53")
response.raise_for_status()
blog_data = response.json()

year = datetime.date.today().year

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template("index.html", blog_data=blog_data, year=year)

@app.route('/article/<int:id>')
def read_article(id):  
    length = len(blog_data)  
    return render_template("post.html", blog_data=blog_data, id=id, year=year, length=length)

if __name__ == "__main__":
    app.run(debug=True)
