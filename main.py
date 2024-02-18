from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys
from backend import Chatbot
import threading

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

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
        self.input_field.returnPressed.connect(self.send_message)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 35)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        reply = self.chatbot.get_response(user_query=user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Bot: {reply}</p>")



app = QApplication(sys.argv)
main_window = MainWindow()
sys.exit(app.exec())
