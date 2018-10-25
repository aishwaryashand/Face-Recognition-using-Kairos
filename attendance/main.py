#!usr/bin/python2

from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')

def index():
	return render_template('try.html')

@app.route('/video_feed')
def video_feed():
	import enroll

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
