import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QStackedWidget, QLabel
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SearchPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget

        # Main layout
        self.layout = QVBoxLayout()

        # Create search bar
        self.search_bar = self.create_search_bar()
        self.layout.addLayout(self.search_bar)

        # Add a spacer to push content to the top
        self.layout.addStretch(1)

        # Set layout and window properties
        self.setLayout(self.layout)


    def create_search_bar(self):
        search_layout = QHBoxLayout()

        # Add a spacer to center the search bar
        search_layout.addStretch(1)

        # Create and add the search input
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search...")
        search_input.setFont(QFont('Arial', 18))  # Increase the font size
        search_input.setFixedHeight(40)  # Increase the height of the search bar
        search_input.setStyleSheet("padding: 5px 15px; border-radius: 10px; border: 1px solid #CCC;")
        search_layout.addWidget(search_input)

        # Add a spacer to center the search bar
        search_layout.addStretch(1)

        return search_layout