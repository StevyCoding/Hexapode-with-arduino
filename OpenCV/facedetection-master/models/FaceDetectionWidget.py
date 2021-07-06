
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import cv2
import numpy as np
import pickle
from socket import *
import keyboard
class FaceDetectionWidget(QtWidgets.QWidget):
        def __init__(self, haar_cascade_filepath, parent=None):
                super().__init__(parent)
                self.classifier = cv2.CascadeClassifier(cv2.data.haarcascades + haar_cascade_filepath)
                self.image = QtGui.QImage()
                self._red = (0, 0, 255)
                self._width = 2
                self._min_size = (30, 30)
                self.recognizer = cv2.face.LBPHFaceRecognizer_create()
                self.recognizer.read("trainer.yml")
                self.labels ={}
                with open("lapbels.pickle",'rb') as f:
                    og_labels = pickle.load(f)
                    self.labels = {v:k for k,v in og_labels.items()}

        def detect_faces(self, image: np.ndarray):
                # haarclassifiers work better in black and white
                self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces = self.classifier.detectMultiScale(self.gray, scaleFactor=1.3, minNeighbors=4, flags=cv2.CASCADE_SCALE_IMAGE, minSize=self._min_size)

                return faces

        def image_data_slot(self, image_data):
                faces = self.detect_faces(image_data)
                # HOST = '192.168.43.92' #  or 'localhost'
                # PORT = 85
                # BUFSIZ = 1024
                # ADDR=(HOST,PORT)
                # tcpCliSock = socket(AF_INET,SOCK_STREAM)
                # tcpCliSock.connect(ADDR)
                # data = ""
                # if keyboard.is_pressed('z'):
                #         data = "z"
                #         print('data=',data);
                #         tcpCliSock.send(data.encode())
                # elif keyboard.is_pressed('q'):
                #         data = "q"
                #         print('data=',data);
                #         tcpCliSock.send(data.encode())
                # elif keyboard.is_pressed('d'):
                #         data = "d"
                #         print('data=',data);
                #         tcpCliSock.send(data.encode())
                # elif keyboard.is_pressed('s'):
                #         data = "s"
                #         print('data=',data);
                # tcpCliSock.send(data.encode())
                for (x, y, w, h) in faces:
                    
                    roi_gray = self.gray[y:y+h,x:x+w]
                    roi_color = image_data[y:y+h,x:x+w]
                    id_, conf = self.recognizer.predict(roi_gray)
                    if conf>=45 and conf <= 85:
                        print(id_)
                        print(self.labels[id_])
                        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
                        name = self.labels[id_]
                        color = (0,255,0)
                        stroke = 2
                        cv2.putText(image_data,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
                    else:
                        print("not recognize")
                        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
                        color = (255,255,255)
                        stroke = 2
                        cv2.putText(image_data,"non reconnu",(x,y),font,1,color,stroke,cv2.LINE_AA)
                    img_item = "7.png"
                    cv2.imwrite(img_item,roi_color)
                    cv2.rectangle(image_data, (x, y), (x+w, y+h), self._red, self._width)
                self.image = self.get_qimage(image_data)
                if self.image.size() != self.size():
                        self.setFixedSize(self.image.size())

                self.update()

        def get_qimage(self, image: np.ndarray):
                height, width, colors = image.shape
                bytesPerLine = 3 * width
                QImage = QtGui.QImage

                image = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)

                image = image.rgbSwapped()
                return image

        def paintEvent(self, event):
                painter = QtGui.QPainter(self)
                painter.drawImage(0, 0, self.image)
                self.image = QtGui.QImage()