'''Flask api init module'''

from flask import Flask
from controllers.words import words_controller

app = Flask(__name__)
app.register_blueprint(words_controller)
app.json.sort_keys = False

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
