# -*- coding:utf8 -*-

import sys

from socket import *
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore,QtTest
from ui_teklif import Ui_Dialog

from modulemdb import *


pdfmetrics.registerFont(TTFont('tahoma', 'tahoma.ttf'))

class Teklif(QtGui.QDialog , Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.myddb=Myddb()
        self.comboBox.currentIndexChanged.connect(self.c1degisti)
        self.comboBox_2.currentIndexChanged.connect(self.c2degisti)

        bul = self.myddb.cur.execute("select distinct type from nen.products ")
        bul1 = self.myddb.cur.fetchall()

        for item in bul1:
            self.comboBox.addItem(item[0])

    def combodoldur(self):
        bul=self.myddb.cur.execute("select distinct type from nen.products ")
        bul1=self.myddb.cur.fetchall()

        for item in bul1:
            self.comboBox.addItem(item[0])


    def c1degisti(self):
        self.comboBox_2.clear()
        a=self.comboBox.currentText()
        bul=self.myddb.cur.execute("select code from nen.products where type=%s",[a])
        bul1=self.myddb.cur.fetchall()

        for item in bul1:
            self.comboBox_2.addItem(item[0])

    def c2degisti(self):
        a=self.comboBox_2.currentText()
        elma="./images/"+ a+".png"
        pic = QtGui.QPixmap(elma)
        self.label.setPixmap(pic)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setScaledContents(True)
        self.label.setMinimumSize(1, 1)
        bul = self.myddb.cur.execute("select size from nen.products where code=%s", [a])
        bul1 = self.myddb.cur.fetchall()
        self.label_8.setText("Size : "+(bul1[0][0]))




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    fatura1=Teklif()
    fatura1.show()
    fatura1.raise_()

    app.exec_()
    print "teklif kapandı"
