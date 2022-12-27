import requests,json


def push_message(payload):

    headers = {"content-type": "application/json", 
               "Accept":       "application/json" }
    url ="http://127.0.0.1:5000/test/"
    requests.post(url, data=json.dumps(payload), headers=headers)

if __name__ == "__main__":
    payload = {"msg": "123"}
    push_message(payload)