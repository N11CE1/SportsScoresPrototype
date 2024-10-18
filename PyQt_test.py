import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QPushButton, QWidget, QHBoxLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton('#1')
        self.button2 = QPushButton('#2')
        self.button3 = QPushButton('#3')
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Helvetica;
                padding: 20px 30px;
                margin: 20px;
                border: 2px solid black;
                border-radius: 10px;
                }
            QPushButton#button1{
                background-color: #02def7;
                }
            QPushButton#button2{
                background-color: #0264f7;
                }
            QPushButton#button3{
                background-color: #02f795;
                }
            QPushButton#button1:hover{
                background-color: #7ff2ff;
                }
            QPushButton#button2:hover{
                background-color: #7fb2ff;
                }
            QPushButton#button3:hover{
                background-color: #7fffcc;
                }
            """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
