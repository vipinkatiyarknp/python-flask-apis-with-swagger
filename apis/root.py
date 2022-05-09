from flask_app import app
from flask import jsonify, request, render_template

@app.route('/', methods=['GET'])
def home():
    message = 'Flask is UP and RUNNING'
    return jsonify(message)

@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')