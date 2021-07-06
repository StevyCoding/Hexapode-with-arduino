import cv2
from PyQt5 import QtCore
import numpy as np
import urllib.request

class RecordVideo(QtCore.QObject):
        image_data = QtCore.pyqtSignal(np.ndarray)

        def __init__(self, camera_port=0, parent=None):
                super().__init__(parent)

                self.url = "http://192.168.43.92/cam-hi.jpg"
                self.timer = QtCore.QBasicTimer()

        def start_recording(self):
                self.timer.start(0, self)

        def timerEvent(self, event):
                if (event.timerId() != self.timer.timerId()):
                        return
                
                imgResponse =  urllib.request.urlopen(self.url)
                imgnp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
                image = cv2.imdecode(imgnp,-1)
                self.image_data.emit(image)
                