#!/usr/bin/env python
import cv2
from urllib2 import Request, urlopen
import base64
import json
from add_student import name, roll, Id

encoded_string = base64.b64encode(open("dataset/user" + Id + "/User."+ Id +".1" + ".jpg", 'r').read())
payload_dict = {
    "image":encoded_string,
    "subject_id": name,
    "gallery_name": "MyGallery"
}
payload = json.dumps(payload_dict)
headers={
'Content-Type':'application/json',
"app_id": "01646bc9",
"app_key": "981a8af72b5b9e19a7d29e3938c70749"
}
request = Request('https://api.kairos.com/enroll', data=payload, headers=headers)
response_body = urlopen(request).read()
print(response_body)

