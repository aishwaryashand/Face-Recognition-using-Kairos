#!/usr/bin/python2
import requests

values ="""
 {
    "gallery_name": "MyGallery"
  }
"""

headers = {
  'Content-Type': 'application/json',
  "app_id": "437f528e",
  "app_key": "79b5ee9c50d854b4647a916a121891ea"
}

url = "http://api.kairos.com/gallery/view"

# make request
r = requests.post(url, data=values, headers=headers)
print r.content
