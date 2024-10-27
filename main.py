import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        name_label = QLabel("Name")
        self.name_line_edit = QLineEdit()

        date_label = QLabel("Date of Birth (MM/DD/YYYY):")
        self.DOB = QLineEdit()
        calculate_button = QPushButton("Calculate Age")
        self.output_label = QLabel("")

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_label, 1, 0)
        grid.addWidget(self.DOB, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        calculate_button.clicked.connect(self.calculate_age)
        self.setLayout(grid)

    def calculate_age(self):
        try:
            current_year = datetime.now().year
            date_of_birth = self.DOB.text()
            birth_date = datetime.strptime(date_of_birth, "%m/%d/%Y").date()
            age = current_year - birth_date.year
            if datetime.now().date() < birth_date.replace(year=current_year):
                age -= 1
            self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")
        except ValueError:
            self.output_label.setText("Please enter a valid date in MM/DD/YYYY format.")

app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
