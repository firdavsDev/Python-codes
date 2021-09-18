#PyQt5 ni o'rnatish uchun qo'llanma 
#video dars https://t.me/pythonuz_videos/43
#PyQt Windows operatsion tizimi uchun dasturlar yaratishda foydalaniladigan cross-platforma .Bundan foydalanish uchun python dasturini yuklang https://www.python.org/ftp/python/3.5.4/python-3.5.4-amd64.exe
#Konsolga <pip install wheel> yozing 
#D diskiga https://www.python.org/ftp/python/3.5.4/python-3.5.4-amd64.exe ni yuklang va konsolga <pip install D:\cx_Freeze‑5.1.1‑cp35‑cp35m‑win_amd64.whl> ni yozing
#Endi kompilyatsiya qilmoqchi bo'lgan dastur bilan katalogda "setup.py" va "test.py" faylini yarating
#matnli fayl ochamiz <python.exe setup.py build> ni yozib "run.bat" ko'rinishida saqlaymiz va "run.bat" faylni ustiga bosamiz

#Руководство по установке PyQt5 
#урок видео https://t.me/pythonuz_videos/43
#PyQt - это кросс-платформа, используемая для создания программного обеспечения для операционной системы Windows. Загрузите для него программное обеспечение python https://www.python.org/ftp/python/3.5.4/python-3.5.4-amd64.exe
#Напишите <pip install wheel> на консоль
#Загрузите файл https://www.python.org/ftp/python/3.5.4/python-3.5.4-amd64.exe на диск D и установите <pip install D:\cx_Freeze-5.1.1-cp35-cp35m-win_amd64.whl> на консоли
#Теперь в каталоге с программой которую нужно скомпилировать создайте файл "setup.py" и "test.py", с таким содежанием
#текстовый файл <python.exe setup.py build> и сохраните его в представлении "run.bat" и нажмите на файл "run.bat"

#PyQt5 Installation Guide
#video lesson https://t.me/pythonuz_videos/43
#PyQt is a cross-platform used to create software for the Windows operating system. Download the python software for it https://www.python.org/ftp/python/3.5.4/python-3.5.4-amd64.exe
#Write <pip install wheel> to the console
#D drive https://www.python.org/ftp/python/3.5.4/python-3.5.4-amd64.exe and install the <pip install D:\cx_Freeze-5.1.1-cp35-cp35m-win_amd64.whl> on the console
#Now, in the directory with the program you want to compile, create a "setup.py" and "test.py" file, with this
#text file <python.exe setup.py build> and save it in the "run.bat" view and click on the file "run.bat"


##############################################################
"setup.py"
from cx_Freeze import setup, Executable

setup(
    name = "Freelance",
    version = "1.0",
    description = "Freelance Parser",
    executables = [Executable("free.py")]
)
##############################################################
#PyQt5 window

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
##############################################################
"run.bat"

python.exe setup.py build
##############################################################

exe.win32-3.5\test.exe



##########################################################################################################################################################
##########################################################################################################################################################


#PyQt5 window

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 statusbar

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 status bar example - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Message in statusbar.')
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 buttons

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100,70) 
        button.clicked.connect(self.on_click)
 
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 signals and slots

from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
 
import sys
 
class Dialog(QDialog):
 
    def slot_method(self):
        print('slot method called.')
 
    def __init__(self):
        super(Dialog, self).__init__()
 
        button=QPushButton("Click")
        button.clicked.connect(self.slot_method)
 
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)
 
        self.setLayout(mainLayout)
        self.setWindowTitle("Button Example - @pyqt5 or @apiuz")
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())
#############################################################################
#PyQt5 messagebox

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 messagebox - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        else:
            print('No clicked.')
 
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
#############################################################################
#PyQt5 textbox example

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
 
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,80)
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - @pyqt5 or @apiuz', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

#############################################################################
#PyQt5 absolute position

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt absolute positioning - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 440
        self.height = 280
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        label = QLabel('Python', self)
        label.move(50,50)
 
        label2 = QLabel('PyQt5', self)
        label2.move(100,100)
 
        label3 = QLabel('Examples', self)
        label3.move(150,150)
 
        label4 = QLabel('pytonspot.com', self)
        label4.move(200,200)
 
 
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 menu

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 menu - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
 
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
 
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 table

