from flask import Flask, jsonify, request

app = Flask(__name__)

# Global todos list
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# GET /todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# POST /todos
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

# DELETE /todos/<position>
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    # Remove the item at the given position
    if 0 <= position < len(todos):
        todos.pop(position)
    else:
        return jsonify({ "error": "Invalid position" }), 400

    return jsonify(todos)

# Bottom of file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
