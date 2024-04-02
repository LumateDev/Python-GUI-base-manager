# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QHeaderView, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_DB_app(object):
    def setupUi(self, DB_app):
        if not DB_app.objectName():
            DB_app.setObjectName(u"DB_app")
        DB_app.resize(957, 840)
        DB_app.setAutoFillBackground(False)
        DB_app.setStyleSheet(u"QWidget {\n"
"background-color: #4D606E;\n"
"}\n"
"\n"
"#title_frame QFrame {\n"
"background-color: #D3D4D8;\n"
"border-radius:12px;\n"
"}\n"
"\n"
"#title_frame QLabel{\n"
"color: #000;\n"
"font:30px;\n"
"}\n"
"\n"
"#info_frame  {\n"
"background-color : #D3D4D8;\n"
"border-radius: 12px;\n"
"}\n"
"#info_frame QLabel  {\n"
"background-color : #D3D4D8;\n"
"color: #000;\n"
"font:24px;\n"
"}\n"
"#info_frame QComboBox, #info_frame QSpinBox, #info_frame QPlainTextEdit, #info_frame gridLayout_7{\n"
"  \n"
"  background-color: #D3D4D8;\n"
"  border: 2px solid #000;\n"
"  color: #000;\n"
"  border-radius: 6px;\n"
"  font: 24px;\n"
" \n"
"}\n"
"\n"
"#function_frame {\n"
"background-color : #D3D4D8;\n"
"border-radius: 12px;\n"
"}\n"
"#info_frame QSpinBox:focus,\n"
"#info_frame QComboBox:focus,\n"
"#info_frame QPlainTextEdit:focus\n"
" {\n"
"	border-color: #4c96f7;\n"
"}\n"
"\n"
"\n"
"#result_frame {\n"
"	border-radius: 5px;\n"
"	background-color: #D3D4D8;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	border: none;\n"
"	border"
                        "-bottom:1px solid black;\n"
"	text-align:left;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QTableWidget::Item{\n"
"	border-bottom:1px solid black;\n"
"border-right:1px solid black;\n"
"	color: black;\n"
"	padding-left: 3px;\n"
"}\n"
"QTableWidget{\n"
"background-color :#D3D4D8;\n"
"border-radius:4px;\n"
"border :2px solid black;\n"
"}\n"
"#function_frame QPushButton {\n"
"	font-size: 14px;\n"
"	padding: 5px 10px;\n"
"	border: 2px solid #000;\n"
"	border-radius: 5px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#function_frame QPushButton:hover {\n"
"	border-color: #4c96f7;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        DB_app.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(DB_app)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title_frame = QFrame(self.centralwidget)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setGeometry(QRect(10, 10, 941, 60))
        self.title_frame.setStyleSheet(u"")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.title_label = QLabel(self.title_frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(0, 0, 941, 61))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setBold(False)
        font.setItalic(False)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.info_frame = QFrame(self.centralwidget)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setGeometry(QRect(10, 80, 941, 281))
        self.info_frame.setStyleSheet(u"")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.comboBox_4 = QComboBox(self.info_frame)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(670, 20, 241, 41))
        self.label_2 = QLabel(self.info_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 20, 120, 40))
        self.spinBox = QSpinBox(self.info_frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(190, 20, 240, 40))
        self.comboBox = QComboBox(self.info_frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(670, 70, 241, 41))
        self.label_5 = QLabel(self.info_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(510, 20, 131, 40))
        self.label_6 = QLabel(self.info_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 70, 131, 40))
        self.comboBox_5 = QComboBox(self.info_frame)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(190, 70, 240, 40))
        self.comboBox_5.setIconSize(QSize(16, 16))
        self.label_task_text = QLabel(self.info_frame)
        self.label_task_text.setObjectName(u"label_task_text")
        self.label_task_text.setGeometry(QRect(29, 140, 141, 40))
        self.label_3 = QLabel(self.info_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(509, 70, 141, 40))
        self.plainTextEdit = QPlainTextEdit(self.info_frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(189, 140, 721, 120))
        self.function_frame = QFrame(self.centralwidget)
        self.function_frame.setObjectName(u"function_frame")
        self.function_frame.setGeometry(QRect(10, 370, 940, 80))
        self.function_frame.setStyleSheet(u"")
        self.function_frame.setFrameShape(QFrame.StyledPanel)
        self.function_frame.setFrameShadow(QFrame.Raised)
        self.add_btn = QPushButton(self.function_frame)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(5, 10, 150, 60))
        icon = QIcon()
        icon.addFile(u"icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_btn.setIcon(icon)
        self.add_btn.setIconSize(QSize(32, 32))
        self.update_btn = QPushButton(self.function_frame)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setGeometry(QRect(162, 10, 150, 60))
        icon1 = QIcon()
        icon1.addFile(u"icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.update_btn.setIcon(icon1)
        self.update_btn.setIconSize(QSize(32, 32))
        self.select_btn = QPushButton(self.function_frame)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setGeometry(QRect(317, 10, 150, 60))
        icon2 = QIcon()
        icon2.addFile(u"icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.select_btn.setIcon(icon2)
        self.select_btn.setIconSize(QSize(32, 32))
        self.search_btn = QPushButton(self.function_frame)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(472, 10, 150, 60))
        icon3 = QIcon()
        icon3.addFile(u"icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon3)
        self.search_btn.setIconSize(QSize(32, 32))
        self.clear_btn = QPushButton(self.function_frame)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(627, 10, 150, 60))
        icon4 = QIcon()
        icon4.addFile(u"icons/clear.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_btn.setIcon(icon4)
        self.clear_btn.setIconSize(QSize(32, 32))
        self.remove_btn = QPushButton(self.function_frame)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setGeometry(QRect(785, 10, 150, 60))
        icon5 = QIcon()
        icon5.addFile(u"icons/remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_btn.setIcon(icon5)
        self.remove_btn.setIconSize(QSize(32, 32))
        self.result_frame = QFrame(self.centralwidget)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setGeometry(QRect(10, 460, 940, 370))
        self.result_frame.setStyleSheet(u"")
        self.result_frame.setFrameShape(QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.result_frame)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font1 = QFont()
        font1.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem15)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(0, 0, 940, 370))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QSize(960, 16777215))
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setFrameShape(QFrame.Panel)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(24)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        DB_app.setCentralWidget(self.centralwidget)
        self.function_frame.raise_()
        self.title_frame.raise_()
        self.info_frame.raise_()
        self.result_frame.raise_()

        self.retranslateUi(DB_app)

        QMetaObject.connectSlotsByName(DB_app)
    # setupUi

    def retranslateUi(self, DB_app):
        DB_app.setWindowTitle(QCoreApplication.translate("DB_app", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("DB_app", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0437\u0430\u0434\u0430\u0447\u0430\u0445", None))
        self.label_2.setText(QCoreApplication.translate("DB_app", u"Id \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label_5.setText(QCoreApplication.translate("DB_app", u"\u0421\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("DB_app", u"\u0422\u0438\u043f \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label_task_text.setText(QCoreApplication.translate("DB_app", u"\u0422\u0435\u043a\u0441\u0442 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label_3.setText(QCoreApplication.translate("DB_app", u"\u0422\u0435\u043c\u0430 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.add_btn.setText(QCoreApplication.translate("DB_app", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.update_btn.setText(QCoreApplication.translate("DB_app", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.select_btn.setText(QCoreApplication.translate("DB_app", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.search_btn.setText(QCoreApplication.translate("DB_app", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.clear_btn.setText(QCoreApplication.translate("DB_app", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.remove_btn.setText(QCoreApplication.translate("DB_app", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DB_app", u"Id \u0417\u0430\u0434\u0430\u0447\u0438", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DB_app", u"\u0422\u0435\u043c\u0430 \u0437\u0430\u0434\u0430\u0447\u0438", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DB_app", u"\u0421\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0438", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DB_app", u"\u0422\u0438\u043f \u0437\u0430\u0434\u0430\u0447\u0438", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("DB_app", u"\u0422\u0435\u043a\u0441\u0442 \u0437\u0430\u0434\u0430\u0447\u0438", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("DB_app", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("DB_app", u"\u041d\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("DB_app", u"fdfd", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("DB_app", u"fdfd", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("DB_app", u"fdfd", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("DB_app", u"fdfdf", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("DB_app", u"fdfdf", None));
        ___qtablewidgetitem12 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("DB_app", u"54", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("DB_app", u"gdfg", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("DB_app", u"gdgfdg", None));
        ___qtablewidgetitem15 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("DB_app", u"gdfgd", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(statustip)
        self.tableWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
    # retranslateUi

