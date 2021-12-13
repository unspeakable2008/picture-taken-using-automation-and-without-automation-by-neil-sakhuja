from types import FrameType
import cv2
def takeSnapshot():
    videoCapturedObject = cv2.VideoCapture(0)  
    result = True
    while(result):
        ret,frame = videoCapturedObject.read()
        cv2.imwrite("myImage.jpg",frame)
        result = False
    videoCapturedObject.release()
    cv2.destroyAllWindows()
takeSnapshot()
