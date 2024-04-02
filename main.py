import sys

from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QFrame, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QIcon

import database_manager
from main_ui import Ui_MainWindow


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        icon = QIcon("./icons/title_icon.svg")
        self.setWindowIcon(icon)
        self.setFixedSize(960, 810)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.connect = database_manager.sql_connection()
        self.task_id = self.ui.spinBoxId
        self.task_type = self.ui.comboBoxType
        self.task_difficult = self.ui.comboBoxDifficult
        self.task_theme = self.ui.comboBoxTheme
        self.task_text = self.ui.plainTextEdit

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
        self.search_info()
        self.update_info()

    def init_signal_slot(self):
        self.button_add.clicked.connect(self.add_info)
        self.button_update.clicked.connect(self.update_info)
        self.button_select.clicked.connect(self.select_info)
        self.button_search.clicked.connect(self.search_info)
        self.button_remove.clicked.connect(self.delete_info)
        self.button_clear.clicked.connect(self.clear_form_info)

    def update_info(self):
        print("Update button clicked")

    def add_info(self):
        table_name = 'Новая_таблица'
        column_names = ['Имя', 'Возраст', 'Город']
        data_types = ['text', 'integer', 'text']
        print("Add button clicked")
        print(
            f"Data: {self.task_id.value()}, {self.task_type.currentText()}, {self.task_theme.currentText()}, {self.task_difficult.currentText()}, {self.task_text.toPlainText()}")

        database_manager.create_tables(self.connect, table_name, column_names, data_types)

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
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
