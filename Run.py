from PyQt5.QtWidgets import *
import sys

from namecall import Crawler
from analyzer import Analy


class UIloader(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


        #Init UI
        self.setWindowTitle("Zipf's law analyzer")
        self.setGeometry(200, 100, 500, 200)

        #Run button(Connect internet)
        Onanalyze = QPushButton("Analyze to Weblink", self)
        Onanalyze.clicked.connect(self.Webanalyze)

        #Run button(Open offline file)
        Offanalyze = QPushButton("Analyze to file", self)
        Offanalyze.clicked.connect(self.Fileanalyze)


        #Put in link URL
        self.Writer = QLineEdit()
        self.Writer.textChanged[str].connect(self.Settxt)

        #Explaining text
        texter = QLabel("Write down text URL include .txt file",self)
        font = texter.font()
        font.setFamily("Courier New")

        #Initiate layout
        Buttonlayout = QHBoxLayout()
        Buttonlayout.addWidget(Onanalyze)
        Buttonlayout.addWidget(Offanalyze)

        Programlayout = QVBoxLayout()
        Programlayout.addWidget(texter)
        Programlayout.addWidget(self.Writer)
        Programlayout.addLayout(Buttonlayout)
        self.setLayout(Programlayout)

    #Call namecall
    def Settxt(self):
        self.crawl = Crawler()
        self.crawl.Setname(self.Writer.text())

    #Call URL analyzer
    def Webanalyze(self):
        self.analy = Analy()
        self.analy.setdetect('URL')
        self.analy.settarget(self.crawl.Getname())
        self.analy.counter()

    #Call file analyzer
    def Fileanalyze(self):
        self.analy = Analy()
        self.analy.setdetect('FILE')
        self.analy.settarget(self.crawl.Getname())
        self.analy.counter()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    run = UIloader()
    run.show()
    app.exec_()


