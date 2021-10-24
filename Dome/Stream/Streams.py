import cv2
from imutils.video import VideoStream
import urllib.request
import base64


class StreamLive(object):
    def __init__(self):
        #here is my constructor method
        self.video = cv2.VideoCapture(0)
        #threading.Thread(target=self.update_frame(), args=()).start()
        
        
    def __del__(self):
        #the release all video frame method is initialize here
        self.video.release()
        
    def get_frame(self):
        success, frame = self.video.read()
        frame_flip = cv2.flip(frame,1)
        frame = cv2.resize(frame, (640, 480))
        encoded, buffer = cv2.imencode('.jpg', frame)
        return buffer.tobytes()
        
    def update_frame(self):
        while(True):
            (self.grabbed, self.frame) = self.video.read()
            
		
		
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

