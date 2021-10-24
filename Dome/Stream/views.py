from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from imutils.video import VideoStream
from .Streams import *

@gzip.gzip_page
def Home(request):
    try:
        return StreamingHttpResponse(gen(StreamLive()),
					content_type='multipart/x-mixed-replace; boundary=frame')
        #return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass

    return render(request, "index.html")
    
    
					
@gzip.gzip_page  
def class_room(request):
    return StreamingHttpResponse(gen(classroom()),
					content_type='multipart/x-mixed-replace; boundary=frame')
