from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test/', methods = ['POST', 'GET'])
def test():
    print(request.get_json()['msg'])

    response = {'status':'200'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)