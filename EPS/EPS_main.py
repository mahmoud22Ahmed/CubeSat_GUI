import sys
from EPS_TAB import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow
from mergeDataWithGui import *

def main ():
   app = QApplication(sys.argv)
   #1)
   EPS=mergeDataWithGui()
   #2)
   EPS.StylingObject.show()  
   sys.exit(app.exec())



if __name__ == "__main__":
   main()