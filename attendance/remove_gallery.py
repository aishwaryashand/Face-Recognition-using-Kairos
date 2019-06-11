#!/usr/bin/python2
import requests

values = """
  {
    "gallery_name":"MyGallery"
  }
"""

headers = {
  'Content-Type': 'application/json',
  "app_id": "01646bc9",
  "app_key": "981a8af72b5b9e19a7d29e3938c70749"
}

url = "http://api.kairos.com/gallery/remove"

# make request
r = requests.post(url, data=values, headers=headers)
print r.content
