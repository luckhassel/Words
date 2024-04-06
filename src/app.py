from flask import Flask
from controllers.words import words_controller
   
app = Flask(__name__)
app.register_blueprint(words_controller)