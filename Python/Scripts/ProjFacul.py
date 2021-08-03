'''from urllib.request import urlopen
import json
import redis

url = "https://87dyrojjxk.execute-api.us-east-1.amazonaws.com/dev/fiap/raw"
response = urlopen(url)
data_json = json.loads(response.read())

json_object = json.dumps(data_json, indent=4)

r = redis.StrictRedis(host='redis-19907.c267.us-east-1-4.ec2.cloud.redislabs.com', port=19907, db='engage', password='kruYdZXe8RsBOv5I3JJlTXRHskX8KyDj')
##print(r)
r.set('a_json', json_object)'''


'''import redis
from redis import StrictRedis
#redis=StrictRedis(host='localhost', port=6379, db=0, password='')
redis= redis.StrictRedis(host='redis-19907.c267.us-east-1-4.ec2.cloud.redislabs.com', port=19907, password='kruYdZXe8RsBOv5I3JJlTXRHskX8KyDj')
redis.set('name','lili')
print(redis.get('name'))'''



'''from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.database_name
collection = db.collection_name
print(collection)
collection.find_one({"name": "name1"})

for db in client.list_databases():
    print(db)'''

from urllib.request import urlopen
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['engage']
collection_currency = db['engage_raw']


url = "https://87dyrojjxk.execute-api.us-east-1.amazonaws.com/dev/fiap/raw"
response = urlopen(url)
data_json = json.loads(response.read())

#json_object = json.dumps(data_json, indent=4)
#with open('engage3.json') as f:
#    file_data = json.load(f)

# if pymongo < 3.0, use insert()
#collection_currency.insert(file_data)
# if pymongo >= 3.0 use insert_one() for inserting one document
#collection_currency.insert_one(file_data)
# if pymongo >= 3.0 use insert_many() for inserting many documents
collection_currency.insert_many(data_json)

client.close()