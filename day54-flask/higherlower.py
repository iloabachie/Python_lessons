from flask import Flask
from random import randint

app = Flask(__name__)

target = randint(0, 10)


# investigate why wrapper function fails
def make_bold(funct):
    def wrapper(_):
        print("i ran")
        text = funct(_)
        return f"<b>{text}</b>"       
    return wrapper


@app.route('/')
def index():
    return '<h2>Choose a number between 0 and 9</h2>\
        <img src="https://media1.giphy.com/media/xUn3CftPBajoflzROU/giphy.gif?cid=ecf05e47yszv2qzl2hr9paw27vgmor4t3jiqfdefrzu1sqjh&ep=v1_gifs_search&rid=giphy.gif&ct=g", width=200>'


@app.route('/user/<int:number>')
@make_bold
def num_input(number):
    if number > target:
        return "Too high, try again"
    elif number < target:
        return "Too low, try again"
    else:
        return "Congrats you are a genius"
 


if __name__ == '__main__':
    app.run(debug=True)
    