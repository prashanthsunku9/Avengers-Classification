from flask import Flask, request, jsonify
import util
import cv2
from flask_cors import CORS, cross_origin

app=Flask(__name__)
cors = CORS(app)
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/') 
@cross_origin()
def f():
    return jsonify("helloss")

@app.route('/hello1',methods=['POST']) 
@cross_origin()
def hello1():
    print("first")
    util.load_saved_artifacts()
    print("sdf")
    a=request.json.get('data')
    a="data:image/jpeg;base64,"+a
    print("sds")
    return jsonify(util.classify_image(a))
    # return jsonify("sf")

if(__name__ ) == "__main__":
    app.run(port=5000)
