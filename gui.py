import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication, QDate, QDateTime, Qt, QTimer
from PyQt5.QtWidgets import QWidget
import PyQt5.QtWidgets as Qw


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(300, 300 , 600, 400)
        self.setWindowTitle('Aviwest SIM reporter')

        self.createLeftGroupBox()
        # self.createRightGroupBox()

        mainLayout = Qw.QGridLayout()
        mainLayout.addWidget(self.LeftGroupBox, 1, 0)
        # mainLayout.addWidget(self.RightGroupBox, 1, 1)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)
        self.home()
        
        
    def home(self):
        quit_btn = Qw.QPushButton('Quit', self)
        quit_btn.clicked.connect(QCoreApplication.instance().quit)      
        quit_btn.move(400,300)
        # self.init_calendar()
        self.show()

    def createLeftGroupBox(self):
        self.LeftGroupBox = Qw.QGroupBox('SIM Card Period')

        heading = Qw.QLabel('SIM Period Start')
        sim_start_cal = Qw.QCalendarWidget(self)
        sim_start_cal.setGridVisible(True)
        sim_start_cal.move(20, 20)
        sim_start_cal.clicked[QDate].connect(self.print_date)

        layout = Qw.QVBoxLayout()
        layout.addWidget(heading)
        layout.addWidget(sim_start_cal)
        layout.addStretch(1)
        self.LeftGroupBox.setLayout(layout)  
    
    def print_date(self, date):
        print(date)

def main():
    app = Qw.QApplication([])
    app.setStyle('Fusion')
    window = Window()
    layout = Qw.QVBoxLayout()

    # dateCalendar = QtGui.
    # layout.addWidget(dateTimeEdit)

    window.setLayout(layout)
    app.exec_()

main()
