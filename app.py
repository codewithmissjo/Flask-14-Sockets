from os import environ
from flask import Flask, render_template#, request, redirect, session
from flask_socketio import SocketIO, emit

socketio = SocketIO()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketop.init(app)

@app.route('/')
def index():
  return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
  emit('my connection', {'data': 'Connected'})

@socketio.on('my new message', namespace='/test')
def test_message(message):
  emit('new message', {'data': message['data']})

if __name__ == '__main__':
  socketio.run(app)
