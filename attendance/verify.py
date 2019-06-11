#!/usr/bin/python2
from urllib2 import Request, urlopen

#!/usr/bin/python2
import cv2
from urllib2 import Request, urlopen
import base64
import json
import camera

encoded_string = base64.b64encode(open("Gallery/test.jpg", 'r').read())
payload_dict = {
    "image":encoded_string,
    "selector": "ROLL"
}
payload = json.dumps(payload_dict)

headers = {
  'Content-Type': 'application/json',
  "app_id": "01646bc9",
  "app_key": "981a8af72b5b9e19a7d29e3938c70749"
}

values = """
  {
    "image": "http://18.222.253.203/images/subject_id.jpg",
    "gallery_name": "MyGallery",
    "subject_id": "kamakshi"
    
  }
"""

headers = {
  'Content-Type': 'application/json',
  "app_id": "01646bc9",
  "app_key": "981a8af72b5b9e19a7d29e3938c70749"
}
request = Request('https://api.kairos.com/verify', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body


