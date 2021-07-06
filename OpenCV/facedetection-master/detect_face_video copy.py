
import cv2
import urllib.request
import numpy as np
import pickle
# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels ={}
with open("lapbels.pickle",'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}
# To capture video from webcam. 
url="http://192.168.43.92/cam-hi.jpg"
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    imgResponse =  urllib.request.urlopen(url)
    imgnp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    img=cv2.imdecode(imgnp,-1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray,1.1,5)
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
        id_, conf = recognizer.predict(roi_gray)
        if conf>=45 and conf <= 85:
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
            name = labels[id_]
            color = (255,255,255)
            stroke = 2
            cv2.putText(img,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
        else:
            print("not recognize")
        img_item = "7.png"
        cv2.imwrite(img_item,roi_color)
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        eyes = eyes_cascade.detectMultiScale(gray)
        #for (ex,ey,ew,eh) in eyes:
        #    cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0,255, 0), 2)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows
