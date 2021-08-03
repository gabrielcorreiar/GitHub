import ast
import urllib
from urllib.request import urlopen
import json

url = "https://87dyrojjxk.execute-api.us-east-1.amazonaws.com/dev/fiap/raw"
response = urlopen(url)
data_json = json.loads(response.read())

json_object = json.dumps(data_json)

'''print(type(response))
print(type(data_json))
print(type(json_object))'''


with open("engage4.json", "w") as outfile:
    outfile.write(json_object)
 #   json.dump(data_json, outfile)

'''dictionary = [{
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}]


print(type(dictionary))'''






















'''import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)'''