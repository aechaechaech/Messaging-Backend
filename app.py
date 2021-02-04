from flask import Flask, request
from flask_socketio import SocketIO, emit
import pymongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

# connect to db
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["msg_db"]
sus_collection = db["msgs"]


# flask routing
@app.route('/api/get_channels')
def get_channels():
    # TODO: get this from db, needs cookie and maybe uuid? 
    channels = ["test1", "test2"]
    return_data = {"channels": channels}

    return return_data

@app.route('/api/')
def recv_msg_from_client():
    # needs uuid, channel
    
    return "H"

# SOCKET.IO TESTING
# # socket io events
# @socketio.on('message')
# def handle_message(data):
#     print('received message: ' + data)
#     socketio.send(data)

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=25565)
