#-------------------------------------------------------------------------------
# Name:        userinterface
# Purpose:     GUI
#
# Author:      Merchelski Patryk
#
# Created:     18.09.2018
# Copyright:   (c) Merchelski Patryk 2018
# Licence:
#-------------------------------------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.uic import *
from functools import partial
from gui import Ui_MainWindow
from productform import productDialog
class InterfaceWindow(QMainWindow):
    product = None
    newsContentTab = []
    def __init__(self, parent=None):
        super(InterfaceWindow, self).__init__(parent)
        self.createInterface()

    def createInterface(self):
        #loadUi("gui.ui", self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.newsHeader.setStyleSheet('background-color: #dbdbdb; border: 1px solid black; font: bold; font-family: Calibri, Verdana, Arial, sans-serif; font-size: 18px;')

    def createNewsList(self):
        import urllib.request
        import json
        body = {'getData': "newsHeaders"}
        myurl = "http://localhost/pythonAPI/api.php"
        req = urllib.request.Request(myurl)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')
        req.add_header('Content-Length', len(jsondataasbytes))
        response = urllib.request.urlopen(req, jsondataasbytes)
        data = response.read()
        encoding = response.info().get_content_charset('utf-8')
        items = []
        for itm in json.loads(data.decode(encoding)):
            items.append(itm['header'])
            self.newsContentTab.append(str(itm['content']))
        self.ui.listNews.addItems(items)

    def initializeEvents(self):
        self.ui.exitProgram.triggered.connect(self.exitApp)
       # self.ui.exitProgram.triggered.connect(productDialog(self.product).closeDialog)
       # self.listNews.itemClicked.connect(partial(self.clickedNews))
       # self.listNews.itemEntered.connect(Partial(self.clickedNews))
        self.ui.listNews.currentItemChanged.connect(partial(self.clickedNews))

    def clickedNews(self, item):
        lab = QLabel(self.newsContentTab[self.ui.listNews.currentRow()])
        lab.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        lab.setTextFormat(Qt.RichText)
        lab.setWordWrap(1)
        self.ui.newsHeader.setText(QListWidgetItem(item).text())
        self.ui.newsHeader.setStyleSheet('background-color: #dbdbdb; border: 1px solid black; font: bold; font-family: Calibri, Verdana, Arial, sans-serif; font-size: 18px;')
        self.ui.newsContent.setWidget(lab)

    def createCategories(self):
        category_layout = QVBoxLayout()
        import urllib.request
        import json
        body = {'getData': "categories"}
        myurl = "http://localhost/pythonAPI/api.php"
        req = urllib.request.Request(myurl)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')
        req.add_header('Content-Length', len(jsondataasbytes))
        response = urllib.request.urlopen(req, jsondataasbytes)
        data = response.read()
        encoding = response.info().get_content_charset('utf-8')
        buttons = []
        for category in json.loads(data.decode(encoding)):
            width = 191
            buttons.append([QPushButton(category['name']), category['id'], width, category['subcategory']])
            style = []
            style.append("#d1d1d1;") #background-color [0]
            style.append("1px solid black;") #border [1]
            style.append("10px;") #border-radius [2]
            style.append("Calibri, Verdana, Arial, sans-serif;") #font-family [3]
            style.append("bold;") #font [4]
            style.append(18) #font-size [5]
            style.append("#f2f2f2;") #background-color :hover [6]
            style.append("2px inset gray;") #border :pressed [7]
            buttons[-1][0].setMinimumSize(QSize(width, 33))
            buttons[-1][0].setMaximumSize(QSize(width, 33))
            buttons[-1][0].setStyleSheet('QPushButton' +
            '{' +
           	'background-color: ' + style[0] +
            'border: ' + style[1] +
            'border-radius: ' + style[2] +
            'font-family: ' + style[3] +
            'font: ' + style[4] +
            'font-size: ' + str(style[5]) + 'px;' +
            '}' +
            'QPushButton:hover' +
            '{' +
            'background-color: ' + style[6] +
            '}' +
            'QPushButton:pressed' +
            '{' +
            'border: '+ style[7] +
            '}')
            buttons[-1][0].clicked.connect(partial(self.clickedCategory, buttons[-1][1]))
            category_layout.addWidget(buttons[-1][0])
            category_layout.setAlignment(buttons[-1][0], Qt.AlignRight)
            if buttons[-1][3] != 0:
                width_sub = width - 15
                ##obsługa subcategorii
                for subcategory in category['subcategory']:
                    buttons.append([QPushButton(subcategory['name']), subcategory['id'], width_sub, subcategory['subcategory']])
                    style[0] = "#e6e6e6;" #background-color [0]
                    style[4] = "normal;" #font [4]
                    style[5] = 16 #font-size [5]
                    buttons[-1][0].setMinimumSize(QSize(width_sub, 33))
                    buttons[-1][0].setMaximumSize(QSize(width_sub, 33))
                    buttons[-1][0].setStyleSheet('QPushButton' +
                    '{' +
                   	'background-color: ' + style[0] +
                    'border: ' + style[1] +
                    'border-radius: ' + style[2] +
                    'font-family: ' + style[3] +
                    'font: ' + style[4] +
                    'font-size: ' + str(style[5]) + 'px;' +
                    '}' +
                    'QPushButton:hover' +
                    '{' +
                    'background-color: ' + style[6] +
                    '}' +
                    'QPushButton:pressed' +
                    '{' +
                    'border: '+ style[7] +
                    '}')
                    category_layout.addWidget(buttons[-1][0])
                    category_layout.setAlignment(buttons[-1][0], Qt.AlignRight)
                    buttons[-1][0].clicked.connect(partial(self.clickedCategory, buttons[-1][1]))
                    if buttons[-1][3] != 0:
                        width_sub2 = width_sub - 15
                        ##obsluga subsubcategorii
                        for subsubcategory in subcategory['subcategory']:
                            buttons.append([QPushButton(subsubcategory['name']), subsubcategory['id'], width_sub2, 0])
                            style[4] = "italic;" #font [4]
                            style[5] = 14 #font-size [5]
                            buttons[-1][0].setMinimumSize(QSize(width_sub2, 33))
                            buttons[-1][0].setMaximumSize(QSize(width_sub2, 33))
                            buttons[-1][0].setStyleSheet('QPushButton' +
                            '{' +
                           	'background-color: ' + style[0] +
                            'border: ' + style[1] +
                            'border-radius: ' + style[2] +
                            'font-family: ' + style[3] +
                            'font: ' + style[4] +
                            'font-size: ' + str(style[5]) + 'px;' +
                            '}' +
                            'QPushButton:hover' +
                            '{' +
                            'background-color: ' + style[6] +
                            '}' +
                            'QPushButton:pressed' +
                            '{' +
                            'border: '+ style[7] +
                            '}')
                            category_layout.addWidget(buttons[-1][0])
                            category_layout.setAlignment(buttons[-1][0], Qt.AlignRight)
                            buttons[-1][0].clicked.connect(partial(self.clickedCategory, buttons[-1][1]))

        self.ui.categoriesFrame.setLayout(category_layout)
        category_layout.setAlignment(Qt.AlignTop)

    productsToDisplay = []
    products_layout = QGridLayout()
    def clickedCategory(self, category):
        self.createProducts(category)

    def createProducts(self, category):
        import sip
        clearTab = False
        for product in self.productsToDisplay:
            if(product[0] != None):
                product[0].deleteLater()
                product[0] = None
                product[1].deleteLater()
                product[1] = None
                product[2].deleteLater()
                product[2] = None
                clearTab = True
                if(self.products_layout != None):
                    for i in reversed(range(self.products_layout.count())):
                        self.products_layout.itemAt(i).widget().deleteLater()
        if(clearTab):
            self.productsToDisplay = []
        import urllib.request
        import json
        self.products_layout.setColumnStretch(0, 2)
        self.products_layout.setColumnStretch(1, 3)
        self.products_layout.setColumnStretch(2, 3)
        body = {'getData': "products", 'category': category}
        myurl = "http://localhost/pythonAPI/api.php"
        req = urllib.request.Request(myurl)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')
        req.add_header('Content-Length', len(jsondataasbytes))
        response = urllib.request.urlopen(req, jsondataasbytes)
        data = response.read()
        encoding = response.info().get_content_charset('utf-8')
        x = 5
        y = 5
        picWidth = 221
        picHeigth = 221
        i = 1
        row = 0
        for product in json.loads(data.decode(encoding)):
            newProduct = int(product['new'])
            promProduct = int(product['prom'])
            self.productsToDisplay.append([QtWidgets.QLabel(), QtWidgets.QLabel(), QtWidgets.QPushButton()])
            self.productsToDisplay[-1][0].setMaximumSize(QSize(picWidth, picHeigth))
            self.productsToDisplay[-1][0].setGeometry(QtCore.QRect(x, y, picWidth, picHeigth))
            self.productsToDisplay[-1][0].setTextFormat(Qt.RichText)
            if(newProduct == 1):
                self.productsToDisplay[-1][0].setPixmap(QtGui.QPixmap(product['pic'] + "new"))
            elif(promProduct == 1):
                self.productsToDisplay[-1][0].setPixmap(QtGui.QPixmap(product['pic'] + "prom"))
            else:
                self.productsToDisplay[-1][0].setPixmap(QtGui.QPixmap(product['pic']))
            self.productsToDisplay[-1][0].setScaledContents(True)
            self.productsToDisplay[-1][0].setObjectName("image"+str(product['id']))
            self.productsToDisplay[-1][0].setStyleSheet("border: 1px solid black")

            self.productsToDisplay[-1][1].setGeometry(QtCore.QRect(x, y, picWidth, picHeigth-20))
            self.productsToDisplay[-1][1].setMaximumSize(QSize(picWidth, picHeigth-20))
            self.productsToDisplay[-1][1].setTextFormat(Qt.RichText)
            self.productsToDisplay[-1][1].setWordWrap(1)
            self.productsToDisplay[-1][1].setText(product['description'])
            self.productsToDisplay[-1][1].setObjectName("imagelabel"+str(product['id']))
            self.productsToDisplay[-1][1].setStyleSheet("font: italic; font-size: 12px")
            self.productsToDisplay[-1][1].setAlignment(Qt.AlignCenter)

            self.productsToDisplay[-1][2].setGeometry(QtCore.QRect(x, y, picWidth, 120))
            self.productsToDisplay[-1][2].setMaximumSize(QSize(picWidth, 120))
            self.productsToDisplay[-1][2].setText(product['name'] +"\n\n"+ product['priceBrutto'] +"zł brutto\n\nZOBACZ KARTĘ PRODUKTU")
            self.productsToDisplay[-1][2].setObjectName("imagelabel"+str(product['id']))
            self.productsToDisplay[-1][2].setStyleSheet("QPushButton {font: bold; font-size: 12px; text-align: center} QPushButton:hover {color: red} ")
            self.productsToDisplay[-1][2].clicked.connect(partial(self.clickedProduct, product['id']))

            self.products_layout.addWidget(self.productsToDisplay[-1][0])
            self.products_layout.addWidget(self.productsToDisplay[-1][1])
            self.products_layout.addWidget(self.productsToDisplay[-1][2])
            x = x+picWidth+10
            if(i == 3):
                i = 0
                y = y+picHeigth+80
                x = 5
            i = i+1
        self.ui.scrollAreaWidgetContents_2.setLayout(self.products_layout)

    def clickedProduct(self, idP):
        self.product = productDialog(idP, self)
    def exitApp(self):
        if self.product != None:
            self.product.closeDialog()
        self.product = None
        self.close()
