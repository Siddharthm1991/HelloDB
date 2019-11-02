import requests
import json

text = "get data from"
url = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/274b0beb-01bd-4fb0-b8c8-4d63d5cbeba1?staging=true&verbose=true&timezoneOffset=-360&subscription-key=5ddec480deda4a3ea442cdd812bf429a&q="+text
res = requests.get(url)
jsonData = json.loads(res.content)
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
    else:
        res_query = "Query could not be formed"

print(res_query)