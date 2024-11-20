import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QPushButton, QWidget
)

class CurrencyConverter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Currency Converter")
        self.setGeometry(200, 200, 400, 200)

        self.exchange_rates = {
            "USD": 1.0,
            "NGN": 1800,  # 1 USD = 1800 Naira
            "EUR": 0.85,   # 1 USD = 0.85 Euros
            "GBP": 0.75,   # 1 USD = 0.75 Pounds
            "INR": 74.0    # 1 USD = 74 Rupees
        }

        # Main Widget and Layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()
        self.create_ui()
        self.main_widget.setLayout(self.layout)

    def create_ui(self):
        title = QLabel("Currency Converter")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.layout.addWidget(title)

        input_layout = QHBoxLayout()
        self.amount_label = QLabel("Enter Amount:")
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("e.g., 100")
        input_layout.addWidget(self.amount_label)
        input_layout.addWidget(self.amount_input)
        self.layout.addLayout(input_layout)

        dropdown_layout = QHBoxLayout()
        self.from_currency_label = QLabel("From Currency:")
        self.from_currency_dropdown = QComboBox()
        self.to_currency_label = QLabel("To Currency:")
        self.to_currency_dropdown = QComboBox()

        currencies = ["USD", "NGN", "EUR", "GBP", "INR"]
        self.from_currency_dropdown.addItems(currencies)
        self.to_currency_dropdown.addItems(currencies)

        dropdown_layout.addWidget(self.from_currency_label)
        dropdown_layout.addWidget(self.from_currency_dropdown)
        dropdown_layout.addWidget(self.to_currency_label)
        dropdown_layout.addWidget(self.to_currency_dropdown)
        self.layout.addLayout(dropdown_layout)

        self.convert_button = QPushButton("Convert")
        self.layout.addWidget(self.convert_button)
        self.result_label = QLabel("Converted Amount: ")
        self.result_label.setStyleSheet("font-size: 16px; color: blue;")
        self.layout.addWidget(self.result_label)

        self.convert_button.clicked.connect(self.convert_currency)

    def convert_currency(self):
        try:
            amount = float(self.amount_input.text())
            from_currency = self.from_currency_dropdown.currentText()
            to_currency = self.to_currency_dropdown.currentText()
            converted_amount = self.perform_conversion(amount, from_currency, to_currency)
            self.result_label.setText(f"Converted Amount: {converted_amount:.2f} {to_currency}")
        except ValueError:
            self.result_label.setText("Error: Please enter a valid number.")

    def perform_conversion(self, amount, from_currency, to_currency):
        from_rate = self.exchange_rates[from_currency]
        to_rate = self.exchange_rates[to_currency]
        return amount * (to_rate / from_rate)

app = QApplication(sys.argv)
window = CurrencyConverter()
window.show()
sys.exit(app.exec_())
