#!/usr/bin/python2
from urllib2 import Request, urlopen

values = """
  {
    "gallery_name":"MyGallery",
    "subject_id":"aishwarya"
  }
"""

headers = {
  'Content-Type': 'application/json',
  "app_id": "01646bc9",
  "app_key": "981a8af72b5b9e19a7d29e3938c70749"
}
request = Request('https://api.kairos.com/gallery/view_subject', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
