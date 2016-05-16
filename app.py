from flask import Flask,request,render_template, redirect, url_for
from RFShield import RFShield
import threading
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)
rfShield = RFShield()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/',methods=['POST'])
def post():
	
	code=request.form['code']
	try:
        	intCode = int(code)
		print("Code received: '{}'".format(intCode))
		rfShield.transmitCode(intCode)
		return redirect('/')
	except ValueError:
		print("Wrong code received: {}".format(code))
		return ('Wrong code',400)


if __name__ == '__main__':
	try:
		app.run(host='0.0.0.0',port=80,debug=False)
	except KeyboardInterrupt:
		rfShield.cleanup()
	finally:
		rfShield.cleanup()
