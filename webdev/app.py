from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db = SQLAlchemy(app)

# upload folder 
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

# Signup 
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='pbkdf2:sha256')
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

# Login 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('gallery'))
        else:
            flash('Login failed. Check your credentials.', 'danger')
    return render_template('login.html')

# Gallery 
@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Handle image upload
        if 'image' in request.files:
            image = request.files['image']
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)
            flash('Image uploaded successfully!', 'success')
    
    # Display images from the upload folder
    uploaded_images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', images=uploaded_images)

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully!', 'info')
    return redirect(url_for('login'))

# Default Root
@app.route('/')
def home():
    return redirect(url_for('signup'))  # Redirect to the signup page

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
