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

@socketio.event
def get_msg_fromPython():
    list_to_JS = [{'key':'U001', 'value':'X Tung'},
                  {'key':'U002', 'value':'Hsiao Tung'}]
    socketio.emit('show_msg', list_to_JS, to=room_id)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)