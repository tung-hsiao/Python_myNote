import requests,json
import cv2
import base64


def push_message(payload):
    headers = {"content-type": "application/json", 
               "Accept":       "application/json" }
    url ="http://127.0.0.1:8080/testAPI/"
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        print(response.text)
    else:
        print(response.status_code)

if __name__ == "__main__":
    payload = {"msg": "123"}

    img = cv2.imread('dog.jpg')
    img_bytes = cv2.imencode('.jpg', img)[1].tobytes()    # class 'bytes'
    img_b64 = base64.b64encode(img_bytes).decode("utf8")  # class 'str'
    payload['img'] = img_b64

    response = push_message(payload)