from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase 
from product import Producto  

app= Flask(__name__)
db= dbase.dbConection() 

@app.route('/')
def home():
    return render_template('index.html')