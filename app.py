from flask import Flask
from flask_restful import Resource, Api
from flask import render_template, make_response, request
import json
import requests
import pymongo
from mongo import get_db, verifyToken, saveToIp, createUser

app = Flask(__name__)
api = Api(app)


class Get_Page(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'),200,headers)

class GetToken(Resource):
    def post(self):
        data = request.json
        print(data)
        check_ip_count = saveToIp(data)
        verify_token = True
        if data['token'] != None:
            verify_token = verifyToken(data)
            if(verify_token):
                resp = createUser(data)
                return resp
            else:
                return 'token did not verify'
        if(check_ip_count):
            return check_ip_count




api.add_resource(Get_Page, '/')
api.add_resource(GetToken, '/add')

if __name__ == '__main__':
    app.run(debug=True)