#!/usr/bin/python2
import requests

headers = {
  'Content-Type': 'application/json',
  "app_id": "01646bc9",
  "app_key": "981a8af72b5b9e19a7d29e3938c70749"
}

url = "http://api.kairos.com/gallery/list_all"

# make request
r = requests.post(url, headers=headers)
print r.content
