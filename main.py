import sys
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QFrame, QMessageBox, QTableWidgetItem

import database_manager
import main_ui
from main_ui import Ui_MainWindow
from database_manager import *


class MainWindow(QWidget):

    def __init__(self):
        """
        Function which initialize window
        Args: none
        Return: none
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Тут описать БД
        #self.db = database_manager.connection(connection)

        self.task_id = self.ui.spinBoxId
        #self.task_id.setValidator(QIntValidator)
        self.task_type = self.ui.comboBoxType
        self.task_difficult = self.ui.comboBoxDifficult
        self.task_theme = self.ui.comboBoxTheme

        self.button_add = self.ui.add_btn
        self.button_update = self.ui.update_btn
        self.button_select = self.ui.select_btn
        self.button_search = self.ui.search_btn
        self.button_remove = self.ui.remove_btn
        self.button_clear = self.ui.clear_btn

        self.result_table = self.ui.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.ui.function_frame.findChildren(QPushButton)

        self.init_signal_slot()
        # Loading data with open App
        self.search_info()
        self.update_info()


    def init_signal_slot(self):
        #connect buttons to their functions
        self.button_add.clicked.connect(self.add_info)
        self.button_update.clicked.connect(self.update_info)
        self.button_select.clicked.connect(self.select_info)
        self.button_search.clicked.connect(self.search_info)
        self.button_remove.clicked.connect(self.delete_info)
        self.button_clear.clicked.connect(self.clear_form_info)

    def update_info(self):
        print("Update button clicked")



    def add_info(self):
        print("Add button clicked")
        print(f"Data: {self.task_id.value()}, {self.task_type}, {self.task_theme}, {self.task_difficult}")

    def search_info(self):
        print("Search button clicked")

    def clear_form_info(self):
        print("Clear button clicked")
    def select_info(self):
        print("Select button clicked")
    def delete_info(self):
        print("Delete button clicked")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
