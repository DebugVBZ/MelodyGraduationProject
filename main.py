from PyQt5 import QtWidgets
from multiprocessing import Process, Manager, freeze_support
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QDesktopWidget,QVBoxLayout,QHBoxLayout,QComboBox,QTextBrowser,QTextEdit,QLabel,QDialog,QFileDialog,QLineEdit,QMessageBox
from PyQt5.QtCore import QCoreApplication,QThread
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtGui import QPixmap

import cv2
import sys
import os


class ImageProcessUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.algorithm=''
        self.setGeometry(40,40,800,600)
        #语言选择下拉框决定数据库表名及语料库读取
        self.languagelCombo=QComboBox(self,minimumWidth=200) # 语言下拉框
        self.picture = None

        self.languagelCombo.addItem('均值模糊')
        self.languagelCombo.addItem('高斯模糊')
        self.languagelCombo.addItem('均值滤波')
        self.languagelCombo.addItem('双边滤波')
        self.languagelCombo.addItem('2D卷积')
        self.sttcrabt=QPushButton('模糊图片',self)
        self.clearButton = QPushButton(self,minimumWidth=200)
        self.clearButton.setText("清空图片")
        self.clearButton.clicked.connect(self.clearButtonFunc)
        self.labels = QLabel()
        self.importButton = QPushButton(self,minimumWidth=200)
        self.importButton.setText("导入图片")
        self.importButton.clicked.connect(self.loadFile)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.languagelCombo)
        hbox.addWidget(self.sttcrabt)
        hbox.addWidget(self.clearButton)
        hbox.addWidget(self.importButton)
        hbox.addWidget(self.labels)
        self.setLayout(hbox)
    def clearButtonFunc(self):
        self.sttcrabt.setEnabled(False)
        self.labels.setPixmap(QPixmap())
    def loadFile(self):
        print("load--file")
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', './', 'Image files(*.jpg *.gif *.png)')
        print(fname)
        qpixmap = QPixmap(fname)
        self.picture = qpixmap.toImage
        self.labels.setPixmap(QPixmap(fname))
 

if __name__ == "__main__":

    app=QApplication(sys.argv)
    ex=ImageProcessUI()
    ex.show()
    sys.exit(app.exec_())
