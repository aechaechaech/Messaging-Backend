from flask import Flask, request
from flask_socketio import SocketIO, emit
import pymongo, json

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

@app.route('/api/send_msg', methods = ["POST"])
def recv_msg_from_client():
    # TODO: error handling, sanitization, different channels through different socket rooms
    post_data = request.data.decode("utf-8")
    post_data = json.loads(post_data)
    
    channel = post_data['channel']
    user_msg = post_data['text']
    socketio.send(user_msg)
    
    return {"status": True}

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=25565)
