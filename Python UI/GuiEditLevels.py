# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guieditlevels.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget





class Ui_EditLevelWindow(QWidget):

    

    def add_row_subject(self):
        current_row_count = self.LvlWin_SubjectTable.rowCount()  # Get the current row count
        self.LvlWin_SubjectTable.insertRow(current_row_count)  # Insert a new row at the end
        line_edit = QtWidgets.QLineEdit(self.LvlWin_SubjectTable)
        line_edit.setPlaceholderText("Enter subject name")
    
    # Add the QLineEdit to the first column of the new row
        self.LvlWin_SubjectTable.setCellWidget(current_row_count, 0, line_edit)

    def remove_row_subject(self):
        current_row_count = self.LvlWin_SubjectTable.rowCount()  # Get the current row count
        self.LvlWin_SubjectTable.removeRow(current_row_count-1)

    def cancel(self):
        self.edit_level_window.close()

    
    def finish(self):
        from GuiMain import Ui_MainWindow
        complete_level = []
        table_values = self.get_table_values()

        level_name = self.LvlWin_LevelNameLineEdit.text()
        level_num_sections = self.LvlWin_LevelNumberSectionsLineEdit.text()

        complete_level.append(level_name)
        complete_level.append(level_num_sections)
        complete_level.append(table_values)

        level_name = complete_level[0]

        Ui_MainWindow = Ui_MainWindow()
        Ui_MainWindow.add_level(complete_level)
        #Ui_MainWindow.add_row_subject(level_name)

        

        self.edit_level_window.close()

    def get_table_values(self):
        table_values = []

        row_count = self.LvlWin_SubjectTable.rowCount()
        column_count = self.LvlWin_SubjectTable.columnCount()

        for row in range(row_count):

            line_edit_item = self.LvlWin_SubjectTable.cellWidget(row, 0)  # Get the QLineEdit widget from the first column
            table_values.append(line_edit_item.text())

        return table_values
            

        
        
        
        
        
      
    def setupUi(self, EditLevelWindow):
        self.edit_level_window = EditLevelWindow

        EditLevelWindow.setObjectName("EditLevelWindow")
        EditLevelWindow.resize(508, 547)
        self.centralwidget = QtWidgets.QWidget(EditLevelWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        
        self.LvlWin_LevelNameLineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.LvlWin_LevelNameLineEdit.setObjectName("LvlWin_LevelNameLineEdit")
        self.gridLayout_2.addWidget(self.LvlWin_LevelNameLineEdit, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.groupBox)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.LvlWin_AddButton = QtWidgets.QPushButton(self.frame_4, clicked = lambda: self.add_row_subject())

        self.LvlWin_AddButton.setObjectName("LvlWin_AddButton")
        self.gridLayout_4.addWidget(self.LvlWin_AddButton, 0, 0, 1, 1)

        self.LvlWin_RemoveButton = QtWidgets.QPushButton(self.frame_4, clicked = lambda: self.remove_row_subject())

        self.LvlWin_RemoveButton.setObjectName("LvlWin_RemoveButton")
        self.gridLayout_4.addWidget(self.LvlWin_RemoveButton, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 1)
        self.LvlWin_SubjectTable = QtWidgets.QTableWidget(self.groupBox)
        self.LvlWin_SubjectTable.setObjectName("LvlWin_SubjectTable")
        self.LvlWin_SubjectTable.setColumnCount(1)
        self.LvlWin_SubjectTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.LvlWin_SubjectTable.setHorizontalHeaderItem(0, item)
        self.LvlWin_SubjectTable.horizontalHeader().setDefaultSectionSize(450)

        self.LvlWin_SubjectTable.horizontalHeader().setSectionsClickable(False)

        # Disable selection for the vertical (left) header
        self.LvlWin_SubjectTable.verticalHeader().setSectionsClickable(False)

        self.gridLayout_5.addWidget(self.LvlWin_SubjectTable, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 2, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.LvlWin_FinishButton = QtWidgets.QPushButton(self.frame_3, clicked = lambda: self.finish())

        self.LvlWin_FinishButton.setObjectName("LvlWin_FinishButton")
        self.gridLayout_3.addWidget(self.LvlWin_FinishButton, 0, 0, 1, 1)

        self.LvlWin_CancelButton = QtWidgets.QPushButton(self.frame_3, clicked = lambda: self.cancel())

        self.LvlWin_CancelButton.setObjectName("LvlWin_CancelButton")
        self.gridLayout_3.addWidget(self.LvlWin_CancelButton, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_3, 3, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.LvlWin_LevelNumberSectionsLineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.LvlWin_LevelNumberSectionsLineEdit.setObjectName("LvlWin_LevelNumberSectionsLineEdit")
        self.gridLayout_7.addWidget(self.LvlWin_LevelNumberSectionsLineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_5, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        EditLevelWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EditLevelWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 21))
        self.menubar.setObjectName("menubar")
        EditLevelWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EditLevelWindow)
        self.statusbar.setObjectName("statusbar")
        EditLevelWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EditLevelWindow)
        QtCore.QMetaObject.connectSlotsByName(EditLevelWindow)

    def retranslateUi(self, EditLevelWindow):
        _translate = QtCore.QCoreApplication.translate
        EditLevelWindow.setWindowTitle(_translate("EditLevelWindow", "MainWindow"))
        self.label.setText(_translate("EditLevelWindow", "Level Name"))
        self.groupBox.setTitle(_translate("EditLevelWindow", "Subjects"))
        self.LvlWin_AddButton.setText(_translate("EditLevelWindow", "Add"))
        self.LvlWin_RemoveButton.setText(_translate("EditLevelWindow", "Remove"))
        item = self.LvlWin_SubjectTable.horizontalHeaderItem(0)
        item.setText(_translate("EditLevelWindow", "Subjects"))
        self.LvlWin_FinishButton.setText(_translate("EditLevelWindow", "Finish"))
        self.LvlWin_CancelButton.setText(_translate("EditLevelWindow", "Cancel"))
        self.label_2.setText(_translate("EditLevelWindow", "Number of Sections"))

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditLevelWindow = QtWidgets.QMainWindow()
    ui = Ui_EditLevelWindow()
    ui.setupUi(EditLevelWindow)
    EditLevelWindow.show()
    sys.exit(app.exec_())
