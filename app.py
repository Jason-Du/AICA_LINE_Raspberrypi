# -*- coding: UTF-8 -*-
from flask import Flask ,request
from flask import render_template
from picamera import PiCamera
from time import sleep

import requests
app = Flask(__name__)
"""
@app.route('/')
def index():
    return 'Hello ATCA!!'    #回傳字串，讓使用看到


@app.route("/", methods=['GET'])
def index2():
    name = request.args.get(key='name')
    print(str(name))
    return "Hello"+str(name)
    """ 
@app.route("/", methods=['GET'])
def photo():
    photo_enable = request.args.get(key='photo')
    print(str(photo_enable))
    if(str(photo_enable)=="ON"):
        try:
            camera = PiCamera()
            sleep(5)
            camera.start_preview()
            camera.capture('./image.jpg')
            camera.stop_preview()
            camera.close()
        except:
            print("camera_fail")
    return "successful"
if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0', port=2224)