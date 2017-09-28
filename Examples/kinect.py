from pykinect import nui
import numpy
import cv2

def video_handler_function(frame):
    video = numpy.empty((480,640,4),numpy.uint8)
    frame.image.copy_bits(video.ctypes.data)
    cv2.imshow('KINECT Video Stream', video)

kinect = nui.Runtime()
kinect.video_frame_ready += video_handler_function
kinect.video_stream.open(nui.ImageStreamType.Video, 2,nui.ImageResolution.Resolution640x480,nui.ImageType.Color)

cv2.namedWindow('KINECT Video Stream', cv2.WINDOW_AUTOSIZE)

while True:

    key = cv2.waitKey(1)
    if key == 27: break

kinect.close()
cv2.destroyAllWindows()