#In this article you will learn how to use tables with PyQt5.

#PyQt5 table

#To add a table, you will need to import QTableWidget and QTableWidgetItem.

from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
#A table is created with:

self.tableWidget = QTableWidget()
 
# set row count
self.tableWidget.setRowCount(4)
 
# set column count
self.tableWidget.setColumnCount(2)
To add individual cells:

self.tableWidget.setItem(X,Y, QTableWidgetItem("TEXT"))

#PyQt5 table example
#The full PyQt5 table code is below:

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 table - @pyqt5 or @apiuz'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createTable()
 
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
 
        # Show widget
        self.show()
 
    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,0)
 
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
 
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 tabs

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabs - @pyqt5 or @apiuz'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
 
        self.show()
 
class MyTableWidget(QWidget):        
 
    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
 
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()   
        self.tab2 = QWidget()
        self.tabs.resize(300,200) 
 
        # Add tabs
        self.tabs.addTab(self.tab1,"Tab 1")
        self.tabs.addTab(self.tab2,"Tab 2")
 
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)
 
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
 
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 horizontal layout

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createHorizontalLayout()
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
 
        self.show()
 
    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("What is your favorite color?")
        layout = QHBoxLayout()
 
        buttonBlue = QPushButton('Blue', self)
        buttonBlue.clicked.connect(self.on_click)
        layout.addWidget(buttonBlue) 
 
        buttonRed = QPushButton('Red', self)
        buttonRed.clicked.connect(self.on_click)
        layout.addWidget(buttonRed) 
 
        buttonGreen = QPushButton('Green', self)
        buttonGreen.clicked.connect(self.on_click)
        layout.addWidget(buttonGreen) 
 
        self.horizontalGroupBox.setLayout(layout)
 
 
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 grid layout

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createGridLayout()
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
 
        self.show()
 
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
 
        layout.addWidget(QPushButton('1'),0,0) 
        layout.addWidget(QPushButton('2'),0,1) 
        layout.addWidget(QPushButton('3'),0,2) 
        layout.addWidget(QPushButton('4'),1,0) 
        layout.addWidget(QPushButton('5'),1,1) 
        layout.addWidget(QPushButton('6'),1,2) 
        layout.addWidget(QPushButton('7'),2,0) 
        layout.addWidget(QPushButton('8'),2,1) 
        layout.addWidget(QPushButton('9'),2,2) 
 
        self.horizontalGroupBox.setLayout(layout)
 
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQT5 input dialog

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 input dialogs - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.getInteger()
        self.getText()
        self.getDouble()
        self.getChoice()
 
        self.show()
 
    def getInteger(self):
        i, okPressed = QInputDialog.getInt(self, "Get integer","Percentage:", 28, 0, 100, 1)
        if okPressed:
            print(i)
 
    def getDouble(self):
        d, okPressed = QInputDialog.getDouble(self, "Get double","Value:", 10.50, 0, 100, 10)
        if okPressed:
            print( d)
 
    def getChoice(self):
        items = ("Red","Blue","Green")
        item, okPressed = QInputDialog.getItem(self, "Get item","Color:", items, 0, False)
        if ok and item:
            print(item)
 
    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Get text","Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 file dialog

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.openFileNameDialog()
        self.openFileNamesDialog()
        self.saveFileDialog()
 
        self.show()
 
    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
 
    def openFileNamesDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
 
    def saveFileDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 image

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('image.jpeg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
 
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 pixels
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import random
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt paint - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 440
        self.height = 280
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
 
        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0,0)
        self.m.resize(self.width,self.height)
 
        self.show()
 
 
