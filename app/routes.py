from flask import Blueprint, request, jsonify
from app.services import TodoService

todo_bp = Blueprint('todos', __name__)

@todo_bp.route('/todos', methods=['GET'])
def get_todos():
    todos = TodoService.get_all_todos()
    return jsonify(todos)

@todo_bp.route('/', methods=['GET'])
def get_home():
    todos = TodoService.get_home()
    return jsonify(todos)

@todo_bp.route('/health', methods=['GET'])
def get_health():
    todos = TodoService.get_health()
    return jsonify(todos)
