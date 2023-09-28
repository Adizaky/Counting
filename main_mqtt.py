import sys, traceback
import platform
import RPi.GPIO as GPIO
from paho.mqtt import client as mqtt_client
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QRunnable, Slot, Signal, QThreadPool, QThread, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_Prototype import Ui_MainWindow

GPIO.setmode(GPIO.BCM)

# inisialisasi pin raspi
proximity1 = 2
proximity2 = 3
servo = 14
GPIO.setup(proximity1,GPIO.IN)
GPIO.setup(proximity2,GPIO.IN)
GPIO.setup(servo,GPIO.OUT)
GPIO.output(servo,GPIO.HIGH)

# pengaturan input gauge
maxGauge = 20000
maxGaugeR = maxGauge/20
Cat_val_blue = 0.835/maxGauge
Cat_val_red = 0.835/maxGaugeR

# inisialisasi counter
reject = 0
good = 0

# simulasi message mqtt
msg = 'CRITICAL 1234'

# thread mqtt
class mqttThread(QThread):
    global msg
    
    mqttSignal = Signal(str)
    mqttFinished = Signal()
    
    def __init__(self, *args, **kwargs):
        global msg        
        print('mqtt jalan')
        QThread.__init__(self, *args, **kwargs)
    
    def run(self,  *args, **kwargs):
        global msg        
        while True:
            x = input('mqtt:')
            if x == '1':
                self.mqttSignal.emit(msg)       
    
    def destroy(self):
        print('mqtt stop')
        self.exit()

# thread sensor
class RelayThread(QThread):
    event_detected = Signal(int)
    threadFinished = Signal()
    
    def destroy(self):
        print("destroy thread")
        GPIO.remove_event_detect(proximity1)
        GPIO.remove_event_detect(proximity2)
        self.exit()
    
    def __init__(self, *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)
        GPIO.add_event_detect(proximity1,GPIO.BOTH, self.emit1,10)
        GPIO.add_event_detect(proximity2,GPIO.BOTH, self.emit2,10)

    def emit1(self, event):
        self.event_detected.emit(1)
        
    def emit2(self, event):
        self.event_detected.emit(2)

