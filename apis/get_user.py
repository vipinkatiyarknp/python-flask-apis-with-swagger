from flask_app import app
from flask import jsonify, request

@app.route('/api/get_user/<id>', methods=['GET'])
def get_user(id=None):
    print("dfdfdf",id)
    results = {
        "id": id,
        "name":"vipin",
        "class": "12"
    }
    return jsonify(results)

