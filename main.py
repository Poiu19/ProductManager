#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     Manager of app
#
# Author:      Merchelski Patryk
#
# Created:     18.09.2018
# Copyright:   (c) Merchelski Patryk 2018
# Licence:
#-------------------------------------------------------------------------------
developerMode = True
if(developerMode):
    import subprocess
    filepaths = []
    filepaths.append("reso.bat")
    filepaths.append("C:\Python35\Lib\site-packages\PyQt5\pyuic5.bat .\product.ui -o product.py")
    filepaths.append("C:\Python35\Lib\site-packages\PyQt5\pyuic5.bat .\gui.ui -o gui.py")
    for filepath in filepaths:
        p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
        stdout, stderr = p.communicate()
        print(p.returncode)

from PyQt5.QtWidgets import QApplication
from userinterface import InterfaceWindow
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = InterfaceWindow()
    window.createNewsList()
    window.initializeEvents()
    window.createCategories()
    app.aboutToQuit.connect(window.exitApp)
    sys.exit(app.exec_())