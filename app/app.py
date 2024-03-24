from flask import Flask, render_template, Response, request, jsonify
from camera import VideoCamera
import pandas as pd
#from webservices import app_webservices

app = Flask(__name__)

@app.route("/")
def index():
    # rendering webpage
    return render_template("index.html")

def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        #print(camera.drowsy)
        #drowsy = camera.get_frame2()
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")
        #yield is_drowsy
        

@app.route("/video_feed")
def video_feed():
    s = VideoCamera()
    resp = Response(gen(s),
                mimetype="multipart/x-mixed-replace; boundary=frame")#,
                #response="hello")
    #return Response(gen(VideoCamera()),
                    #mimetype="multipart/x-mixed-replace; boundary=frame")
    return render_template("index.html", drowsy = s.drowsy)

@app.route("/get-data",methods=['GET', 'POST'])
def get_data():
    data = "hello world"
    return data

if __name__ == "__main__":
    # defining server ip address and port
    app.run(host="127.0.0.1",port="5001", debug=True)