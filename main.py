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
    filepath="compile.bat"
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
    sys.exit(app.exec_())