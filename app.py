from flask import Flask, request

app = Flask(__name__)

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
    stores.append(new_store) #append new store to the list
    return new_store, 201 #return the store and status code