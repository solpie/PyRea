from PyQt4 import QtGui as G
import sys

sys.argv = ["Main"]
if __name__ == '__main__':
    app = G.QApplication(sys.argv)
    button = G.QPushButton("Hello World!")
    button.show()
    sys.exit(app.exec_())