from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from GuiEditBuildings import Ui_EditBuildingWindow
from GuiEditLevels import Ui_EditLevelWindow
from GuiEditRooms import Ui_EditRoomWindow




class GuiFunctions:


    def open_add_building(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EditBuildingWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_add_level(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EditLevelWindow()
        self.ui.setupUi(self.window)
        self.window.show()
                
    def open_add_rooms(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EditRoomWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def recieve_level_name(self, data):
        print(data)