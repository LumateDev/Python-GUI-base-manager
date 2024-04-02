import sys
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QFrame, QMessageBox, QTableWidgetItem

import main_ui
from main_ui import Ui_DB_app
from database_manager import *


class MainWindow(QWidget):

    def __init__(self):
        """
        Function which initialize window
        Args: none
        Return: none
        """
        super().__init__()
        self.ui = Ui_DB_app
        self.ui.setupUi(self)

