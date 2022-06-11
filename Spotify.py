# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfazSpotify.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(948, 602)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_Rewind = QtWidgets.QPushButton(self.centralwidget)
        self.button_Rewind.setGeometry(QtCore.QRect(340, 380, 61, 61))
        self.button_Rewind.setAutoFillBackground(False)
        self.button_Rewind.setStyleSheet("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"    \n"
"    border-image: url(:/newPrefix/Button_Rewind_OFF.jpg);\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/newPrefix/Button_Rewind_ON.jpg);\n"
"}\n"
"")
        self.button_Rewind.setText("")
        self.button_Rewind.setObjectName("button_Rewind")
        self.button_Play = QtWidgets.QPushButton(self.centralwidget)
        self.button_Play.setGeometry(QtCore.QRect(440, 380, 61, 61))
        self.button_Play.setAutoFillBackground(False)
        self.button_Play.setStyleSheet("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"    border-image: url(:/newPrefix/Button_Play_OFF.jpg);\n"
"padding: 5px;\n"
"}\n"
"QPushButton::checked{\n"
"border-image: url(:/newPrefix/Button_Pause_OFF.jpg);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed:!checked {\n"
"border-image: url(:/newPrefix/Button_Play_ON.jpg);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed:checked {\n"
"border-image: url(:/newPrefix/Button_Pause_ON.jpg);\n"
"}\n"
"\n"
"")
        self.button_Play.setText("")
        self.button_Play.setCheckable(True)
        self.button_Play.setObjectName("button_Play")
        self.button_FF = QtWidgets.QPushButton(self.centralwidget)
        self.button_FF.setGeometry(QtCore.QRect(540, 380, 61, 61))
        self.button_FF.setStyleSheet("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"    border-image: url(:/newPrefix/Button_FF_OFF.jpg);\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/newPrefix/Button_FF_ON.jpg);\n"
"}\n"
"")
        self.button_FF.setText("")
        self.button_FF.setCheckable(True)
        self.button_FF.setObjectName("button_FF")
        self.button_Random = QtWidgets.QPushButton(self.centralwidget)
        self.button_Random.setGeometry(QtCore.QRect(830, 440, 61, 61))
        self.button_Random.setStyleSheet("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"    border-image: url(:/newPrefix/Button_Random_OFF.jpg);\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"border-image: url(:/newPrefix/Button_Random_ON.jpg);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed:!checked {\n"
"border-image: url(:/newPrefix/Button_Random_ON.jpg);\n"
"}\n"
"\n"
"")
        self.button_Random.setText("")
        self.button_Random.setCheckable(True)
        self.button_Random.setChecked(False)
        self.button_Random.setObjectName("button_Random")
        self.slider_MusicDuration = QtWidgets.QSlider(self.centralwidget)
        self.slider_MusicDuration.setGeometry(QtCore.QRect(200, 460, 551, 22))
        self.slider_MusicDuration.setStyleSheet("QSlider::groove:horizontal{\n"
"    border: 1px solid black;\n"
"    height: 5px;\n"
"    background: rgb(119, 221, 119);\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"    background: white;\n"
"    border: 1px solid black;\n"
"    width: 10px;\n"
"    margin: -4px 0;\n"
"    border-radius: 9px\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"    background: white;\n"
"    border: 1px solid black;\n"
"}")
        self.slider_MusicDuration.setSingleStep(0)
        self.slider_MusicDuration.setOrientation(QtCore.Qt.Horizontal)
        self.slider_MusicDuration.setObjectName("slider_MusicDuration")
        self.label_SoundStart = QtWidgets.QLabel(self.centralwidget)
        self.label_SoundStart.setGeometry(QtCore.QRect(160, 460, 31, 16))
        self.label_SoundStart.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_SoundStart.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_SoundStart.setTextFormat(QtCore.Qt.RichText)
        self.label_SoundStart.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SoundStart.setObjectName("label_SoundStart")
        self.button_Repeat = QtWidgets.QPushButton(self.centralwidget)
        self.button_Repeat.setGeometry(QtCore.QRect(60, 440, 61, 61))
        self.button_Repeat.setStyleSheet("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"    border-image: url(:/newPrefix/Button_Repeat_OFF.jpg);\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/newPrefix/Button_Repeat_ON.jpg);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"border-image: url(:/newPrefix/Button_Repeat_ON.jpg);\n"
"}")
        self.button_Repeat.setText("")
        self.button_Repeat.setCheckable(True)
        self.button_Repeat.setObjectName("button_Repeat")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 541, 341))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(610, 20, 261, 261))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 290, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 320, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 981, 551))
        self.label_4.setStyleSheet("background-color: rgb(66,66,66);")
        self.label_4.setObjectName("label_4")
        self.label_SoundEnd = QtWidgets.QLabel(self.centralwidget)
        self.label_SoundEnd.setGeometry(QtCore.QRect(760, 460, 31, 16))
        self.label_SoundEnd.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_SoundEnd.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_SoundEnd.setTextFormat(QtCore.Qt.RichText)
        self.label_SoundEnd.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SoundEnd.setObjectName("label_SoundEnd")
        self.label_4.raise_()
        self.button_Rewind.raise_()
        self.button_Play.raise_()
        self.button_FF.raise_()
        self.button_Random.raise_()
        self.slider_MusicDuration.raise_()
        self.label_SoundStart.raise_()
        self.button_Repeat.raise_()
        self.listWidget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_SoundEnd.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 948, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_SoundStart.setText(_translate("MainWindow", "0:00"))
        self.label_2.setText(_translate("MainWindow", "Nombre de la Canción"))
        self.label_3.setText(_translate("MainWindow", "Artista"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_SoundEnd.setText(_translate("MainWindow", "0:00"))
import Button_icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
