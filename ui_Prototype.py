# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI-PrototypeXexeum.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(663, 517)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.close = QPushButton(self.centralwidget)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(10, 10, 35, 35))
       
        ## Widget Frame ##
        self.WidgetFrame = QFrame(self.centralwidget)
        self.WidgetFrame.setObjectName(u"WidgetFrame")
        self.WidgetFrame.setGeometry(QRect(10, 10, 661, 511))
        self.WidgetFrame.setFrameShape(QFrame.NoFrame)
        self.WidgetFrame.setFrameShadow(QFrame.Raised)       
       
        ## Good Counter Widget ##
        self.GaugeBase = QFrame(self.WidgetFrame)
        self.GaugeBase.setObjectName(u"GaugeBase")
        self.GaugeBase.setGeometry(QRect(10, 10, 320, 320))
        self.GaugeBase.setFrameShape(QFrame.NoFrame)
        self.GaugeBase.setFrameShadow(QFrame.Raised)
        self.GaugeBG = QFrame(self.GaugeBase)
        self.GaugeBG.setObjectName(u"GaugeBG")
        self.GaugeBG.setGeometry(QRect(10, 10, 300, 300))
        self.GaugeBG.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.GaugeBG.setFrameShape(QFrame.NoFrame)
        self.GaugeBG.setFrameShadow(QFrame.Raised)
        self.GaugeMeter = QFrame(self.GaugeBase)
        self.GaugeMeter.setObjectName(u"GaugeMeter")
        self.GaugeMeter.setGeometry(QRect(10, 10, 300, 300))
        self.GaugeMeter.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:0.799 rgba(255, 255, 255, 0), stop:0.8 rgb(0, 175, 255));\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:0.998rgba(0, 0, 0, 0), stop:0.999 rgb(0, 175, 255))\n"
"\n"
"}")
        self.GaugeMeter.setFrameShape(QFrame.NoFrame)
        self.GaugeMeter.setFrameShadow(QFrame.Raised)
        self.Interface = QFrame(self.GaugeBase)
        self.Interface.setObjectName(u"Interface")
        self.Interface.setGeometry(QRect(25, 25, 270, 270))
        self.Interface.setStyleSheet(u"QFrame{\n"
"border-radius:135;\n"
"background-color: rgb(77, 77, 127)\n"
"}")
        self.Interface.setFrameShape(QFrame.StyledPanel)
        self.Interface.setFrameShadow(QFrame.Raised)
        self.CounterLabel = QLabel(self.Interface)
        self.CounterLabel.setObjectName(u"CounterLabel")
        self.CounterLabel.setGeometry(QRect(-20, 170, 321, 20))
        font = QFont()
        font.setFamily(u"Mongolian Baiti")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(50)
        self.CounterLabel.setFont(font)
        self.CounterLabel.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.CounterLabel.setAlignment(Qt.AlignCenter) 
        self.GaugeName = QLabel(self.Interface)
        self.GaugeName.setObjectName(u"GaugeName")
        self.GaugeName.setGeometry(QRect(-20, 100, 311, 61))
        self.GaugeName.setFont(font)
        self.GaugeName.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.GaugeName.setAlignment(Qt.AlignCenter)
        self.CounterInt = QLabel(self.Interface)
        self.CounterInt.setObjectName(u"CounterInt")
        self.CounterInt.setGeometry(QRect(70, 200, 130, 31))
        self.CounterInt.setFont(font)
        self.CounterInt.setStyleSheet(u"background-color: #FFFFFF;\n"
"color: rgb(0, 120, 255)")
        self.CounterInt.setAlignment(Qt.AlignCenter)
        
        ## Meter Good Counter ##
        self.Border1 = QFrame(self.GaugeBase)
        self.Border1.setObjectName(u"Border1")
        self.Border1.setGeometry(QRect(10, 10, 300, 300))
        self.Border1.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240.001, stop:0 rgba(255, 255, 255, 255), stop:0.001 rgba(255, 255, 255, 0))\n"
"}")
        self.Border1.setFrameShape(QFrame.NoFrame)
        self.Border1.setFrameShadow(QFrame.Raised)
        self.Border2 = QFrame(self.GaugeBase)
        self.Border2.setObjectName(u"Border2")
        self.Border2.setGeometry(QRect(10, 10, 300, 300))
        self.Border2.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:299.001, stop:0 rgba(255, 255, 255, 255), stop:0.001 rgba(255, 255, 255, 0))\n"
"}")
        self.Border2.setFrameShape(QFrame.NoFrame)
        self.Border2.setFrameShadow(QFrame.Raised)
        
        self.GaugeBG.raise_()
        self.GaugeMeter.raise_()
        self.Border1.raise_()
        self.Border2.raise_()
        self.Interface.raise_()
        
        ## Reject Counter Widget ##
        self.GaugeBaseR = QFrame(self.WidgetFrame)
        self.GaugeBaseR.setObjectName(u"GaugeBaseR")
        self.GaugeBaseR.setGeometry(QRect(330, 10, 320, 320))
        self.GaugeBaseR.setFrameShape(QFrame.NoFrame)
        self.GaugeBaseR.setFrameShadow(QFrame.Raised)
        self.GaugeBaseR.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)                
        self.GaugeBGR = QFrame(self.GaugeBaseR)
        self.GaugeBGR.setObjectName(u"GaugeBGR")
        self.GaugeBGR.setGeometry(QRect(10, 10, 300, 300))
        self.GaugeBGR.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.GaugeBGR.setFrameShape(QFrame.NoFrame)
        self.GaugeBGR.setFrameShadow(QFrame.Raised)
        self.GaugeMeterR = QFrame(self.GaugeBaseR)
        self.GaugeMeterR.setObjectName(u"GaugeMeterR")
        self.GaugeMeterR.setGeometry(QRect(10, 10, 300, 300))
        self.GaugeMeterR.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:0.799 rgba(255, 255, 255, 0), stop:0.8 rgba(255, 50, 0, 255));\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:0.998 rgba(0, 0, 0, 0), stop:0.999 rgba(255, 50, 0, 255))\n"
