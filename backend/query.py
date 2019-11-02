from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource



class Query(Resource):
    def post(self):
        jsonData = request.json
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
                return {'query': res_query, 'status':200}
            else:
                res_query = "Query could not be formed"
                return {'query': res_query, 'status':400}
            

# text = "get data from emploe"
# url = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/274b0beb-01bd-4fb0-b8c8-4d63d5cbeba1?staging=true&verbose=true&timezoneOffset=-360&subscription-key=5ddec480deda4a3ea442cdd812bf429a&q="+text
# res = requests.get(url)
# jsonData = json.loads(res.content)
# print(jsonData)
# topIntent = jsonData['topScoringIntent']['intent']
# entities = jsonData['entities']

# res_query = ""
# if(topIntent == 'selectQuery'):
#     tableName = ""
#     for val in entities:
#         if(val['type'] == 'tableName'):
#             tableName = val['entity'].lower()

#     res_query = "SELECT * FROM "
#     if(len(tableName) > 0):
#         res_query += tableName
#     else:
#         res_query = "Query could not be formed"

# print(res_query)