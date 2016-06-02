#!/usr/bin/env python

from flask import Flask,request,render_template, redirect, url_for, jsonify, Response
from RFShield import RFShield
import json
import threading
import logging

app = Flask(__name__, static_url_path='')
rfShield = RFShield()
switches=[]
def loadConfig():
  with open('config.json', 'r') as f:
    config = json.load(f)
    global switches
    switches = config
        #edit the data
        #config['key3'] = 'value3'

        #write it back to the file
        #with open('config.json', 'w') as f:
        #      json.dump(config, f)

@app.route('/')
def index():
  return app.send_static_file('index.html')

@app.route('/api/switches',methods=['GET'])
def getSwitches():
  return Response(json.dumps(switches), mimetype='application/json')

@app.route('/api/switches/<int:switchId>/on',methods=['POST'])
def turnOnSwitch(switchId):
  logging.debug("Turn on request received: %d",switchId)
  rfShield.transmitCode(switches[switchId].get('onCode'))
  return ('', 204)

@app.route('/api/switches/<int:switchId>/off',methods=['POST'])
def turnOffSwitch(switchId):
  logging.debug("Turn off request received: %d",switchId)
  rfShield.transmitCode(switches[switchId].get('offCode'))
  return ('', 204)

@app.route('/api/send',methods=['POST'])
def post():
  jsonRequest=request.get_json()
  code= jsonRequest.get('code')
  try:
    intCode = int(code)
    logging.debug("Code received: '{}'".format(intCode))
    rfShield.transmitCode(intCode)
    return ('', 204)
  except ValueError:
    print("Wrong code received: {}".format(code))
    return ('Wrong code',400)


if __name__ == '__main__':
  try:
    loadConfig()
    logging.basicConfig(level=logging.INFO)
    logging.info('Initializing...')
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host='0.0.0.0',port=80,debug=False)
  except KeyboardInterrupt:
    rfShield.cleanup()
  finally:
    rfShield.cleanup()
