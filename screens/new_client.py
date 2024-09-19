import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QStackedWidget, QLabel
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class NewClientPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget

        # Main layout
        self.layout = QVBoxLayout()

        # Create form
        self.form = self.create_form()
        self.layout.addLayout(self.form)

        # Add a spacer to push content to the top
        self.layout.addStretch(1)

        # Set layout and window properties
        self.setLayout(self.layout)

    def create_form(self):
        form_layout = QVBoxLayout()

        # Create and add text fields
        for i in range(1, 6):
            text_input = QLineEdit()
            text_input.setPlaceholderText(f"Field {i}")
            text_input.setFont(QFont('Arial', 18))  # Increase the font size
            text_input.setFixedHeight(40)  # Set the height of the text field
            text_input.setStyleSheet(
                "padding: 5px 15px; border-radius: 10px; border: 1px solid #CCC; margin-bottom: 15px;"
            )
            form_layout.addWidget(text_input)

        # Create and add submit button
        submit_button = QPushButton("Submit")
        submit_button.setFont(QFont('Arial', 16))
        submit_button.setStyleSheet(
            "background-color: #28A745; color: white; padding: 10px 20px; border-radius: 5px;"
        )
        submit_button.setCursor(Qt.PointingHandCursor)
        form_layout.addWidget(submit_button, alignment=Qt.AlignCenter)

        return form_layout