from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


home = Blueprint('home',__name__)

@home.route('/')
def hello_world():
    return 'Hello, World!'