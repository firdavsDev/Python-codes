from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #nevbar yasaymz
        navbar=QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Orqaga',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Oldingi',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        
        reload_btn = QAction('Qayta',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btm = QAction('Uy',self)
        home_btm.triggered.connect(self.navigate_home)
        navbar.addAction(home_btm)

        self.url_bar= QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("Pro browser | Firdavs_Dev")
window=MainWindow()
app.exec_()