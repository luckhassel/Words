from flask import Blueprint

words_controller = Blueprint('word', __name__)

@words_controller.route('/', methods=["GET"])
def words_health_check():
    return 'healthy'

@words_controller.route('/vowel_count', methods=["POST"])
def vowel_count():
    return 'vowel count'

@words_controller.route('/sort', methods=["POST"])
def sort():
    return 'sort'
