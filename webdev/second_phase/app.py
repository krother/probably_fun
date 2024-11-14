from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import os
import uuid


app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', uuid.uuid4().hex)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/landing')
def landing():
    return render_template('landing_screen.html')

@app.route('/random_generator')
def random_generator():
    return render_template('randomgenerator.html')


@app.route('/proceed_signup', methods=['POST'])
def proceed_signup():
    username = request.form['username']
    password = request.form['password']
    
    user = User.query.filter_by(username=username).first()
    if user:
        flash('Username is already taken. Please choose another one', 'error')
        return redirect(url_for('signup'))
    
    new_user = User(username=username, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    
    flash('Signup successful! Please log in.', 'signup_success')
    return redirect(url_for('login'))


@app.route('/proceed_login', methods=['POST'])
def proceed_login():
    username = request.form['username']
    entered_password = request.form['password']
    
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, entered_password):
        flash('Login successful!', 'login_success')
        return redirect(url_for('landing'))  
    else:
        flash('Invalid username or password. Please try again!!', 'error')
        return redirect(url_for('login'))


uploaded_images = []  

@app.route('/upload_images', methods=['POST'])
def upload_images():
    # Your upload handling logic
    return jsonify({"success": True})



if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
