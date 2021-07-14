import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        navbar = QToolBar()
        self.addToolBar(navbar)

        back = QAction('<', self)
        back.triggered.connect(self.browser.back)
        navbar.addAction(back)

        forward = QAction('>', self)
        forward.triggered.connect(self.browser.forward)
        navbar.addAction(forward)
        
        refresh = QAction('R', self)
        refresh.triggered.connect(self.browser.reload)
        navbar.addAction(refresh)


        home = QAction('H', self)
        home.triggered.connect(self.hom)
        navbar.addAction(home)

        
       

    def hom(self):
               self.browser.setUrl(QUrl('https://google.com'))
  
  

app = QApplication(sys.argv)
QApplication.setApplicationName('Peanut')
window = MainWindow()
app.exec_()