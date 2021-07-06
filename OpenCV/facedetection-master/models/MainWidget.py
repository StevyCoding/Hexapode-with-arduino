from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

from models.RecordVideo import RecordVideo
from models.FaceDetectionWidget import FaceDetectionWidget

class MainWidget(QtWidgets.QWidget):
        def __init__(self, haarcascade_filepath, parent=None):
                super().__init__(parent)
                fp = haarcascade_filepath
                self.face_detection_widget = FaceDetectionWidget(fp)

                # TODO: set video port
                self.record_video = RecordVideo()
                self.run_button = QtWidgets.QPushButton('Start')
                self.label1  = QtWidgets.QLabel("temperatue: ")
                self.label2  = QtWidgets.QLabel("distance: ")

                # Connect the image data signal and slot together
                image_data_slot = self.face_detection_widget.image_data_slot
                self.record_video.image_data.connect(image_data_slot)
                # connect the run button to the start recording slot
                self.run_button.clicked.connect(self.record_video.start_recording)

                # Create and set the layout
                layout = QtWidgets.QVBoxLayout()
                layout.addWidget(self.face_detection_widget)
                layout.addWidget(self.run_button)


                self.setLayout(layout)