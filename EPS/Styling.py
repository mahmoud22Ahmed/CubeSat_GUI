from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel,  QTabWidget, QWidget
from PyQt6.QtGui import QPixmap
from EPS_TAB import Ui_MainWindow

class Styling(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set up a QLabel to display the background image
        self.background_label = QLabel(self)
        self.update_background_size()  # Set initial size
        pixmap = QPixmap("../background.jpg")  # Replace with the path to your image
        self.background_label.setPixmap(pixmap)

        # Make the label a child of the central widget
        self.background_label.setParent(self.centralWidget())

        # Set a lower stacking order for the background_label
        self.background_label.lower()
        self.setStyleSheet('''
         QGroupBox#groupbox_AV{
                 font-size: 20px; font-family: Arial; font-weight: bold;color: white;          
         }  
         QLabel#label_VBAT{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }
         QLabel#label_C33{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }
         QLabel#label_C5{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }

                              
         QGroupBox#groupbox_SUB{
                 font-size: 20px; font-family: Arial; font-weight: bold;color: white;          
         }  
         QLabel#label_OBC{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }
         QLabel#label_COMM{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }
         QLabel#label_PAYLOAD{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }  
         QLabel#label_ADCS{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }

                                         
          QGroupBox#groupbox_SOLAR{
                 font-size: 20px; font-family: Arial; font-weight: bold;color: white;          
          }  
          QLabel#label_SOLAR1{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }
          QLabel#label_SOLAR2{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }
          QLabel#label_SOLAR3{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }  
          QLabel#label_SOLAR4{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }
                           

          QGroupBox#groupBox_MOTORS{
                 font-size: 20px; font-family: Arial; font-weight: bold;color: white;          
          }  
          QLabel#label_MOTX{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }
          QLabel#label_MOTY{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }
          QLabel#label_MOTZ{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }
                           
          QGroupBox#groupBox_TEMP{
                 font-size: 20px; font-family: Arial; font-weight: bold;color: white;          
          }  
          QLabel#label_HBAT{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }
          QLabel#label_EPST{
                 font-size: 16px; font-family: Arial; font-weight: bold; color: white;          
          }                                  
        ''')


    def update_background_size(self):
        # Update the size of the background_label to cover the entire window
        self.background_label.setGeometry(0, 0, self.width(), self.height())

    def resizeEvent(self, event):
        # Override the resizeEvent to update the background size when the window is resized
        self.update_background_size()

       