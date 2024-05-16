from flask import Blueprint, render_template

test = Blueprint('test', __name__)

@test.route('/')
def Login():
    return render_template("Login.html")

# @main.route('/test')
# def home():
#     return "Mass Home!!"
