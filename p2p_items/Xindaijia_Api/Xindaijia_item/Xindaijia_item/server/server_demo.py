


import json
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
app = Flask(__name__)

from flask import abort


@app.route('/qianhai/api.test', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def http_method_example(xingdaijia_data):
    

    # if request.method == 'GET':
    #     #return 'Send request with `GET` method'
    #     return jsonify({'start_code':'200','data':xingdaijia_data})
    if request.method == 'POST':
        # return 'Send request with `POST` method'
        return jsonify({'start_code':'200','data':xingdaijia_data})
    elif request.method == 'PUT':
        return 'Send request with `PUT` method'
    elif request.method == 'PATCH':
        return 'Send request with `PATCH` method'
    elif request.method == 'DELETE':
        return 'Send request with `DELETE` method'

if __name__ == '__main__':
    app.run(debug=True,port=6500)