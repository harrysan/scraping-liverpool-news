# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 22:17:56 2021

@author: Harry
"""

#!flask/bin/python
from flask import Flask, render_template
from bolanet import output 
from detikcom import output1 
from okezone import output2 
import json

vdetikcom = {}
vkompas = {}

app = Flask(__name__)

@app.route('/')
def index():
    #return "Hello, World!"
    #vbolanet = scrapbola()
    
    json_data = json.loads(output)
    #return json_data;
    return render_template('index.html',data=json_data)

@app.route('/bolanet')
def bolanet():
    #return "Hello, World!"
    #vbolanet = scrapbola()
    
    json_data = json.loads(output)
    #return json_data;
    return render_template('bolanet.html',data=json_data)

@app.route('/detikcom')
def detikcom():
    #return "Hello, World!"
    #vbolanet = scrapbola()
    
    json_data = json.loads(output1)
    #return json_data;
    return render_template('detikcom.html',data=json_data)

@app.route('/okezone')
def okezone():
    #return "Hello, World!"
    #vbolanet = scrapbola()
    
    json_data = json.loads(output2)
    #return json_data;
    return render_template('okezone.html',data=json_data)

"""
@app.route('/bolanet', methods=['GET'])
def scrapbola():
    return output
    
@app.route('/detikcom', methods=['GET'])
def scrapbola1():
    return output1

@app.route('/kompas', methods=['GET'])
def scrapbola2():
    return output2
"""

if __name__ == '__main__':
    app.run(debug=True)