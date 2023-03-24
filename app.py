from flask import Flask,render_template,flash,redirect,url_for,session,request,logging
from sqlhelpers import *

app=Flask(__name__)

@app.route('/register')
def register():
    return render_template('register.html')
@app.route("/")
def index():
    return render_template('index.html')

if __name__ =='__main__':
   app.run(debug=True)