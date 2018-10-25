#!/usr/bin/python2
from urllib2 import Request, urlopen

values = """
  {
    "image": "http://18.222.253.203/images/subject_id.jpg",
    "gallery_name": "MyGallery",
    "subject_id": "Aishwarya Shand"
    
  }
"""

headers = {
  'Content-Type': 'application/json',
  "app_id": "437f528e",
  "app_key": "79b5ee9c50d854b4647a916a121891ea"
}
request = Request('https://api.kairos.com/verify', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body



