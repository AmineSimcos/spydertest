import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QGridLayout, QFileDialog
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore



app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Titre su fenetre")
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")
window.move(200, 200)

grid = QGridLayout()

def frame1():
    
    image = QPixmap("aaa.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 20px;")
    
    button = QPushButton("PLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 45px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 25px 0;" +
        "margin: 100px 200px;}" +
        "*:hover{background: '#BC006C';}"
    )
    
    
    
    grid.addWidget(logo, 0, 0)
    grid.addWidget(button, 1, 0)

frame1()

window.setLayout(grid)


window.show()
sys.exit(app.exec())