from PyQt5 import QtWidgets
from os import path
from models.MainWidget import MainWidget

import sys

def main(haar_cascade_filepath):
        app = QtWidgets.QApplication(sys.argv)

        main_window = QtWidgets.QMainWindow()
        main_widget = MainWidget(haar_cascade_filepath)
        main_window.setCentralWidget(main_widget)
        main_window.show()
        sys.exit(app.exec_())


               

if __name__ == '__main__':

        main("haarcascade_frontalface_default.xml")