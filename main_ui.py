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
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 840)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QTableWidget {\n"
"	margin-bottom : 20px;\n"
"}")
#        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title_frame = QFrame(self.centralwidget)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setGeometry(QRect(10, 10, 941, 60))
        self.title_frame.setStyleSheet(u"")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.title_frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 941, 51))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.title_label = QLabel(self.layoutWidget)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButtonDark = QRadioButton(self.layoutWidget)
        self.radioButtonDark.setObjectName(u"radioButtonDark")
        font1 = QFont()
        font1.setPointSize(16)
        self.radioButtonDark.setFont(font1)

        self.horizontalLayout.addWidget(self.radioButtonDark)

        self.radioButtonLight = QRadioButton(self.layoutWidget)
        self.radioButtonLight.setObjectName(u"radioButtonLight")
        self.radioButtonLight.setFont(font1)

        self.horizontalLayout.addWidget(self.radioButtonLight)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.info_frame = QFrame(self.centralwidget)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setGeometry(QRect(10, 80, 941, 281))
        self.info_frame.setStyleSheet(u"")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.comboBoxDifficult = QComboBox(self.info_frame)
        self.comboBoxDifficult.addItem("")
        self.comboBoxDifficult.addItem("")
        self.comboBoxDifficult.addItem("")
        self.comboBoxDifficult.addItem("")
        self.comboBoxDifficult.setObjectName(u"comboBoxDifficult")
        self.comboBoxDifficult.setEnabled(True)
        self.comboBoxDifficult.setGeometry(QRect(670, 20, 241, 41))
        self.comboBoxDifficult.setFont(font1)
        self.comboBoxDifficult.setAutoFillBackground(False)
        self.label_2 = QLabel(self.info_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(29, 20, 151, 40))
        self.label_2.setFont(font1)
        self.spinBoxId = QSpinBox(self.info_frame)
        self.spinBoxId.setObjectName(u"spinBoxId")
        self.spinBoxId.setGeometry(QRect(190, 20, 240, 40))
        self.spinBoxId.setFont(font1)
        self.comboBoxTheme = QComboBox(self.info_frame)
        self.comboBoxTheme.addItem("")
        self.comboBoxTheme.addItem("")
        self.comboBoxTheme.addItem("")
        self.comboBoxTheme.addItem("")
        self.comboBoxTheme.addItem("")
        self.comboBoxTheme.addItem("")
        self.comboBoxTheme.addItem("")
        self.comboBoxTheme.addItem("")
        self.comboBoxTheme.addItem("")
        self.comboBoxTheme.addItem("")
        self.comboBoxTheme.setObjectName(u"comboBoxTheme")
        self.comboBoxTheme.setGeometry(QRect(670, 70, 241, 41))
        self.comboBoxTheme.setFont(font1)
        self.label_5 = QLabel(self.info_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(510, 20, 131, 40))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.info_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 70, 141, 40))
        self.label_6.setFont(font1)
        self.comboBoxType = QComboBox(self.info_frame)
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.comboBoxType.setObjectName(u"comboBoxType")
        self.comboBoxType.setGeometry(QRect(190, 70, 240, 40))
        self.comboBoxType.setFont(font1)
        self.comboBoxType.setIconSize(QSize(16, 16))
        self.label_task_text = QLabel(self.info_frame)
        self.label_task_text.setObjectName(u"label_task_text")
        self.label_task_text.setGeometry(QRect(29, 140, 141, 40))
        self.label_task_text.setFont(font1)
        self.label_3 = QLabel(self.info_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(509, 70, 141, 40))
        self.label_3.setFont(font1)
        self.plainTextEdit = QPlainTextEdit(self.info_frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(189, 140, 721, 120))
        self.plainTextEdit.setFont(font1)
        self.function_frame = QFrame(self.centralwidget)
        self.function_frame.setObjectName(u"function_frame")
        self.function_frame.setGeometry(QRect(10, 370, 940, 80))
        self.function_frame.setStyleSheet(u"")
        self.function_frame.setFrameShape(QFrame.StyledPanel)
        self.function_frame.setFrameShadow(QFrame.Raised)
        self.add_btn = QPushButton(self.function_frame)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(5, 10, 150, 60))
        font2 = QFont()
        font2.setPointSize(14)
        self.add_btn.setFont(font2)
        icon = QIcon()
        icon.addFile(u"icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_btn.setIcon(icon)
        self.add_btn.setIconSize(QSize(32, 32))
        self.update_btn = QPushButton(self.function_frame)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setGeometry(QRect(162, 10, 150, 60))
        self.update_btn.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u"icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.update_btn.setIcon(icon1)
        self.update_btn.setIconSize(QSize(32, 32))
        self.select_btn = QPushButton(self.function_frame)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setGeometry(QRect(317, 10, 150, 60))
        self.select_btn.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u"icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.select_btn.setIcon(icon2)
        self.select_btn.setIconSize(QSize(32, 32))
        self.search_btn = QPushButton(self.function_frame)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(472, 10, 150, 60))
        self.search_btn.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u"icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon3)
        self.search_btn.setIconSize(QSize(32, 32))
        self.clear_btn = QPushButton(self.function_frame)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setGeometry(QRect(627, 10, 150, 60))
        self.clear_btn.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u"icons/clear.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_btn.setIcon(icon4)
        self.clear_btn.setIconSize(QSize(32, 32))
        self.remove_btn = QPushButton(self.function_frame)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setGeometry(QRect(785, 10, 150, 60))
        self.remove_btn.setFont(font2)
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
        font3 = QFont()
        font3.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem2.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem3.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem4.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(0, 0, 940, 370))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QSize(960, 16777215))
        self.tableWidget.setFont(font3)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
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
#        MainWindow.setCentralWidget(self.centralwidget)
        self.function_frame.raise_()
        self.title_frame.raise_()
        self.info_frame.raise_()
        self.result_frame.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0437\u0430\u0434\u0430\u0447\u0430\u0445", None))
        self.radioButtonDark.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0451\u043c\u043d\u0430\u044f \u0442\u0435\u043c\u0430", None))
        self.radioButtonLight.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f \u0442\u0435\u043c\u0430", None))
        self.comboBoxDifficult.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0433\u043a\u043e", None))
        self.comboBoxDifficult.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f", None))
        self.comboBoxDifficult.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0436\u043d\u0430\u044f", None))
        self.comboBoxDifficult.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0425\u0430\u0440\u0434", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Id \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.comboBoxTheme.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBoxTheme.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBoxTheme.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBoxTheme.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBoxTheme.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBoxTheme.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBoxTheme.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBoxTheme.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBoxTheme.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBoxTheme.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.comboBoxType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0430\u0448\u043dee \u0437\u0430\u0434\u0430\u043d\u0438\u0435", None))
        self.comboBoxType.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0430\u043c\u043e\u0441\u0442\u043e\u044f\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430", None))
        self.comboBoxType.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430", None))

        self.label_task_text.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430 \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.select_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.remove_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id \u0417\u0430\u0434\u0430\u0447\u0438", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0437\u0430\u0434\u0430\u0447\u0438", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u0430 \u0437\u0430\u0434\u0430\u0447\u0438", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u0437\u0430\u0434\u0430\u0447\u0438", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0438", None));
#if QT_CONFIG(statustip)
        self.tableWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
    # retranslateUi

