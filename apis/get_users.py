from flask_app import app
from flask import jsonify, request


@app.route('/api/get_users', methods=['GET'])
def get_users():
   results = [{
      "name":"vipin",
      "class":"12"
   },{
      "name":"vipin345",
      "class":"122"
   }]
   return jsonify(results)
