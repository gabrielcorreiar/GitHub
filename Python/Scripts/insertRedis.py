from urllib.request import urlopen
import json
import redis

url = "https://87dyrojjxk.execute-api.us-east-1.amazonaws.com/dev/fiap/raw"
response = urlopen(url)
data_json = json.loads(response.read())

json_object = json.dumps(data_json, indent=4)

r = redis.StrictRedis(host='localhost', port=6379, db=0, password='')

r.json.set('b_json', json_object)