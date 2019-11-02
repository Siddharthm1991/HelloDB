from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import db
import json
from decimal import Decimal
class Query(Resource):
    def post(self):
        print(request)
        jsonData = request.json
        print(jsonData)
        topIntent = jsonData['topScoringIntent']['intent']
        entities = jsonData['entities']

        res_query = ""
        if(topIntent == 'selectQuery'):
            tableName = ""
            for val in entities:
                if(val['type'] == 'tableName'):
                    tableName = val['entity'].lower()

            res_query = "SELECT * FROM "
            if(len(tableName) > 0):
                res_query += tableName
                cnx=db.getDBConn()
                cursor = db.execQuery(cnx, res_query)
                data =[]
                for t in cursor:
                    dict_row = dict(zip(cursor.column_names, t))
                    for col in dict_row:
                        if isinstance(dict_row[col], Decimal):
                            dict_row[col] = float(dict_row[col])
                    data.append(dict_row)
                cnx.close()
                return {'query': res_query, 'status':200, 'data':data}
            else:
                res_query = "Query could not be formed"
                return {'query': res_query, 'status':400, 'data':null}
        