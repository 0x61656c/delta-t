#################################################################################
#IMPORTS
#################################################################################
from api_sim import *
import os
import hashlib
from flask import Flask, request, redirect, render_template

#################################################################################
#GLOBALS
#################################################################################

app = Flask(__name__)
#Initiate Flask Server

"""
#Routing + Controllers
"""

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/cells')
def cells():
    return render_template("cells.html")

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
