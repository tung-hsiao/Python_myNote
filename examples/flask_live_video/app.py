from flask import Flask,render_template,Response,request
import live

app = Flask(__name__)

@app.route('/video_feed')
def video_feed():
     return Response(live.gen_surveillance(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()