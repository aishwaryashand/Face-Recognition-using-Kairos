#!/usr/bin/python2
from urllib2 import Request, urlopen
import camera
import os

nam=camera.x
path1="/home/adhoc/Desktop/attendance/Gallery/"+nam

# copy image captured to instance
os.system("scp -i /home/adhoc/Downloads/warya.pem  "+path1+"  ubuntu@18.222.253.203:/var/www/html/images")

path2="http://18.222.253.203/images/"+nam

values = """
  {
    "image": "%s",
    "gallery_name": "MyGallery"
  }
"""%(path2)

headers = {
  'Content-Type': 'application/json',
  "app_id": "437f528e",
  "app_key": "79b5ee9c50d854b4647a916a121891ea"
}
request = Request('https://api.kairos.com/recognize', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body
