# import firebase_admin
# from firebase_admin import db
# import numpy as np
# from PIL import Image
# import math
from flask import Flask
import os

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))

def get(rule: str, **options: Any) -> ((T_route@get) -> T_route@get):
    
    

# cred_obj = firebase_admin.credentials.Certificate('./firebaseProducts/ai-fashion-e0677-firebase-adminsdk-amrf3-700c61a65c.json')
# app_database = firebase_admin.initialize_app(
# 	cred_obj, 
# 	{'databaseURL':"https://ai-fashion-e0677-default-rtdb.firebaseio.com/"})

# Vec_dist = math.sqrt(np.sum((numpyIm-X_numpy[i])**2))


