from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from dbSchema import DbSchema
from query import Query

app = Flask(__name__)
api = Api(app)

class HelloDb(Resource):
    def get(self):
        return {'Application':'HelloDb'}

api.add_resource(HelloDb, '/')
api.add_resource(DbSchema, '/dbSchema')
api.add_resource(Query, '/query')

if __name__ == '__main__':
    app.run(debug=True)
