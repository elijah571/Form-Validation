from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for session management

# In-memory database to store users
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']

    if username in users:
        flash('Username already exists. Please choose another one.', 'danger')
    else:
        users[username] = generate_password_hash(password)
        flash('Signup successful!', 'success')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
