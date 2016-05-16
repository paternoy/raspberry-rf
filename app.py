from flask import Flask,request,render_template, redirect, url_for
import threading
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/',methods=['POST'])
def post():
	
	code=request.form['code']
	if ~(code.isdigit()):
		print("Wrong code received: {}".format(code))
		return ('Wrong code',400)
	else:
		print("Code received: {}".format(code))
		return ('', 204)


if __name__ == '__main__':
#	try:
	app.run(host='0.0.0.0',port=80,debug=False)
                #GPIO.cleanup() # cleanup all GPIO
#	except KeyboardInterrupt:
#		onOff.cleanup()
#	finally:
#		onOff.cleanup()
