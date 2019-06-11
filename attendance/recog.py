#!/usr/bin/python2
import cv2
from urllib2 import Request, urlopen
import base64
import json
import camera
import objectpath

encoded_string = base64.b64encode(open("Gallery/test.jpg", 'r').read())
payload_dict = {
    "image":encoded_string,
    "gallery_name": "MyGallery"
}
payload = json.dumps(payload_dict)

headers = {
  'Content-Type': 'application/json',
  'app_id': '01646bc9',
  'app_key': '981a8af72b5b9e19a7d29e3938c70749'
}

request = Request('https://api.kairos.com/recognize', data=payload, headers=headers)
response_body = urlopen(request).read()
print(response_body)


'''
with open('data.json', 'w') as outfile:
    json.dump(response_body, outfile)

with open ("data.json") as datafile: data=json.load(datafile)
#dumps the json object into an element
json_str = json.dumps(data)
#load the json to a string
resp = json.loads(json_str)
#extract an element in the response
print (resp['face_id'])
'''
