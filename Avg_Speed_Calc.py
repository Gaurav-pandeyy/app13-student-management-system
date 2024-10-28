import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox

class Speed_Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")

        grid = QGridLayout()

        D_label = QLabel("Distance")
        self.D_label_edit = QLineEdit()
        self.combo = QComboBox()
        self.combo.addItems(['Metric(km)', 'Imperial(miles)'])

        T_label = QLabel("Time(hours)")
        self.T_label_edit = QLineEdit()
        calculate_button = QPushButton("Calculate")
        self.output_label = QLabel("")

        grid.addWidget(D_label, 0, 0)
        grid.addWidget(self.D_label_edit, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(T_label, 1, 0)
        grid.addWidget(self.T_label_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 3)
        grid.addWidget(self.output_label, 3, 0, 1, 3)

        self.setLayout(grid)
        calculate_button.clicked.connect(self.calucate_speed)

    def calucate_speed(self):
        if self.combo.currentText() == "Metric(km)":
            try:
                distance = float(self.D_label_edit.text())
                timeftravel = float(self.T_label_edit.text())
                averagespeed = distance / timeftravel
                self.output_label.setText(
                    f"The average speed is {averagespeed:.2f} {'km/h' if self.combo.currentText() == 'Metric(km)' else 'miles/h'}.")
            except ValueError:
                self.output_label.setText("Please enter valid numbers for distance and time.")
                return

app = QApplication(sys.argv)
speedC = Speed_Calculator()
speedC.show()
sys.exit(app.exec())
