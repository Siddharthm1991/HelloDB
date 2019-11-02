from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from dbSchema import DbSchema
from query import Query
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['DEFAULT_PARSERS'] = [
            'flask.ext.api.parsers.JSONParser',
                'flask.ext.api.parsers.URLEncodedParser',
                    'flask.ext.api.parsers.MultiPartParser',
                    'flask.ext.api.parsers.FormParser'
                    ]
class HelloDb(Resource):
    def get(self):
        return {'Application':'HelloDb'}

api.add_resource(HelloDb, '/')
api.add_resource(DbSchema, '/dbSchema')
api.add_resource(Query, '/query')

if __name__ == '__main__':
    app.run(debug=True)
