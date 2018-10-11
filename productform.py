from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.uic import *
from functools import partial
from product import Ui_productDialog
from apicontroler import ApiControler
class productDialog(QDialog):
    def __init__(self, idP, parent=None):
        super(productDialog, self).__init__(parent)
        self.createProduct(idP)

    def createProduct(self, idP):
        self.product = Ui_productDialog()
        self.product.setupUi(self)

        import urllib.request
        import json
        body = {'getData': "product", 'productId': idP}
        api = ApiControler({'getData': "product", 'productId': idP})
        for productLoaded in api.getResponse():
            self.setWindowTitle(productLoaded['name'])
            self.show()
            lab = QLabel(productLoaded['description_long'])
            lab.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            lab.setTextFormat(Qt.RichText)
            lab.setWordWrap(1)
            self.product.picView1.setPixmap(QtGui.QPixmap(productLoaded['pic']))
            self.product.picView1.setStyleSheet("border: 1px solid black")
            self.product.picView1.setScaledContents(True)
            self.product.picView2.setPixmap(QtGui.QPixmap(productLoaded['pic'] + "new"))
            self.product.picView2.setStyleSheet("border: 1px solid black")
            self.product.picView2.setScaledContents(True)
            self.product.picView3.setPixmap(QtGui.QPixmap(productLoaded['pic'] + "prom"))
            self.product.picView3.setStyleSheet("border: 1px solid black")
            self.product.picView3.setScaledContents(True)
            self.product.productDescription.setWidget(lab)

    def closeDialog(self):
        self.product.picView1.deleteLater()
        self.product.picView2.deleteLater()
        self.product.picView3.deleteLater()
        self.close()