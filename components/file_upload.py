import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog
)
from PyQt5.QtGui import QFont, QDragEnterEvent, QDropEvent
from PyQt5.QtCore import Qt, QMimeData

class FileUploadWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.load_document())
        self.setLayout(self.layout)

        # Enable drag and drop
        self.setAcceptDrops(True)
    
    def load_document(self):
        new_document_layout = QHBoxLayout()

        # Add a stretch to center the button
        new_document_layout.addStretch(1)

        # Create the "Add new document" button
        upload_button = QPushButton("Adicionar novo documento")
        upload_button.setFont(QFont('Arial', 18))
        upload_button.setFixedHeight(40)
        upload_button.setFixedWidth(600)
        upload_button.setStyleSheet("""
            background-color: #007BFF;
            color: white;
            padding: 5px 15px; 
            border-radius: 10px; 
            border: 1px solid #CCC;
        """)
        upload_button.setCursor(Qt.PointingHandCursor)

        # Connect the button to open a file dialog
        upload_button.clicked.connect(self.open_file_dialog)

        # Add the button to the layout
        new_document_layout.addWidget(upload_button)

        # Add a stretch to center the button
        new_document_layout.addStretch(1)
        
        return new_document_layout
    
    def open_file_dialog(self):
        # Open the file explorer and allow the user to select a file
        file_name, _ = QFileDialog.getOpenFileName(self, "Selecionar arquivo", "", "All Files (*)")
        if file_name:
            print(f"File selected: {file_name}")  # Handle the file upload process

    # Handle drag-and-drop events
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            print(f"File dropped: {file_path}")  # Handle the file upload process