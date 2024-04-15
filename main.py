import os.path
import sys

from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QIcon

import database_manager
from main_ui import Ui_MainWindow
import qdarktheme


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        icon = QIcon("./icons/title_icon.svg")
        self.setWindowIcon(icon)
        self.setFixedSize(960, 810)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        file_path = "TasksBase.DB"
        flag = False
        if os.path.isfile(file_path):
            flag = True

        self.connect = database_manager.sql_connection()
        if not flag:
            database_manager.init_db(self.connect)

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

        self.radioDark = self.ui.radioButtonDark
        self.radioLight = self.ui.radioButtonLight
        self.table = self.ui.tableWidget
        self.table.setAutoScroll(True)
        self.data = []

        if app.styleSheet() == qdarktheme.load_stylesheet("dark"):
            self.radioDark.setChecked(True)
        else:
            self.radioLight.setChecked(True)

        self.init_signal_slot()
        self.update_info()

    def init_signal_slot(self):
        self.button_add.clicked.connect(self.add_info)
        self.button_update.clicked.connect(self.edit_info)
        self.button_select.clicked.connect(self.select_info)
        self.button_search.clicked.connect(self.search_info)
        self.button_remove.clicked.connect(self.delete_info)
        self.button_clear.clicked.connect(self.clear_form_info)

        self.radioDark.toggled.connect(self.set_dark_theme)
        self.radioLight.toggled.connect(self.set_light_theme)

    def update_info(self):
        self.data = database_manager.get_all_tasks(self.connect)

        for task in self.data:
            item = QTableWidgetItem(str(task))
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            for idx, value in enumerate(task):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row_position, idx, item)

    def add_info(self):

        if not (self.task_type.currentText() and self.task_theme.currentText() and self.task_difficult.currentText() and self.task_text.toPlainText()):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText("Заполните все поля")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            database_manager.add_task(self.connect, self.task_type.currentText(), self.task_theme.currentText(), self.task_text.toPlainText(), self.task_difficult.currentText())
            self.table.setRowCount(0)
            self.update_info()

    def search_info(self):

        row_index = self.task_id.value()
        if not row_index:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Необходимо указать ID')
            msg.setWindowTitle("Error")
            msg.exec_()
        if len(self.data) < row_index:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText(f"Записи с {row_index} не существует ")
            msg.setWindowTitle("Error")
            msg.exec_()

        column = 0
        index = self.table.model().index(row_index-1, column)
        self.table.scrollTo(index)
        self.table.setCurrentCell(row_index,0)

    def clear_form_info(self):

        database_manager.drop_all_tables(self.connect)
        self.table.setRowCount(0)
        self.update_info()

    def edit_info(self):

        if not (self.task_id.value() and self.task_type.currentText() and self.task_theme.currentText() and self.task_difficult.currentText() and self.task_text.toPlainText()):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText("Заполните все поля")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:

            database_manager.update_task(self.connect,self.task_id.value(), self.task_type.currentText(), self.task_theme.currentText(),
                                  self.task_text.toPlainText(), self.task_difficult.currentText())
            self.table.setRowCount(0)
            self.update_info()

    def select_info(self):
        row = self.table.currentIndex().row()
        active_row_index = self.table.model().index(row, 0).data()
        print(active_row_index)
        data_by_id = database_manager.get_task_by_id(self.connect, active_row_index)
        print(data_by_id)

        self.task_id.setValue(data_by_id[0])
        self.task_type.setCurrentIndex(data_by_id[1]-1)
        self.task_theme.setCurrentIndex(data_by_id[2]-1)
        self.task_text.setPlainText(data_by_id[3])
        self.task_difficult.setCurrentIndex(data_by_id[4]-1)

    def delete_info(self):

        if not self.task_id.value():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText("Укажите запись, которую нужно удалить")
            msg.setWindowTitle("Error")
            msg.exec_()

        else:
            database_manager.delete_task(self.connect, self.task_id.value())
            self.table.setRowCount(0)
            self.update_info()
            self.task_id.setValue(0)
            self.task_type.setCurrentIndex(0)
            self.task_theme.setCurrentIndex(0)
            self.task_text.setPlainText("")
            self.task_difficult.setCurrentIndex(0)

    def set_dark_theme(self):
        app.setStyleSheet(qdarktheme.load_stylesheet("dark"))

    def set_light_theme(self):
        app.setStyleSheet(qdarktheme.load_stylesheet("light"))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet("dark"))
    window = MainWindow()
    window.setWindowTitle("Database UI app")
    window.show()
    sys.exit(app.exec())
