from flask import Blueprint, render_template

test = Blueprint('test', __name__)

@test.route('/')
def index():
    return "Testing!!"

# @main.route('/test')
# def home():
#     return "Mass Home!!"
