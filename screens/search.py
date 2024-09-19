import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QStackedWidget, QLabel
)
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt

class SearchPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget

        # Main layout
        self.layout = QVBoxLayout()

        # Add a centered label at the top
        self.add_top_label()

        # Create search bar
        self.search_bar = self.create_search_bar()
        self.layout.addLayout(self.search_bar)
        
        # Add add new client btn
        self.layout.addLayout(self.add_new_client())
        
        # Create a persistent result label
        self.result_label = QLabel()
        self.result_label.setFont(QFont('Arial', 14))
        self.result_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.result_label)  # Add it to the layout

        # Add a spacer to push content to the top
        self.layout.addStretch(1)

        # Set layout and window properties
        self.setLayout(self.layout)


    def add_top_label(self):
        # Create a label
        top_label = QLabel("Buscar por cliente")
        top_label.setFont(QFont('Arial', 24))  # Set font and size
        top_label.setAlignment(Qt.AlignCenter)  # Center the text
        top_label.setStyleSheet("padding: 10px;")

        # Add the label to the layout
        self.layout.addWidget(top_label)
        
    def add_new_client(self):
        new_client_layout = QHBoxLayout()
        new_client_layout.addStretch(1)
        home_button = QPushButton("Adicionar novo cliente")
        home_button.setFont(QFont('Arial', 18))
        home_button.setFixedHeight(40)
        home_button.setFixedWidth(600)
        home_button.setStyleSheet("""
            background-color: #007BFF;
            color: white;
            padding: 5px 15px; 
            border-radius: 10px; 
            border: 1px solid #CCC;
        """)
        home_button.setCursor(Qt.PointingHandCursor)
        home_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        
        new_client_layout.addWidget(home_button)
        new_client_layout.addStretch(1)
        
        return new_client_layout
        
    def create_search_bar(self):
        search_layout = QHBoxLayout()

        # Add a spacer to center the search bar
        search_layout.addStretch(1)

        # Create and add the search input
        search_input = QLineEdit()
        search_input.setPlaceholderText("Insira o nome do cliente...")
        search_input.setFont(QFont('Arial', 18))  # Increase the font size
        search_input.setFixedHeight(40)  # Increase the height of the search bar
        search_input.setFixedWidth(600)  # Increase the width of the search bar
        search_input.setStyleSheet("""
            padding: 5px 15px; 
            border-radius: 10px; 
            border: 1px solid #CCC;
        """)
        
        # Add the magnifier icon inside the input field
        search_input.addAction(QIcon('assets/icons/magnifier.png'), QLineEdit.TrailingPosition)
        
        # Connect signals for Enter key and text changes
        search_input.returnPressed.connect(self.on_enter_pressed)  # When Enter is pressed
        search_input.textChanged.connect(self.on_text_changed)  # When the text changes

        search_layout.addWidget(search_input)

        # Add a spacer to center the search bar
        search_layout.addStretch(1)

        return search_layout

    
    
    def update_search_result(self, text):
        # Update the text of the result label
        self.result_label.setText(f"Resultado para: {text}")
        
    def on_enter_pressed(self):
        # Handle when Enter is pressed
        search_text = self.sender().text()  # Get the text from the QLineEdit
        print(f"Enter pressed with text: {search_text}")
        self.update_search_result(search_text)  # Update the result label

    def on_text_changed(self, text):
        # Handle when the text changes
        print(f"Text changed: {text}")
        self.update_search_result(text)  # Update the result label
        
