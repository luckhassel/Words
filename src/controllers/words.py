from flask import Blueprint, jsonify, request, abort
from container import Container

words_controller = Blueprint('words_controller', __name__)
container = Container()

@words_controller.before_request
def only_json():
    if not request.is_json and request.method == "POST": 
        abort(415)

@words_controller.route('/', methods=["GET"])
def words_health_check():
    return 'healthy'

@words_controller.route('/vowel_count', methods=["POST"])
def vowel_count():
    try:
        content = request.json
        use_case = container.words_vowel_count_use_case(content['words'])
        return jsonify(use_case.vowel_count())
    except KeyError:
        abort(400)
    except:
        abort(422)
    
@words_controller.route('/sort', methods=["POST"])
def sort():
    try:
        content = request.json
        use_case = container.words_sort_use_case(content['words'], content['order'])
        return jsonify(use_case.sort())
    except KeyError:
        abort(400)
    except:
        abort(422)
