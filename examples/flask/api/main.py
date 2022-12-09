from flask import Flask, request

app = Flask(__name__)

@app.route('/testAPI/', methods=['GET','POST'])
def post():
    msg = request.get_json().get('msg')
    print('msg',msg)

    return '200'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)