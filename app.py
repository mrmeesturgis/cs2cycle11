from flask import Flask, request, jsonify, json, render_template
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO
from matplotlib.figure import Figure
from database import *

app = Flask(__name__)

@app.route('/')
def doc():
	return render_template('home.html')

@app.route('/images')
def tester():
	return render_template('images.html')

@app.route('/bootstrapper')
def index():
	return render_template('bootstrapper.html')


@app.route('/graph')
def graph():
	return render_template('graph.html')

@app.route('/database')
def database():
	mydb = db()
	mydb.builddb('dbinit.sql')
	mydb.checkdb()
	result = mydb.checktable('*', 'car')
	print(result)
	return render_template('database.html', tables=[result.to_html(classes='data')], titles=result.columns.values)

@app.route('/poster')
def poster():
	return render_template('poster.html')

if __name__ == "__main__":
	app.run(port=5000, debug = True)