class PaintWidget(QWidget):
   def paintEvent(self, event):
      qp = QPainter(self)
 
      qp.setPen(Qt.black)
      size = self.size()
 
      for i in range(1024):
          x = random.randint(1, size.width()-1)
          y = random.randint(1, size.height()-1)
          qp.drawPoint(x, y)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQT5 color dialog
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 color dialog - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        button = QPushButton('Open color dialog', self)
        button.setToolTip('Opens color dialog')
        button.move(10,10)
        button.clicked.connect(self.on_click)
 
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        openColorDialog(self)
 
 
def openColorDialog(self):
    color = QColorDialog.getColor()
 
    if color.isValid():
        print(color.name())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 colors
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import random
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt rectangle colors - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 440
        self.height = 280
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
 
        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0,0)
        self.m.resize(self.width,self.height)
 
        self.show()
 
 
class PaintWidget(QWidget):
   def paintEvent(self, event):
      qp = QPainter(self)
 
      qp.setPen(Qt.black)
      size = self.size()
 
      # Colored rectangles
      qp.setBrush(QColor(200, 0, 0))
      qp.drawRect(0, 0, 100, 100)
 
      qp.setBrush(QColor(0, 200, 0))
      qp.drawRect(100, 0, 100, 100)
 
      qp.setBrush(QColor(0, 0, 200))
      qp.drawRect(200, 0, 100, 100)
 
      # Color Effect
      for i in range(0,100):
          qp.setBrush(QColor(i*10, 0, 0))
          qp.drawRect(10*i, 100, 10, 32)
 
          qp.setBrush(QColor(i*10, i*10, 0))
          qp.drawRect(10*i, 100+32, 10, 32)
 
          qp.setBrush(QColor(i*2, i*10, i*1))
          qp.drawRect(10*i, 100+64, 10, 32)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 drag and drop
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 drag and drop - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 60
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        editBox = QLineEdit('Drag this', self)
        editBox.setDragEnabled(True)
        editBox.move(10, 10)
        editBox.resize(100,32)
 
        button = CustomLabel('Drop here.', self)
        button.move(130,15)
 
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
 
class CustomLabel(QLabel):
 
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)
 
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
 
    def dropEvent(self, e):
        self.setText(e.mimeData().text())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
#############################################################################
#PyQt5 font dialog
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFontDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 font dialog - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        button = QPushButton('Open PyQt5 Font Dialog', self)
        button.setToolTip('font dialog')
        button.move(50,50)
        button.clicked.connect(self.on_click)
 
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        openFontDialog(self)
 
 
def openFontDialog(self):
    font, ok = QFontDialog.getFont()
    if ok:
        print(font.toString())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 Matplotlib
import sys
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
 
 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
 
import random
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - @pyqt5 or @apiuz'
        self.width = 640
        self.height = 400
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        m = PlotCanvas(self, width=5, height=4)
        m.move(0,0)
 
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(500,0)
        button.resize(140,100)
 
        self.show()
 
 
class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
 
 
    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 webkit example
#!/usr/bin/env python
 
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
 
app = QApplication(sys.argv)
 
web = QWebView()
web.load(QUrl("https://@pyqt5 or @apiuz"))
web.show()
 
sys.exit(app.exec_())
#############################################################################
PyQt5 webkit browser
#!/usr/bin/python
 
import PyQt5
from PyQt5.QtCore import QUrl 
from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtWebKitWidgets import QWebView , QWebPage
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtNetwork import *
import sys
from optparse import OptionParser
 
 
class MyBrowser(QWebPage):
    ''' Settings for the browser.'''
 
    def userAgentForUrl(self, url):
        ''' Returns a User Agent that will be seen by the website. '''
        return "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
 
class Browser(QWebView):
    def __init__(self):
        # QWebView
        self.view = QWebView.__init__(self)
        #self.view.setPage(MyBrowser())
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)
        #super(Browser).connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&)"), self.adjustTitle)
 
    def load(self,url):  
        self.setUrl(QUrl(url)) 
 
    def adjustTitle(self):
        self.setWindowTitle(self.title())
 
    def disableJS(self):
        settings = QWebSettings.globalSettings()
        settings.setAttribute(QWebSettings.JavascriptEnabled, False)
 
 
 
app = QApplication(sys.argv) 
view = Browser()
view.showMaximized()
view.load("https://@pyqt5 or @apiuz")
app.exec_()
#############################################################################
#PyQt5 Treeview
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtGui import QIcon
 
