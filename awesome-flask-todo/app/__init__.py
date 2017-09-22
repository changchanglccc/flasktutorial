#initialize app pkg

from flask import Flask

app = Flask(__name__)       # initialize application of Flask in app pkg
app.config.from_object("config")

from app import views, models