from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_home_function():
    return render_template('./index.html')

@app.route('/index.html')
def my_home_back_function():
    return render_template('./index.html')

@app.route('/about.html')
def about():
    return render_template('./about.html')

@app.route('/works.html')
def work():
    return render_template('./works.html')

@app.route('/contact.html')
def contact():
    return render_template('./contact.html')

@app.route('/components.html')
def components():
    return render_template('./components.html')