from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

class DigitalClock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Clock")
        self.setGeometry(100, 100, 200, 100)

        # Create a label to display the time
        self.label = QLabel("", self)
        self.label.setGeometry(50, 20, 100, 50)
        self.label.setAlignment(Qt.AlignCenter)

        # Set up a timer to update time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Initialize with the current time
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString('hh:mm:ss')
        self.label.setText(current_time)


app = QApplication(sys.argv)
window =DigitalClock()
window.show()
sys.exit(app.exec_())
