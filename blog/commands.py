from blog.app import db
from wsgi import app

@app.cli.commands('init-db')
def init_db():
    db.create_all()