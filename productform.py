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
        body = {'getData': "product", 'productId': idP}
        api = ApiControler({'getData': "product", 'productId': idP})
        for productLoaded in api.getResponse():
            self.setWindowTitle(productLoaded['name'])
            self.show()
            lab = QLabel(productLoaded['description_long'])
            lab.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            lab.setTextFormat(Qt.RichText)
            lab.setWordWrap(1)
            views = [self.product.picView1, self.product.picView2, self.product.picView3]
            self.appendProductsImages(views, productLoaded['pic'])
            self.product.productDescription.setWidget(lab)
            self.product.productName.setText(productLoaded['name'])

    def appendProductsImages(self, views, mainPath):
        for i in range(3):
            views[i].setPixmap(QtGui.QPixmap(mainPath + str(i+1)))
            views[i].setStyleSheet("border: 1px solid black")
            views[i].setScaledContents(True)

    def closeDialog(self):
        self.product.picView1.deleteLater()
        self.product.picView2.deleteLater()
        self.product.picView3.deleteLater()
        self.close()