import sys

from PyQt6.QtWidgets import QMainWindow, QLayout, QTextEdit, QLineEdit, QPushButton, QApplication
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chatbot")
        self.setMinimumSize(700, 500)

        # layout = QLayout()

        # Add chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add the input widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 30)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 35)

        self.show()

class Chatbot:
    pass


app = QApplication(sys.argv)
main_window = MainWindow()
sys.exit(app.exec())
