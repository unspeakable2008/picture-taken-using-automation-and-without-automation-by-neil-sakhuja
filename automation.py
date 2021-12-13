from types import FrameType
import cv2
import dropbox
import time
import random
startTime = time.time()
def takeSnapshot():
    number= random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = "img"+ str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime = time.time()
        result = False
    return imageName
    print("takeSnapshot")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def uploadFiles(imageName):
    access_Token = "RCGVshM00JEAAAAAAAAAAZVUZbGFpyLOS-XkxSB75dFOwUWy0pFu5wDt2gvNMnaK"
    file_from = imageName
    file_to = "/testDropBox/"+(imageName)
    dbx = dropbox.Dropbox(access_Token) 
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to)
        print("fileUploaded")
def main():
    while(True):
        if (time.time()-startTime >=5):
            name = takeSnapshot()
            uploadFiles(name)
main()
