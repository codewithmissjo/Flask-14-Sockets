<<<<<<< HEAD
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# create socket obj AFTER flask obj, this plus the other changes = :)
socketio = SocketIO(app)
=======
from flask import Flask, render_template#, request, redirect, session
from flask_socketio import SocketIO, emit

socketio = SocketIO()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio.init_app(app)
>>>>>>> 1da36911b8efd1c4be9c0a54fca749619b5f4a31

@app.route('/')
def index():
  return render_template('index.html')

<<<<<<< HEAD
@socketio.on("form_submitted", namespace="/test")
def get_message_from_form(msg):
  #print(msg['data'])
  emit("a_new_message", { "data": msg['data'] })

if __name__ == '__main__':
  socketio.run(app)
=======
@socketio.on('connect', namespace='/test')
def test_connect():
  emit('my connection', {'data': 'Connected'})

@socketio.on('my new message', namespace='/test')
def test_message(message):
  emit('new message', {'data': message['data']})

if __name__ == '__main__':
  socketio.run(app)
>>>>>>> 1da36911b8efd1c4be9c0a54fca749619b5f4a31
