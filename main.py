import sys
from PyQt5.QtWidgets import QApplication as qa, QMainWindow as qm, QLabel as ql
from PyQt5.QtGui import QFont as qf, QPixmap as qp
from PyQt5.QtCore import Qt as qt

class appl(qm):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Design Feedback Normalizer")
        self.setGeometry(0, 0, 500, 500)
        self.setFixedSize(500, 500)

        title = ql("Design Feedback Normalizer", self)
        title.setFont(qf("Arial", 20))
        title.setGeometry(0, 120, 500, 50)
        title.setAlignment(qt.AlignHCenter)
        title.setAlignment(qt.AlignCenter)
        title.setStyleSheet("color: blue;")

        logo = ql(self)
        logo.setGeometry(200, 20, 100, 100)
        logo.setStyleSheet("border: 2px solid blue;"
                           "border-radius: 5px;")
        pxm = qp("logo.png")
        logo.setPixmap(pxm)
        logo.setScaledContents(True)


def main():
    app = qa(sys.argv)
    window = appl()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()