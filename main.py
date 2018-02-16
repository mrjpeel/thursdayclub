from PyQt5.QtCore import QSize
from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtWidgets import *


class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("Hello World")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        title = QLabel("Hello World again!", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)

        pybutton = QPushButton("Click This!", self)
        pybutton.setToolTip("This is a button which opens a message box")
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100, 32)
        pybutton.move(50, 50)
        gridLayout.addWidget(pybutton)

        newAction = QAction("&New", self)
        newAction.setShortcut("Ctrl + N")
        newAction.setToolTip("New Document")
        newAction.triggered.connect(self.newCall)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(newAction)

        nameLabel = QLabel(self)
        nameLabel.setText('Name:')
        lineEdit = QLineEdit(self)

        gridLayout.addWidget(nameLabel)
        gridLayout.addWidget(lineEdit)


    def clickMethod(self):
        QMessageBox.about(self, "Button Clicked", "Thank you for clicking the button")


    def newCall(self):
        print("New Document Created")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainwin = HelloWindow()
    mainwin.show()

    sys.exit( app.exec_() )


