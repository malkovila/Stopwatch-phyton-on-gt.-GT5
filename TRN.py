import datetime
import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 264)
        MainWindow.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(30, 20, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    border: 1px solid white;\n"
"}")
        self.start_button.setObjectName("start_button")
        self.finish_button = QtWidgets.QPushButton(self.centralwidget)
        self.finish_button.setGeometry(QtCore.QRect(280, 20, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.finish_button.setFont(font)
        self.finish_button.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    border: 1px solid white;\n"
"}\n"
"")
        self.finish_button.setObjectName("finish_button")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 130, 471, 101))
        font = QtGui.QFont()
        font.setPointSize(42)
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_func()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "Старт"))
        self.finish_button.setText(_translate("MainWindow", "Сброс"))
        self.lineEdit.setText(_translate("MainWindow", "00:00:00"))


    isStart = False
    def add_func(self):
        self.start_button.clicked.connect(self.start)
        self.finish_button.clicked.connect(self.finish)
    def start(self):
        global isStart
        isStart = True
        thr = threading.Thread(target=self.timere, name='thr-1')
        thr.start()

    def finish(self):
        global isStart
        isStart = False
        print(isStart)
    def timere(self):
        global isStart
        sec = 0
        while isStart:
            print(sec)
            time.sleep(1)
            sec += 1
            hours = sec // 3600
            minut = (sec%3600)//60
            seconds = sec % 60
            if hours > 99:
                isStart == False
            else:
                hours = str(hours); minut = str(minut); seconds = str(seconds)
                time_str = '0'*(2-len(hours)) + hours + ':' + '0'*(2-len(minut)) + minut+':' + '0'*(2-len(seconds))+ seconds
                self.lineEdit.setText(time_str)
        else:
            return





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