# thread mainwindow UI
class Gauge(QMainWindow):
    global reject, good, kondisiStart, msg    
    
    def __init__(self):        
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        self.ui.pushButton.setCheckable(True)
        self.ui.pushButton.clicked.connect(self.Start)        
        self.ui.pushButton_2.clicked.connect(self.Reset)
        self.ui.close.clicked.connect(self.Close)
        
        self.cat_good()
        self.cat_reject()
        
        self.setWindowFlags(Qt.FramelessWindowHint)        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)        
        self.showMaximized()
        self.ui.WidgetFrame.move(qr.topLeft())
        self.ui.close.move((QDesktopWidget().width())-60, 10)
        
        ## SHOW ==> MAIN WINDOW ##
        self.show()
        self.update()
        ## ==> END ##

    # callback mqtt
    def mqttQuality(self, msg):
        print(msg)
        badQuality = {'MINOR','MAJOR','CRITICAL'}
        msgSplit = msg.split()
        catId = msgSplit[1]
        catQuality = msgSplit[0]
        
        if catQuality in badQuality:
            GPIO.output(servo,GPIO.LOW)                        
        elif catQuality == 'GOOD':
            pass            
    
    # counter callback
    def runCounter(self, value):
        global reject, good, quality
        
        if value == 1 :
            self.Prox1()
        elif value == 2 :
            self.Prox2()
        else:
            pass
        
    # callback sensor untuk counter good   
    def Prox1(self):
        global proximity1, servo, quality, good, reject
        
        if GPIO.input(proximity1) == 0:           
            good += 1
            self.cat_good()
            self.blink_widget(1)  
        elif GPIO.input(proximity1) == 1:
            self.blink_widget(0)
            
    # callback sensor untuk counter reject
    def Prox2(self):
        global proximity2, servo, reject
        
        if GPIO.input(proximity2) == 0:
            reject += 1
            self.cat_reject()
            self.blink_widget(2)            
        elif GPIO.input(proximity2) == 1:
            self.blink_widget(0)
            
        GPIO.output(servo,GPIO.HIGH)
    
    # pengaturan radius gauge
    def gauge_radius(self, max, std, current):
        
        if current > max:
            current = current % max
            
        value = 1 - (current * std)
        stop_1 = str(value - 0.001)
        stop_2 = str(value)        
        return stop_1, stop_2

    # counter good
    def cat_good(self):
        global good, maxGauge, Cat_val_blue   
        x = good
        
        if x > maxGauge:
            x = x % maxGauge

        # perubahan counter dan gauge good
        denomed = f"{x:,}"
        denomed = denomed.replace(",",".")        
        htmlText = """<html><head/><body><p><span style=\" color:#0078ff;\">{VALUE}</span></p></body></html>"""
        newHtml = htmlText.replace("{VALUE}", denomed)
        self.ui.CounterInt.setText(newHtml) 
        styleSheet = """
        QFrame{
            border-radius: 150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:{STOP_1} rgba(0, 0, 0, 0), stop:{STOP_2} rgb(0, 175, 255));
        }
        """
        radBlue, baserad = self.gauge_radius(maxGauge, Cat_val_blue, good)        
        newStylesheet = styleSheet.replace("{STOP_1}", radBlue).replace("{STOP_2}", baserad)
        self.ui.GaugeMeter.setStyleSheet(newStylesheet)
        
        # perubahan counter good total
        denomed_total = f"{good:,}"
        denomed_total = denomed_total.replace(",",".")
        htmlText = """<html><head/><body><p>{VALUE}</p></body></html>"""
        newHtml = htmlText.replace("{VALUE}", denomed_total)
        self.ui.TargetLabel_2.setText(newHtml)
        
    # counter reject
    def cat_reject(self):
        global reject, maxGaugeR, Cat_val_red 

        # perubahan counter dan gauge reject
        denomed = f"{reject:,}"
        denomed = denomed.replace(",",".")
        htmlText = """<html><head/><body><p><span style=\" color:#f00000;\">{VALUE}</span></p></body></html>"""
        newHtml = htmlText.replace("{VALUE}", denomed)
        self.ui.Counter.setText(newHtml)
        styleSheet = """
        QFrame{
            border-radius: 150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:{STOP_1} rgba(0, 0, 0, 0), stop:{STOP_2} rgb(255, 50, 0));
        }
        """
        radRed, baserad = self.gauge_radius(maxGaugeR, Cat_val_red, reject)        
        newStylesheet = styleSheet.replace("{STOP_1}", radRed).replace("{STOP_2}", baserad)
        self.ui.GaugeMeterR.setStyleSheet(newStylesheet)
    
    # pengaturan blink widget
    def blink_widget(self, indicator):
        if indicator == 1:
            
            styleSheet = """
            QFrame{
                border-radius:135;
                background-color: rgb(0, 120, 255)
            }
            """
            self.ui.Interface.setStyleSheet(styleSheet)
            
        elif indicator == 2:
            styleSheetR = """
            QFrame{
                border-radius:135;
                background-color: rgb(175, 0, 0)
            }
            """
            self.ui.InterfaceR.setStyleSheet(styleSheetR)
            
        elif indicator == 0:
            styleSheet = """
            QFrame{
                border-radius:135;
                background-color: rgb(77, 77, 127)
            }
            """
            self.ui.Interface.setStyleSheet(styleSheet)
            self.ui.InterfaceR.setStyleSheet(styleSheet)
            
        
    
    # callback tombol start dan memulai threading
    def Start(self):
        global msg  
        
        if self.ui.pushButton.isChecked():
            
            self.qualityThread = mqttThread()
            self.qualityThread.mqttSignal.connect(self.mqttQuality)
            self.qualityThread.mqttFinished.connect(self.qualityThread.destroy)
            self.qualityThread.start()

            self.countThread = RelayThread()
            self.countThread.event_detected.connect(self.runCounter)
            self.countThread.threadFinished.connect(self.countThread.destroy)
            self.countThread.start()
                
            htmlText = """STOP"""
            self.ui.pushButton.setText(htmlText)
        
        else:
            
            print("stop jalan")
            self.countThread.threadFinished.emit()
            self.qualityThread.mqttFinished.emit()
                
            htmlText = """START"""
            self.blink_widget(0)
            self.ui.pushButton.setText(htmlText)
            
    # callback tombol reset
    def Reset(self):
        global good, reject
        good = reject = 0

        self.cat_reject()
        self.cat_good()
        
    # callback tombol "x"
    def Close(self, event):
        close = QMessageBox.question(self, 'EXIT', "Apakah Anda Yakin Untuk Keluar?", QMessageBox.No | QMessageBox.Yes)
        if close == QMessageBox.Yes:
            self.close()
        else:
            pass
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Gauge()
    sys.exit(app.exec_())