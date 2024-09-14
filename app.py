from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    print(f"Username: {username}")
    print(f"Password: {password}")
    
    return 'Login data received!'

if __name__ == '__main__':
    app.run(debug=True)
