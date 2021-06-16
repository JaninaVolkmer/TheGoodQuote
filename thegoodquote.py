from app import app, db
from app.models import User, Post, Todo, Notification, Message

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Todo': Todo, 'Message': Message,
            'Notification': Notification}