from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/test1'
db = SQLAlchemy(app)

@app.route('/')

def index():
    return 'hello world!!'