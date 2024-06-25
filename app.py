import os

from flask import Flask, request
from flask import render_template
from flask import jsonify

from distutils.log import debug 
from fileinput import filename 
from flask import *  


app = Flask(__name__)

@app.route('/')   
def main():   
    return render_template("index.html")  


@app.route('/upload', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        print(request.files['file'])
        f = request.files['file'] 
        f.save(os.path.join("static/uploads", f.filename))

        path_name = os.path.join("static/uploads", f.filename)

        print(path_name)
       
        return render_template("result.html", name = f.filename)  


# EXAMPLE CODE ==========================
stores = [
    {
    "name": "Ekaabo Cosmetics",
    "items":[
    {"name" : "lip gel",
     "price" : 20.36
     },
    {"name" : "moisturizer",
     "price" : 38.90
     }, 
     {"name" : "hair wigs",
      "price" : 50.89
      },
      {"name" : "Body Cream",
       "price": 12.46}]
    }
    ]

# METHOD GET DATA

@app.get("/store")
def get_stores():
    return {"stores" : stores}

# METHOD POST DATA

@app.post("/store")
def post_store():
    request_data = request.get_json() # you need to import json
    new_store = {
        "name": request_data["name"], 
        "items":[]
        }
    image = stores.append(new_store) #append new store to the list
    return new_store, 201 #return the store and status code


if __name__ == '__main__':
    app.run()