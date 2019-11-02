
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import db


class DbSchema(Resource):
    def get(self):
        cnx = db.getDBConn()
        cursor = cnx.cursor()
        query = ''' 
            SELECT 
                table_name, 
                column_name 
            FROM 
                INFORMATION_SCHEMA.COLUMNS   
            WHERE 
                table_schema = "classicmodels" 
            ORDER BY 
                table_name, column_name;'''
        cursor.execute(query)
        out = {}
        for table_name, col_name in cursor:
            if table_name not in out:
                out[table_name] = []
            out[table_name].append(col_name)
        cnx.close()
        return out
