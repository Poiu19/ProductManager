from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5.uic import *
from functools import partial
from gui import Ui_MainWindow
from productform import productDialog
from apicontroler import ApiControler
from manager import KAW01
from timer import RepeatEvent
class ProductDetails():
    productId = None
    forceLoad = False
    def setId(self, id):
        self.productId = id

    def loadProduct(self):
        api = ApiControler({'getData': "productEditDetails", 'productId': str(self.productId)})
        for product in api.getResponse():
            if(product['code'] == "KAW01"):
                self.product = KAW01(int(product['color']))
                self.forceLoad = True

class InterfaceWindow(QMainWindow):
    product = None
    newsContentTab = []
    productsToDisplay = []
    products_layout = QGridLayout()
    productInEditPanel = None
    repeatAbleEvents = []
    def __init__(self, parent=None):
        super(InterfaceWindow, self).__init__(parent)
        self.createInterface()
        self.productInEditPanel = ProductDetails()

    def createInterface(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.newsHeader.setStyleSheet('background-color: #dbdbdb; border: 1px solid black; font: bold; font-family: Calibri, Verdana, Arial, sans-serif; font-size: 18px;')

    def createNewsList(self):
        items = []
        api = ApiControler({'getData': "newsHeaders"})
        for itm in api.getResponse():
            items.append(itm['header'])
            self.newsContentTab.append(str(itm['content']))
        self.ui.listNews.addItems(items)

    def initializeEvents(self):
        self.ui.exitProgram.triggered.connect(self.exitApp)
        self.ui.listNews.currentItemChanged.connect(partial(self.clickedNews))
        self.ui.acceptNewDim.clicked.connect(self.acceptDim)
        self.repeatAbleEvents.append(RepeatEvent(1.0, self.loadManager))

    def clickedNews(self, item):
        lab = QLabel(self.newsContentTab[self.ui.listNews.currentRow()])
        lab.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        lab.setTextFormat(Qt.RichText)
        lab.setWordWrap(1)
        self.ui.newsHeader.setText(QListWidgetItem(item).text())
        self.ui.newsHeader.setStyleSheet('background-color: #dbdbdb; border: 1px solid black; font: bold; font-family: Calibri, Verdana, Arial, sans-serif; font-size: 18px;')
        self.ui.newsContent.setWidget(lab)

    def loadManager(self):
        if(self.productInEditPanel.productId != None and self.productInEditPanel.forceLoad == True):
            self.ui.lengthBox.setText(str(self.productInEditPanel.product.getLength()))
            self.ui.widthBox.setText(str(self.productInEditPanel.product.getWidth()))
            self.ui.heigthBox.setText(str(self.productInEditPanel.product.getHeigth()))
            self.productInEditPanel.forceLoad = False
            print(str(self.productInEditPanel.productId))

    def acceptDim(self):
        if(self.productInEditPanel.productId != None):
            errorHandler = self.productInEditPanel.product.changeLength(int(self.ui.lengthBox.displayText()))
            if errorHandler != True:
                self.ui.lengthBox.setText(str(self.productInEditPanel.product.getLength()))
                print (errorHandler)
            errorHandler = self.productInEditPanel.product.changeWidth(int(self.ui.widthBox.displayText()))
            if errorHandler != True:
                self.ui.widthBox.setText(str(self.productInEditPanel.product.getWidth()))
                print (errorHandler)
            errorHandler = self.productInEditPanel.product.changeHeigth(int(self.ui.heigthBox.displayText()))
            if errorHandler != True:
                self.ui.heigthBox.setText(str(self.productInEditPanel.product.getHeigth()))
                print (errorHandler)
            self.productInEditPanel.product.printFormsDimensions()

    def createCategories(self):
        category_layout = QVBoxLayout()
        buttons = []
        api = ApiControler({'getData': "categories"})
        for category in api.getResponse():
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
            self.setStyleForCategoryButton(style, buttons, width)
            self.setCategoryButtonToLayout(buttons, category_layout)
            if buttons[-1][3] != 0:
                width_sub = width - 15
                ##obsługa subcategorii
                for subcategory in category['subcategory']:
                    buttons.append([QPushButton(subcategory['name']), subcategory['id'], width_sub, subcategory['subcategory']])
                    style[0] = "#e6e6e6;" #background-color [0]
                    style[4] = "normal;" #font [4]
                    style[5] = 16 #font-size [5]
                    self.setStyleForCategoryButton(style, buttons, width_sub)
                    self.setCategoryButtonToLayout(buttons, category_layout)
                    if buttons[-1][3] != 0:
                        width_sub2 = width_sub - 15
                        ##obsluga subsubcategorii
                        for subsubcategory in subcategory['subcategory']:
                            buttons.append([QPushButton(subsubcategory['name']), subsubcategory['id'], width_sub2, 0])
                            style[4] = "italic;" #font [4]
                            style[5] = 14 #font-size [5]
                            self.setStyleForCategoryButton(style, buttons, width_sub2)
                            self.setCategoryButtonToLayout(buttons, category_layout)
        self.ui.categoriesFrame.setLayout(category_layout)
        category_layout.setAlignment(Qt.AlignTop)

    def setStyleForCategoryButton(self, style, buttons, width):
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

    def setCategoryButtonToLayout(self, buttons, category_layout):
        buttons[-1][0].clicked.connect(partial(self.clickedCategory, buttons[-1][1]))
        category_layout.addWidget(buttons[-1][0])
        category_layout.setAlignment(buttons[-1][0], Qt.AlignRight)

    def clickedCategory(self, category):
        self.createProducts(category)

    def createProducts(self, category):
        picWidth = 221
        picHeigth = 221
        self.clearProductTab()
        self.setProductColumnStretch(2, 3, 3) #proportion
        api = ApiControler({'getData': "products", 'category': category})
        for product in api.getResponse():
            self.productsToDisplay.append([QtWidgets.QLabel(), QtWidgets.QLabel(), QtWidgets.QPushButton()])
            self.setProductDetails(product, picWidth, picHeigth)
            self.addProductsToLayout()
        self.ui.scrollAreaWidgetContents_2.setLayout(self.products_layout)

    def setProductDetails(self, product, width, heigth):
        self.setProductPic(product, width, heigth)
        self.setProductDescription(product, width, heigth)
        self.setProductViewButton(product, width, heigth)

    def clearProductTab(self):
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

    def setProductColumnStretch(self, col1, col2, col3):
        self.products_layout.setColumnStretch(0, col1)
        self.products_layout.setColumnStretch(1, col2)
        self.products_layout.setColumnStretch(2, col3)

    def setProductPic(self, product, picWidth, picHeigth):
        newProduct = int(product['new'])
        promProduct = int(product['prom'])
        self.productsToDisplay[-1][0].setMaximumSize(QSize(picWidth, picHeigth))
        self.productsToDisplay[-1][0].setTextFormat(Qt.RichText)
        if(newProduct == 1):
            self.productsToDisplay[-1][0].setPixmap(QtGui.QPixmap(product['pic'] + "new"))
        elif(promProduct == 1):
            self.productsToDisplay[-1][0].setPixmap(QtGui.QPixmap(product['pic'] + "prom"))
        else:
            self.productsToDisplay[-1][0].setPixmap(QtGui.QPixmap(product['pic'] + str(1)))
        self.productsToDisplay[-1][0].setScaledContents(True)
        self.productsToDisplay[-1][0].setObjectName("image"+str(product['id']))
        self.productsToDisplay[-1][0].setStyleSheet("border: 1px solid black")

    def setProductDescription(self, product, picWidth, picHeigth):
        self.productsToDisplay[-1][1].setMaximumSize(QSize(picWidth, picHeigth-20))
        self.productsToDisplay[-1][1].setTextFormat(Qt.RichText)
        self.productsToDisplay[-1][1].setWordWrap(1)
        self.productsToDisplay[-1][1].setText(product['description'])
        self.productsToDisplay[-1][1].setObjectName("imagelabel"+str(product['id']))
        self.productsToDisplay[-1][1].setStyleSheet("font: italic; font-size: 12px")
        self.productsToDisplay[-1][1].setAlignment(Qt.AlignCenter)

    def setProductViewButton(self, product, picWidth, picHeigth):
        self.productsToDisplay[-1][2].setMaximumSize(QSize(picWidth, 120))
        self.productsToDisplay[-1][2].setText(product['name'] +"\n\n"+ product['priceBrutto'] +"zł brutto\n\nZOBACZ KARTĘ PRODUKTU")
        self.productsToDisplay[-1][2].setObjectName("imagelabel"+str(product['id']))
        self.productsToDisplay[-1][2].setStyleSheet("QPushButton {font: bold; font-size: 12px; text-align: center} QPushButton:hover {color: red} ")
        self.productsToDisplay[-1][2].clicked.connect(partial(self.clickedProduct, product['id']))

    def addProductsToLayout(self):
        self.products_layout.addWidget(self.productsToDisplay[-1][0])
        self.products_layout.addWidget(self.productsToDisplay[-1][1])
        self.products_layout.addWidget(self.productsToDisplay[-1][2])

    def destroyChildProduct(self):
        if self.product != None:
            self.product.closeDialog()
            self.product = None

    def clickedProduct(self, idP):
        self.destroyChildProduct()
        self.product = productDialog(idP, self.productInEditPanel, self)

    def exitApp(self):
        for event in self.repeatAbleEvents:
            event.stop()
        self.destroyChildProduct()
        self.close()
