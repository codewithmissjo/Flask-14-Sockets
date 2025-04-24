from os import environ
from flask import Flask, render_template#, request, redirect, session
from flask_socketio import SocketIO, emit

appFlask = Flask(__name__)
appFlask.config['SECRET_KEY'] = 'secret!'
app = SocketIO(appFlask)

@app.route('/')
def index():
  return render_template('index.html')

@app.on('connect', namespace='/test')
def test_connect():
  emit('my connection', {'data': 'Connected'})

@app.on('my new message', namespace='/test')
def test_message(message):
  emit('new message', {'data': message['data']})

if __name__ == '__main__':
  HOST = environ.get('SERVER_HOST', 'localhost')
  PORT = int(environ.get('SERVER_PORT', '5000'))
  app.run(app, host=HOST, port=PORT)
