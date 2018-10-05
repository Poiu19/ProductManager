# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        MainWindow.setToolTipDuration(-1)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #dbdbdb")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, -1, 1031, 731))
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"border: 1px solid black;\n"
"padding: 10px;\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"margin-right: 1px;\n"
"margin-top: 1px;\n"
"min-height: 20px;\n"
"background-color: #dbdbdb;\n"
"    font-family: Calibri, Verdana, Arial, sans-serif;\n"
"    font-size: 18px;\n"
"min-width: 40ex;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"border-color: #9B9B9B;\n"
"border-bottom-color: #CC2C7CB;\n"
"font: bold;\n"
"background-color: #cecece;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 2px;\n"
"}")
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabInfo = QtWidgets.QWidget()
        self.tabInfo.setObjectName("tabInfo")
        self.newsContent = QtWidgets.QScrollArea(self.tabInfo)
        self.newsContent.setGeometry(QtCore.QRect(280, 50, 741, 621))
        self.newsContent.setMouseTracking(True)
        self.newsContent.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.newsContent.setToolTipDuration(100)
        self.newsContent.setStyleSheet("    background-color: #dbdbdb;\n"
"    font-family: Calibri, Verdana, Arial, sans-serif;\n"
"    font-size: 18px;\n"
"    vertical-align: top;\n"
"    text-align: left;")
        self.newsContent.setLineWidth(1)
        self.newsContent.setMidLineWidth(0)
        self.newsContent.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.newsContent.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.newsContent.setWidgetResizable(True)
        self.newsContent.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.newsContent.setObjectName("newsContent")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 722, 619))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.newsContent.setWidget(self.scrollAreaWidgetContents)
        self.listNews = QtWidgets.QListWidget(self.tabInfo)
        self.listNews.setGeometry(QtCore.QRect(10, 10, 256, 661))
        font = QtGui.QFont()
        font.setFamily("Calibri,Verdana,Arial,sans-serif")
        font.setPointSize(-1)
        self.listNews.setFont(font)
        self.listNews.setMouseTracking(True)
        self.listNews.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.listNews.setStyleSheet("    background-color: #dbdbdb;\n"
"    border: 1px solid black;\n"
"    font-family: Calibri, Verdana, Arial, sans-serif;\n"
"    font-size: 18px;")
        self.listNews.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listNews.setProperty("showDropIndicator", False)
        self.listNews.setObjectName("listNews")
        self.newsHeader = QtWidgets.QLabel(self.tabInfo)
        self.newsHeader.setGeometry(QtCore.QRect(280, 10, 741, 31))
        self.newsHeader.setToolTipDuration(1)
        self.newsHeader.setStyleSheet("QLabel#labelTitle {\n"
"    background-color: #dbdbdb;\n"
"    border: 1px solid black;\n"
"    font-family: Calibri, Verdana, Arial, sans-serif;\n"
"    font-size: 18px;\n"
"\n"
"}")
        self.newsHeader.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
        self.newsHeader.setText("")
        self.newsHeader.setTextFormat(QtCore.Qt.RichText)
        self.newsHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.newsHeader.setWordWrap(False)
        self.newsHeader.setObjectName("newsHeader")
        self.tabWidget.addTab(self.tabInfo, "")
        self.tabProducts = QtWidgets.QWidget()
        self.tabProducts.setObjectName("tabProducts")
        self.categoriesFrame = QtWidgets.QFrame(self.tabProducts)
        self.categoriesFrame.setGeometry(QtCore.QRect(10, 10, 211, 661))
        self.categoriesFrame.setStyleSheet("background-color: #dbdbdb; border: 1px solid black; border-radius: 20px;")
        self.categoriesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.categoriesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.categoriesFrame.setObjectName("categoriesFrame")
        self.productCatalog = QtWidgets.QScrollArea(self.tabProducts)
        self.productCatalog.setGeometry(QtCore.QRect(240, 10, 781, 661))
        self.productCatalog.setMouseTracking(True)
        self.productCatalog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.productCatalog.setToolTipDuration(100)
        self.productCatalog.setStyleSheet("    background-color: #dbdbdb;\n"
"    font-family: Calibri, Verdana, Arial, sans-serif;\n"
"    font-size: 18px;\n"
"    vertical-align: top;\n"
"    text-align: left;")
        self.productCatalog.setLineWidth(1)
        self.productCatalog.setMidLineWidth(0)
        self.productCatalog.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.productCatalog.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.productCatalog.setWidgetResizable(True)
        self.productCatalog.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.productCatalog.setObjectName("productCatalog")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 762, 659))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.productCatalog.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tabProducts, "")
        self.tabConfig = QtWidgets.QWidget()
        self.tabConfig.setObjectName("tabConfig")
        self.tabWidget.addTab(self.tabConfig, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 23))
        self.menubar.setStyleSheet("background-color: #cccccc; border: 1px solid black")
        self.menubar.setObjectName("menubar")
        self.menuPlik = QtWidgets.QMenu(self.menubar)
        self.menuPlik.setStyleSheet("background-color: #cccccc; border: 1px solid black")
        self.menuPlik.setObjectName("menuPlik")
        self.menuO_programie = QtWidgets.QMenu(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuO_programie.sizePolicy().hasHeightForWidth())
        self.menuO_programie.setSizePolicy(sizePolicy)
        self.menuO_programie.setMaximumSize(QtCore.QSize(16777215, 16777211))
        self.menuO_programie.setToolTip("")
        self.menuO_programie.setToolTipDuration(-1)
        self.menuO_programie.setAutoFillBackground(False)
        self.menuO_programie.setStyleSheet("background-color: #cccccc; border: 1px solid black")
        self.menuO_programie.setObjectName("menuO_programie")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exitProgram = QtWidgets.QAction(MainWindow)
        self.exitProgram.setCheckable(False)
        font = QtGui.QFont()
        self.exitProgram.setFont(font)
        self.exitProgram.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.exitProgram.setAutoRepeat(False)
        self.exitProgram.setMenuRole(QtWidgets.QAction.QuitRole)
        self.exitProgram.setIconVisibleInMenu(False)
        self.exitProgram.setPriority(QtWidgets.QAction.HighPriority)
        self.exitProgram.setObjectName("exitProgram")
        self.menuPlik.addAction(self.exitProgram)
        self.menubar.addAction(self.menuPlik.menuAction())
        self.menubar.addAction(self.menuO_programie.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.listNews)
        MainWindow.setTabOrder(self.listNews, self.newsContent)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cut It"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInfo), _translate("MainWindow", "Nowości"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProducts), _translate("MainWindow", "Katalog Produktów"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfig), _translate("MainWindow", "Konfigurator zamówień"))
        self.menuPlik.setTitle(_translate("MainWindow", "Plik"))
        self.menuO_programie.setTitle(_translate("MainWindow", "O programie"))
        self.exitProgram.setText(_translate("MainWindow", "Wyjdź z programu"))
        self.exitProgram.setShortcut(_translate("MainWindow", "Ctrl+Q"))

import resources_rc