from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,
        QTime)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout,
        QWidget)
 
 
class App(QWidget):
 
    FROM, SUBJECT, DATE = range(3)
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Treeview Example - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 240
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.dataGroupBox = QGroupBox("Inbox")
        self.dataView = QTreeView()
        self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(True)
 
        dataLayout = QHBoxLayout()
        dataLayout.addWidget(self.dataView)
        self.dataGroupBox.setLayout(dataLayout)
 
        model = self.createMailModel(self)
        self.dataView.setModel(model)
        self.addMail(model, 'service@github.com', 'Your Github Donation','03/25/2017 02:05 PM')
        self.addMail(model, 'support@github.com', 'Github Projects','02/02/2017 03:05 PM')
        self.addMail(model, 'service@phone.com', 'Your Phone Bill','01/01/2017 04:05 PM')
 
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataGroupBox)
        self.setLayout(mainLayout)
 
        self.show()
 
    def createMailModel(self,parent):
        model = QStandardItemModel(0, 3, parent)
        model.setHeaderData(self.FROM, Qt.Horizontal, "From")
        model.setHeaderData(self.SUBJECT, Qt.Horizontal, "Subject")
        model.setHeaderData(self.DATE, Qt.Horizontal, "Date")
        return model
 
    def addMail(self,model, mailFrom, subject, date):
        model.insertRow(0)
        model.setData(model.index(0, self.FROM), mailFrom)
        model.setData(model.index(0, self.SUBJECT), subject)
        model.setData(model.index(0, self.DATE), date)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 Directory View
import sys
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file system view - @pyqt5 or @apiuz'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
 
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
 
        self.tree.setWindowTitle("Dir View")
        self.tree.resize(640, 480)
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.setLayout(windowLayout)
 
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
#############################################################################
#PyQt5 Form Layout
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
 
import sys
 
class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4
 
    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()
 
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
 
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
 
        self.setWindowTitle("Form Layout - @pyqt5 or @apiuz")
 
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel("Name:"), QLineEdit())
        layout.addRow(QLabel("Country:"), QComboBox())
        layout.addRow(QLabel("Age:"), QSpinBox())
        self.formGroupBox.setLayout(layout)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())
#############################################################################
#PyQt5 QBoxLayout
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)
 
import sys
 
class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4
 
    def __init__(self):
        super(Dialog, self).__init__()
 
        b1=QPushButton("Button1")
        b2=QPushButton("Button2")
        b3=QPushButton("Button3")
        b4=QPushButton("Button4")
 
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(b1)
        mainLayout.addWidget(b2)
        mainLayout.addWidget(b3)
        mainLayout.addWidget(b4)
 
        self.setLayout(mainLayout)
        self.setWindowTitle("Form Layout - @pyqt5 or @apiuz")
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())
#############################################################################
#PyQt5 Wizard
#!/usr/bin/env python
 
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtProperty
from PyQt5 import QtCore, QtWidgets
 
class QIComboBox(QtWidgets.QComboBox):
    def __init__(self,parent=None):
        super(QIComboBox, self).__init__(parent)
 
 
class MagicWizard(QtWidgets.QWizard):
    def __init__(self, parent=None):
        super(MagicWizard, self).__init__(parent)
        self.addPage(Page1(self))
        self.addPage(Page2(self))
        self.setWindowTitle("PyQt5 Wizard Example - @pyqt5 or @apiuz")
        self.resize(640,480)
 
class Page1(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super(Page1, self).__init__(parent)
        self.comboBox = QIComboBox(self)
        self.comboBox.addItem("Python","/path/to/filename1")
        self.comboBox.addItem("PyQt5","/path/to/filename2")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.comboBox)
        self.setLayout(layout)
 
 
class Page2(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super(Page2, self).__init__(parent)
        self.label1 = QtWidgets.QLabel()
        self.label2 = QtWidgets.QLabel()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)
 
    def initializePage(self):
        self.label1.setText("Example text")
        self.label2.setText("Example text")
 
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wizard = MagicWizard()
    wizard.show()
    sys.exit(app.exec_())
#############################################################################