"}")
        self.GaugeMeterR.setFrameShape(QFrame.NoFrame)
        self.GaugeMeterR.setFrameShadow(QFrame.Raised)
        self.InterfaceR = QFrame(self.GaugeBaseR)
        self.InterfaceR.setObjectName(u"InterfaceR")
        self.InterfaceR.setGeometry(QRect(25, 25, 270, 270))
        self.InterfaceR.setStyleSheet(u"QFrame{\n"
"border-radius:135;\n"
"background-color: rgb(77, 77, 127)\n"
"}")
        self.InterfaceR.setFrameShape(QFrame.StyledPanel)
        self.InterfaceR.setFrameShadow(QFrame.Raised)
        self.CounterLabelR = QLabel(self.InterfaceR)
        self.CounterLabelR.setObjectName(u"CounterLabelR")
        self.CounterLabelR.setGeometry(QRect(-20, 170, 321, 20))
        self.CounterLabelR.setFont(font)
        self.CounterLabelR.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.CounterLabelR.setAlignment(Qt.AlignCenter)
        self.GaugeNameR = QLabel(self.InterfaceR)
        self.GaugeNameR.setObjectName(u"GaugeNameR")
        self.GaugeNameR.setGeometry(QRect(-20, 100, 311, 61))
        self.GaugeNameR.setFont(font)
        self.GaugeNameR.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.GaugeNameR.setAlignment(Qt.AlignCenter)
        self.Counter = QLabel(self.InterfaceR)
        self.Counter.setObjectName(u"Counter")
        self.Counter.setGeometry(QRect(70, 200, 130, 31))
        self.Counter.setFont(font)
        self.Counter.setStyleSheet(u"background-color: #FFFFFF;\n"
"color: rgb(0, 120, 255)")
        self.Counter.setAlignment(Qt.AlignCenter)
        
        ## Meter Reject Counter ##
        self.Border1R = QFrame(self.GaugeBaseR)
        self.Border1R.setObjectName(u"Border1R")
        self.Border1R.setGeometry(QRect(10, 10, 300, 300))
        self.Border1R.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240.001, stop:0 rgba(255, 255, 255, 255), stop:0.001 rgba(255, 255, 255, 0))\n"
"}")
        self.Border1R.setFrameShape(QFrame.StyledPanel)
        self.Border1R.setFrameShadow(QFrame.Raised)
        self.Border2R = QFrame(self.GaugeBaseR)
        self.Border2R.setObjectName(u"Border2R")
        self.Border2R.setGeometry(QRect(10, 10, 300, 300))
        self.Border2R.setStyleSheet(u"QFrame{\n"
"border-radius: 150px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:299.001, stop:0 rgba(255, 255, 255, 255), stop:0.001 rgba(255, 255, 255, 0))\n"
"}")
        self.Border2R.setFrameShape(QFrame.StyledPanel)
        self.Border2R.setFrameShadow(QFrame.Raised)
        self.GaugeBGR.raise_()
        self.GaugeMeterR.raise_()
        self.Border1R.raise_()
        self.Border2R.raise_()
        self.InterfaceR.raise_()
        
        ## Control Button, Total Good Counter ##
        self.CounterBase = QFrame(self.WidgetFrame)
        self.CounterBase.setObjectName(u"CounterBase")
        self.CounterBase.setGeometry(QRect(20, 350, 621, 151))
        self.CounterBase.setFrameShape(QFrame.Box)
        self.CounterBase.setFrameShadow(QFrame.Raised)
        self.CounterBase.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)                
        self.TargetLabel = QLabel(self.CounterBase)
        self.TargetLabel.setObjectName(u"TargetLabel")
        self.TargetLabel.setGeometry(QRect(270, 10, 101, 41))
        self.TargetLabel.setFont(font)
        self.TargetLabel.setStyleSheet(u"background-color: none;\n"
"color: rgb(0, 0, 0)")
        self.TargetLabel.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.CounterBase)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 90, 161, 51))
        font1 = QFont()
        font1.setFamily(u"Mongolian Baiti")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton_2 = QPushButton(self.CounterBase)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 90, 161, 51))
        self.pushButton_2.setFont(font1)
        
        ## Total Good Counter ##
        self.TargetLabel_2 = QLabel(self.CounterBase)
        self.TargetLabel_2.setObjectName(u"TargetLabel_2")
        self.TargetLabel_2.setGeometry(QRect(180, 40, 271, 41))
        self.TargetLabel_2.setFont(font)
        self.TargetLabel_2.setAlignment(Qt.AlignCenter)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Catridge Counter", None))
        self.CounterLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">CURRENT COUNT</span></p></body></html>", None))
        self.GaugeName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">GOOD</span></p></body></html>", None))
        self.CounterInt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#0078ff;\">0</span></p></body></html>", None))
        self.CounterLabelR.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">CURRENT COUNT</span></p></body></html>", None))
        self.GaugeNameR.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">REJECT</span></p></body></html>", None))
        self.Counter.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#af0000;\">0</span></p></body></html>", None))
        self.TargetLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#000000;\">TOTAL</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.close.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.TargetLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0</p></body></html>", None))
    # retranslateUi

