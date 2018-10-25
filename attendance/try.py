#!/usr/bin/python2
import os,sys,time
import commands,os
import cgi,cgitb

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

#Data is retrieved
data=cgi.FieldStorage()
choice=data.getvalue('choice')

print "<center>"
print "Click on the image to save the file!"
print "</br>"
print "Open the saved file and run the code on your terminal."
print "\n"
print "</br>"
print "root's password:redhat"
print "</br>"

if  choice == 'enroll':

    print "<a href='http://192.168.122.1/home/adhoc/Desktop/attendance/enroll.py>"
    print "<img src='http://0www.free-icons-download.net/images/download-button-icon-27698.png' style='width:200px;height:200px;'>"
    print "</a>"
   
elif  choice == "Rec":

    print "<a href='http://192.168.43.109/vlc.sh.tar.gz'>"
    print "<img src='http://www.free-icons-download.net/images/download-button-icon-27698.png' style='width:200px;height:200px;'>"
    print "</a>"   

elif  choice == "Gedit":

    print "<a href='http://192.168.43.109/gedit.sh.tar.gz'>"
    print "<img src='http://www.free-icons-download.net/images/download-button-icon-27698.png' style='width:200px;height:200px;'>"
    print "</a>"

else:

    print "<a href='http://192.168.43.109/cheese.sh.tar.gz'>"
    print "<img src='http://www.free-icons-download.net/images/download-button-icon-27698.png' style='width:200px;height:200px;'>"
    print "</a>"
