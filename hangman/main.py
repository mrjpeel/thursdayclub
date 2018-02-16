from PyQt5.QtCore import QSize
from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtWidgets import *
from random import randint


class Hangman(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle(" - - Hangman - - ")
        self.statusBar().showMessage("Welcome to PyQt Hangman")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        vertbox = QVBoxLayout()
        centralWidget.setLayout(vertbox)

        hozbox = QHBoxLayout()
        vertbox.addLayout(hozbox)

        gridLayout = QGridLayout(self)
        vertbox.addLayout(gridLayout)

        self.guesslist = []
        self.blankslist = []
        self.startblankslist = []

        self.dictofletters = {'0':'A', '1':'B', '2':'C', '3':'D', '4':'E', '5':'F',
                              '6':'G', '7':'H', '8':'I', '9':'J', '10':'K', '11':'L',
                              '12':'M', '13':'N', '14':'O', '15':'P', '16':'Q',
                              '17':'R', '18':'S', '19':'T', '20':'U', '21':'V',
                              '22':'W', '23':'X', '24':'Y', '25':'Z', '26':'REPLAY'}

        self.hanglist = ['COMPUTING', 'WARWICK', 'GOOGLE']
        randword = randint(0, len(self.hanglist) - 1)

        self.hangword = self.hanglist[randword]
        self.answerlist = list(self.hangword)

        numofguesses = len(self.hangword) + len(self.hangword) // 2

        for letter in range(numofguesses):
            self.guesslist.append("_")

        for letter in self.hangword:
            self.blankslist.append("_")

        blankstext = " ".join(self.blankslist)
        starttext = " ".join(self.guesslist)

        print(self.hangword, "<> ", blankstext,"<>", starttext)

        self.lblwordtoguess = QLabel(blankstext, self)
        self.lblwordtoguess.setAlignment(QtCore.Qt.AlignCenter)
        # self.lblwordtoguess.move(50, 35)
        hozbox.addWidget(self.lblwordtoguess)

        self.lbllettersguessed = QLabel(starttext, self)
        self.lbllettersguessed.setAlignment(QtCore.Qt.AlignCenter)
        # self.lbllettersguessed.move(150, 55)
        hozbox.addWidget(self.lbllettersguessed)

        positions = [(i,j) for i in range(9) for j in range(3)]

        for position, aletter in zip(positions, range(0,27)):
            pybutton = QPushButton(self.dictofletters[str(aletter)], self)
            pybutton.resize(35, 35)
            pybutton.clicked.connect(self.clickMethod)
            gridLayout.addWidget(pybutton, *position)



    def clickMethod(self):

        newguess = self.sender() # this will get memory location of value

        # newguess.text() will then get the value of the button text

        print(newguess.text(), "<>", self.guesslist, "<>", self.answerlist)

        if newguess.text() == 'REPLAY':
            self.statusBar().showMessage(newguess.text() + ' game will restart now....')
        else:
            self.statusBar().showMessage(newguess.text() + ' has been pressed')

        if newguess.text() not in self.answerlist and newguess.text() not in self.guesslist:
            guessstring = "".join(self.guesslist)
            guessstring = guessstring.replace("_", newguess.text(), 1)
            self.guesslist = list(guessstring)

        wordguess = ' '.join(self.guesslist)
        print(wordguess)

        stringblanks = ' '.join(self.blankslist)
        print(stringblanks)

        self.lblwordtoguess.setText(stringblanks)
        self.lbllettersguessed.setText(wordguess)

        for index, item in enumerate(self.answerlist):
            if item == newguess.text():
                self.blankslist[index] = item
                strnewblanks = " ".join(self.blankslist)
                self.lblwordtoguess.setText(strnewblanks)

        #if newguess.text() in self.answerlist and newguess.text() not in self.guesslist:
        #    guessstring = "".join(self.guesslist)
        #    guessstring = guessstring.replace("_", newguess.text(), 1)
        #    self.guesslist = list(guessstring)

        if self.blankslist == self.answerlist:
            self.lblwordtoguess.setText("You Won")
            self.lbllettersguessed.setText("# S U P E R S T A R #")

        if "_" not in self.guesslist:
            self.lblwordtoguess.setText("You Lost")
            self.lbllettersguessed.setText("# DON'T BE SAD #")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainwin = Hangman()
    mainwin.show()

    sys.exit( app.exec_() )


