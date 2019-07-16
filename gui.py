from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDateTimeEdit


app = QApplication([])
app.setStyle('Fusion')
window = QWidget()
layout = QVBoxLayout()

dateTimeEdit = QDateTimeEdit()
dateTimeEdit.setDateTime(QDateTime.currentDateTime())
layout.addWidget(dateTimeEdit)

window.setLayout(layout)
window.show()
app.exec_()
