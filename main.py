import sys
import os
from PyQt5.QtWidgets import (QApplication as qa, QMainWindow as qm, QLabel as ql, QLineEdit as qle, QPushButton as qpb,
                            QWidget as qw, QVBoxLayout as qvb, QHBoxLayout as qhb, QGridLayout as qg, QFileDialog as qfd)
 
from PyQt5.QtGui import QFont as qf, QPixmap as qp, QIcon as qi
from PyQt5.QtCore import Qt as qt

class appl(qm):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Design Feedback Normalizer")
        self.setGeometry(0, 0, 500, 500)
        self.setFixedSize(500, 600)
        self.setWindowIcon(qi('icon.png'))
        
        # input 1
        self.ilabel = ql("Identity Brand", self)
        self.ident = qle(self)
        
        # input 2
        self.clabel = ql("Color Pallete & Tipography",self)
        self.color = qle(self)

        #input 3
        self.comp = ql("Composition & Layout",self)
        self.coml = qle(self)

        #input 3
        self.ref = ql("Reference & Benchmarking",self)
        self.refer = qle(self)
        
        

        self.enter = qpb("Save Feedback", self)
        self.initUI()

        title = ql("Design Feedback Normalizer", self)
        done = ql("Your feedback is important, please describe it to your designer", self)
        done.setGeometry(35, 480, 500, 50)
        title.setFont(qf("Arial", 20))
        title.setGeometry(0, 120, 500, 50)
        title.setAlignment(qt.AlignHCenter)
        title.setAlignment(qt.AlignCenter)
        title.setStyleSheet("""
                                color: #a29bfe;
                                font-weight: bold;
                            """)


        logo = ql(self)
        logo.setGeometry(200, 20, 100, 100)
        logo.setStyleSheet("""
                                border: 2px solid #6c5ce7;
                                border-radius: 10px;
                                background-color: #1a1a24;
                            """)
        pxm = qp("icon.png")
        logo.setPixmap(pxm)
        logo.setScaledContents(True)

        self.enter.clicked.connect(self.save)
        self.enter.clicked.connect(self.toggle)

    def save(self):
        path, _ = qfd.getSaveFileName(self, "Save File and Share it to Your Designer", "", "Text Files (*.txt)")
        with open(path, 'w') as f:
                id = self.ident.text()
                col = self.color.text()
                com = self.coml.text()
                re = self.refer.text()
                
                f.write("Everything that needs to be revised\n")
                f.write(f"Identity Brand:             {id}\n")
                f.write(f"Color Pallete & Typography: {col}\n")
                f.write(f"Composition & Layout:       {com}\n")
                f.write(f"Reference & Benchmarking:   {re}\n")


    def initUI(self):
        self.ilabel.setGeometry(30, 170, 150, 25)
        self.ilabel.setAlignment(qt.AlignLeft)
        self.ident.setGeometry(30, 195, 430, 40)
        
        self.clabel.setGeometry(30, 250, 250, 25)
        self.clabel.setAlignment(qt.AlignLeft)
        self.color.setGeometry(30, 275, 430, 40)
        
        self.comp.setGeometry(30, 330, 220, 25)
        self.comp.setAlignment(qt.AlignLeft)
        self.coml.setGeometry(30, 355, 430, 40)
        
        self.ref.setGeometry(30, 410, 260, 25)
        self.ref.setAlignment(qt.AlignLeft)
        self.refer.setGeometry(30, 435, 430, 40)

        self.setStyleSheet("""
        QWidget {
            background-color: #0f0f14;
            color: #eae6ff;
            font-family: Segoe UI;
            font-size: 14px;
        }
        QLineEdit {
            background-color: #1a1a24;
            border: 1px solid #6c5ce7;
            border-radius: 8px;
            padding: 8px;
            color: #ffffff;
        }
        QLineEdit:focus {
            border: 2px solid #a29bfe;
            background-color: #1f1f2e;
        }
        QPushButton {
            background-color: #6c5ce7;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: bold;
            color: #ffffff;
        }
        QPushButton:hover {
            background-color: #a29bfe;
        }
        QPushButton:pressed {
            background-color: #4b3fbf;
        }
        QLabel {
                background-color: transparent;
                color: #a29bfe;
                font-weight: bold;
                font-size: 15px;
            }
        """)
        


        self.enter.setGeometry(30, 530, 430, 50)
        

def main():
    app = qa(sys.argv)
    window = appl()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()