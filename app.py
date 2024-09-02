import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QStackedWidget, QLabel
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from screens.create import CreatePage
from screens.search import SearchPage

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Main layout
        self.layout = QVBoxLayout()
        
        # Create navigation bar
        self.navbar = self.create_navbar()
        self.layout.addLayout(self.navbar)

        # Create QStackedWidget to hold multiple pages
        self.stacked_widget = QStackedWidget()

        # Create instances of the pages
        self.main_page = SearchPage(self.stacked_widget)
        self.create_page = CreatePage(self.stacked_widget)

        # Add pages to the QStackedWidget
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.create_page)

        # Add the stacked widget to the main layout
        self.layout.addWidget(self.stacked_widget)

        # Set layout and window properties
        self.setLayout(self.layout)
        self.setWindowTitle("App with Navigation")
        self.showMaximized()
        
        
    def create_navbar(self):
          nav_layout = QHBoxLayout()

          # Create and add navigation buttons
          home_button = QPushButton("Home")
          create_button = QPushButton("Create")
          
          # Set button style
          buttons = [home_button, create_button]
          for button in buttons:
              button.setFont(QFont('Arial', 14))
              button.setStyleSheet(
                  "background-color: #007BFF; color: white; padding: 10px 20px; border-radius: 5px;"
              )
              button.setCursor(Qt.PointingHandCursor)

          # Connect buttons to page switching
          home_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
          create_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

          nav_layout.addWidget(home_button)
          nav_layout.addWidget(create_button)

          # Add a spacer to push buttons to the left
          nav_layout.addStretch(1)

          return nav_layout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
