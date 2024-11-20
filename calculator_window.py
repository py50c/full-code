import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QWidget, QPushButton, QLineEdit

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        # Create the main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()

        # Create the display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display)

        # Create a grid layout for buttons
        self.buttons_layout = QGridLayout()
        self.layout.addLayout(self.buttons_layout)

        # Add buttons
        self.add_buttons()

        # Set layout to the main widget
        self.main_widget.setLayout(self.layout)

    def add_buttons(self):
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]
        for text, row, col in buttons:
            button = QPushButton(text)
            self.buttons_layout.addWidget(button, row, col)

app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec_())
