from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.uic import *
from functools import partial
from product import Ui_productDialog
class productDialog(QDialog):
    def __init__(self, parent=None):
        super(productDialog, self).__init__(parent)
        self.createProduct()

    def createProduct(self):
        self.product = Ui_productDialog()
        self.product.setupUi(self)
        self.show()
    def closeDialog(self):
        self.close()