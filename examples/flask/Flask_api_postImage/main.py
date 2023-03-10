from flask import Flask,jsonify,request
import cv2
import base64
import numpy as np

app = Flask(__name__)

def bts_to_img(bts):
    buff = np.frombuffer(bts, np.uint8)
    buff = buff.reshape(1, -1)
    img = cv2.imdecode(buff, cv2.IMREAD_COLOR)
    return img

@app.route('/testAPI/', methods=['GET','POST'])
def post():
    img_b64 = request.json['img']                         # base64 encoded string
    img_bytes = base64.b64decode(img_b64.encode('utf-8')) # convert str to bytes
    img = bts_to_img(img_bytes)

    rtn = {"message" : "200"}
    return jsonify(rtn)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)