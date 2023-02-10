"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route('/')
def homepage():
    return redirect('/users')


@app.route('/users')
def show_users():
    users = User.query.all()
    return render_template('user.html', users=users)


@app.route('/users/new')
def new_user():


@app.route('/users/new', methods=['POST'])
def add_user():


@app.route('/users/<int:user_id>')
def show_user(user_id):


@app.route('/users/<int:user_id>/edit')
def show_edit(user_id):


@app.route('/users/<int:user_id>/edit' methods=['POST'])
def do_edit(user_id):


@app.route('/users/<int:user_id>/delete' methods=['POST'])
def delete_user():
