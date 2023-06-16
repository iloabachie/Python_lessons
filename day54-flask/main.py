from flask import Flask

app = Flask(__name__)

def make_bold(funct):
    def wrapper(*args):
        text = funct(*args)
        return "<b>" + text + "</b>"       
    return wrapper

def make_italics(funct):
    def wrapper(*args):
        text = funct(*args)
        return "<em>" + text + "</em>"       
    return wrapper

def make_underline(funct):
    def wrapper(*args):
        text = funct(*args)
        return f"<u>{text}</u>"       
    return wrapper

@app.route('/')
@make_bold
@make_italics
@make_underline
def index():
    return 'Index Pagessssssssss'

@app.route('/hello')
def hello():
    return '<h2>Hello, World</h2>\
        <p>lorem ipsum this is another line here we go</p>'


@app.route("/username/<name>")
def greet(name):
    return f"hello {name}"

from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


if __name__ == '__main__':
    app.run(debug=True)