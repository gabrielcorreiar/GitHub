from urllib.request import urlopen
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['engage']
collection_currency = db['engage_new']


url = "https://87dyrojjxk.execute-api.us-east-1.amazonaws.com/dev/fiap/raw"
response = urlopen(url)
data_json = json.loads(response.read())

#json_object = json.dumps(data_json, indent=4)
#with open('engage3.json') as f:
#    file_data = json.load(f)

# if pymongo < 3.0, use insert()
#collection_currency.insert(data_json)


# if pymongo >= 3.0 use insert_one() for inserting one document
#collection_currency.insert_one(data_json)


# if pymongo >= 3.0 use insert_many() for inserting many documents
collection_currency.insert_many(data_json)

client.close()