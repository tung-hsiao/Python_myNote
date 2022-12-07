from flask_socketio import SocketIO, emit, join_room
from flask import Flask, render_template, Response,request

app = Flask(__name__)
socketio = SocketIO(app)
room_id = ""

# When web opened, this function will be called (checkout app.js)
@socketio.event
def login(msg):
    print(msg)
    room_id = msg['login_id']
    join_room(room_id)
    print('login success!')

@app.route('/')
def index():
    msg_list = [1,2,3,4,5]
    return render_template('index.html',msg_list=msg_list)

if __name__ == '__main__':
    socketio.run(app)