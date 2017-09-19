from flask import Blueprint, jsonify
from flask import request
from controller import *

auto_complete = Blueprint('auto_complete_api', __name__)

@auto_complete.route('/complete/<complete_text>', methods=['GET'])
def get_auto_complete_results(complete_text):
    return jsonify(autoComplete(complete_text))
