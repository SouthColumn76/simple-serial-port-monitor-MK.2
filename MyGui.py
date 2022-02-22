# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(721, 741)
        MainWindow.setMinimumSize(QSize(682, 582))
        MainWindow.setMaximumSize(QSize(721, 741))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 11, 702, 721))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.port_label = QLabel(self.widget)
        self.port_label.setObjectName(u"port_label")
        self.port_label.setMinimumSize(QSize(22, 23))
        self.port_label.setMaximumSize(QSize(22, 23))

        self.horizontalLayout.addWidget(self.port_label)

        self.port_box = QComboBox(self.widget)
        self.port_box.addItem("")
        self.port_box.addItem("")
        self.port_box.addItem("")
        self.port_box.addItem("")
        self.port_box.addItem("")
        self.port_box.setObjectName(u"port_box")
        self.port_box.setMinimumSize(QSize(62, 20))
        self.port_box.setMaximumSize(QSize(62, 20))

        self.horizontalLayout.addWidget(self.port_box)

        self.baud_label = QLabel(self.widget)
        self.baud_label.setObjectName(u"baud_label")
        self.baud_label.setMinimumSize(QSize(29, 23))
        self.baud_label.setMaximumSize(QSize(29, 23))

        self.horizontalLayout.addWidget(self.baud_label)

        self.baud_box = QComboBox(self.widget)
        self.baud_box.addItem("")
        self.baud_box.addItem("")
        self.baud_box.addItem("")
        self.baud_box.addItem("")
        self.baud_box.addItem("")
        self.baud_box.addItem("")
        self.baud_box.addItem("")
        self.baud_box.setObjectName(u"baud_box")
        self.baud_box.setMinimumSize(QSize(63, 20))
        self.baud_box.setMaximumSize(QSize(63, 20))

        self.horizontalLayout.addWidget(self.baud_box)

        self.data_label = QLabel(self.widget)
        self.data_label.setObjectName(u"data_label")
        self.data_label.setMinimumSize(QSize(25, 23))
        self.data_label.setMaximumSize(QSize(25, 23))

        self.horizontalLayout.addWidget(self.data_label)

        self.data_box = QComboBox(self.widget)
        self.data_box.addItem("")
        self.data_box.addItem("")
        self.data_box.addItem("")
        self.data_box.addItem("")
        self.data_box.setObjectName(u"data_box")
        self.data_box.setMinimumSize(QSize(33, 20))
        self.data_box.setMaximumSize(QSize(33, 20))

        self.horizontalLayout.addWidget(self.data_box)

        self.stop_label = QLabel(self.widget)
        self.stop_label.setObjectName(u"stop_label")
        self.stop_label.setMinimumSize(QSize(25, 23))
        self.stop_label.setMaximumSize(QSize(25, 23))

        self.horizontalLayout.addWidget(self.stop_label)

        self.stop_box = QComboBox(self.widget)
        self.stop_box.addItem("")
        self.stop_box.addItem("")
        self.stop_box.addItem("")
        self.stop_box.setObjectName(u"stop_box")
        self.stop_box.setMinimumSize(QSize(43, 20))
        self.stop_box.setMaximumSize(QSize(43, 20))

        self.horizontalLayout.addWidget(self.stop_box)

        self.parity_label = QLabel(self.widget)
        self.parity_label.setObjectName(u"parity_label")
        self.parity_label.setMinimumSize(QSize(32, 23))
        self.parity_label.setMaximumSize(QSize(32, 23))

        self.horizontalLayout.addWidget(self.parity_label)

        self.parity_box = QComboBox(self.widget)
        self.parity_box.addItem("")
        self.parity_box.addItem("")
        self.parity_box.addItem("")
        self.parity_box.addItem("")
        self.parity_box.addItem("")
        self.parity_box.setObjectName(u"parity_box")
        self.parity_box.setMinimumSize(QSize(62, 20))
        self.parity_box.setMaximumSize(QSize(62, 20))

        self.horizontalLayout.addWidget(self.parity_box)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.connect_button = QPushButton(self.widget)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setMinimumSize(QSize(75, 23))
        self.connect_button.setMaximumSize(QSize(75, 23))

        self.horizontalLayout.addWidget(self.connect_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.protocol_label = QLabel(self.widget)
        self.protocol_label.setObjectName(u"protocol_label")
        self.protocol_label.setMinimumSize(QSize(46, 20))
        self.protocol_label.setMaximumSize(QSize(46, 20))

        self.horizontalLayout_2.addWidget(self.protocol_label)

        self.protocol_box = QComboBox(self.widget)
        self.protocol_box.addItem("")
        self.protocol_box.addItem("")
        self.protocol_box.addItem("")
        self.protocol_box.setObjectName(u"protocol_box")
        self.protocol_box.setMinimumSize(QSize(72, 20))
        self.protocol_box.setMaximumSize(QSize(72, 20))

        self.horizontalLayout_2.addWidget(self.protocol_box)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.dle_label = QLabel(self.widget)
        self.dle_label.setObjectName(u"dle_label")
        self.dle_label.setMinimumSize(QSize(23, 20))
        self.dle_label.setMaximumSize(QSize(23, 20))

        self.horizontalLayout_2.addWidget(self.dle_label)

        self.dle_text = QLineEdit(self.widget)
        self.dle_text.setObjectName(u"dle_text")
        self.dle_text.setEnabled(False)
        self.dle_text.setMinimumSize(QSize(21, 20))
        self.dle_text.setMaximumSize(QSize(21, 20))
        self.dle_text.setMaxLength(2)
        self.dle_text.setFrame(True)
        self.dle_text.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.dle_text)

        self.stx_label = QLabel(self.widget)
        self.stx_label.setObjectName(u"stx_label")
        self.stx_label.setMinimumSize(QSize(24, 20))
        self.stx_label.setMaximumSize(QSize(24, 20))

        self.horizontalLayout_2.addWidget(self.stx_label)

        self.stx_text = QLineEdit(self.widget)
        self.stx_text.setObjectName(u"stx_text")
        self.stx_text.setEnabled(False)
        self.stx_text.setMinimumSize(QSize(21, 20))
        self.stx_text.setMaximumSize(QSize(21, 20))
        self.stx_text.setMaxLength(2)
        self.stx_text.setFrame(True)
        self.stx_text.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.stx_text)

        self.etx_label = QLabel(self.widget)
        self.etx_label.setObjectName(u"etx_label")
        self.etx_label.setMinimumSize(QSize(24, 20))
        self.etx_label.setMaximumSize(QSize(24, 20))

        self.horizontalLayout_2.addWidget(self.etx_label)

        self.etx_text = QLineEdit(self.widget)
        self.etx_text.setObjectName(u"etx_text")
        self.etx_text.setEnabled(False)
        self.etx_text.setMinimumSize(QSize(21, 20))
        self.etx_text.setMaximumSize(QSize(21, 20))
        self.etx_text.setMaxLength(2)
        self.etx_text.setFrame(True)
        self.etx_text.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.etx_text)

        self.datalength_label = QLabel(self.widget)
        self.datalength_label.setObjectName(u"datalength_label")
        self.datalength_label.setMinimumSize(QSize(67, 20))
        self.datalength_label.setMaximumSize(QSize(67, 20))

        self.horizontalLayout_2.addWidget(self.datalength_label)

        self.datalength_text = QLineEdit(self.widget)
        self.datalength_text.setObjectName(u"datalength_text")
        self.datalength_text.setEnabled(True)
        self.datalength_text.setMinimumSize(QSize(41, 20))
        self.datalength_text.setMaximumSize(QSize(41, 20))
        self.datalength_text.setMaxLength(4)
        self.datalength_text.setFrame(True)
        self.datalength_text.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.datalength_text)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.format_label = QLabel(self.widget)
        self.format_label.setObjectName(u"format_label")
        self.format_label.setMinimumSize(QSize(39, 21))
        self.format_label.setMaximumSize(QSize(39, 21))
        self.format_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.format_label)

        self.format_box = QComboBox(self.widget)
        self.format_box.addItem("")
        self.format_box.addItem("")
        self.format_box.addItem("")
        self.format_box.setObjectName(u"format_box")
        self.format_box.setMinimumSize(QSize(57, 20))
        self.format_box.setMaximumSize(QSize(57, 20))

        self.horizontalLayout_3.addWidget(self.format_box)

        self.clear_button = QPushButton(self.widget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setMinimumSize(QSize(75, 23))
        self.clear_button.setMaximumSize(QSize(75, 23))

        self.horizontalLayout_3.addWidget(self.clear_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.outlier_checking_button = QCheckBox(self.widget)
        self.outlier_checking_button.setObjectName(u"outlier_checking_button")
        self.outlier_checking_button.setMinimumSize(QSize(121, 16))
        self.outlier_checking_button.setMaximumSize(QSize(121, 16))

        self.horizontalLayout_5.addWidget(self.outlier_checking_button)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_4)

        self.sampling_label = QLabel(self.widget)
        self.sampling_label.setObjectName(u"sampling_label")
        self.sampling_label.setMinimumSize(QSize(81, 16))
        self.sampling_label.setMaximumSize(QSize(81, 16))

        self.horizontalLayout_5.addWidget(self.sampling_label)

        self.sampling_box = QComboBox(self.widget)
        self.sampling_box.addItem("")
        self.sampling_box.addItem("")
        self.sampling_box.addItem("")
        self.sampling_box.addItem("")
        self.sampling_box.setObjectName(u"sampling_box")
        self.sampling_box.setEnabled(False)
        self.sampling_box.setMinimumSize(QSize(61, 21))
        self.sampling_box.setMaximumSize(QSize(61, 21))
        self.sampling_box.setEditable(False)

        self.horizontalLayout_5.addWidget(self.sampling_box)

        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.recieved_label = QLabel(self.widget)
        self.recieved_label.setObjectName(u"recieved_label")
        self.recieved_label.setMinimumSize(QSize(61, 16))
        self.recieved_label.setMaximumSize(QSize(61, 16))

        self.horizontalLayout_5.addWidget(self.recieved_label)

        self.recieved_text = QLineEdit(self.widget)
        self.recieved_text.setObjectName(u"recieved_text")
        self.recieved_text.setEnabled(False)
        self.recieved_text.setMinimumSize(QSize(51, 20))
        self.recieved_text.setMaximumSize(QSize(51, 20))
        self.recieved_text.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.recieved_text.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.recieved_text)

        self.horizontalSpacer_4 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.outliers_label = QLabel(self.widget)
        self.outliers_label.setObjectName(u"outliers_label")
        self.outliers_label.setMinimumSize(QSize(43, 21))
        self.outliers_label.setMaximumSize(QSize(43, 21))

        self.horizontalLayout_5.addWidget(self.outliers_label)

        self.outliers_text = QLineEdit(self.widget)
        self.outliers_text.setObjectName(u"outliers_text")
        self.outliers_text.setEnabled(False)
        self.outliers_text.setMinimumSize(QSize(51, 20))
        self.outliers_text.setMaximumSize(QSize(51, 20))
        self.outliers_text.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.outliers_text.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.outliers_text)

        self.horizontalSpacer_5 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.ratio_label = QLabel(self.widget)
        self.ratio_label.setObjectName(u"ratio_label")
        self.ratio_label.setMinimumSize(QSize(28, 21))
        self.ratio_label.setMaximumSize(QSize(28, 21))

        self.horizontalLayout_5.addWidget(self.ratio_label)

        self.ratio_text = QLineEdit(self.widget)
        self.ratio_text.setObjectName(u"ratio_text")
        self.ratio_text.setEnabled(False)
        self.ratio_text.setMinimumSize(QSize(51, 20))
        self.ratio_text.setMaximumSize(QSize(51, 20))
        self.ratio_text.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ratio_text.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.ratio_text)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.command_label = QLabel(self.widget)
        self.command_label.setObjectName(u"command_label")
        self.command_label.setMinimumSize(QSize(61, 16))
        self.command_label.setMaximumSize(QSize(61, 16))

        self.horizontalLayout_4.addWidget(self.command_label)

        self.line_5 = QFrame(self.widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_5)

        self.change_data_length_label = QLabel(self.widget)
        self.change_data_length_label.setObjectName(u"change_data_length_label")
        self.change_data_length_label.setMinimumSize(QSize(121, 16))
        self.change_data_length_label.setMaximumSize(QSize(121, 16))

        self.horizontalLayout_4.addWidget(self.change_data_length_label)

        self.change_data_length_text = QLineEdit(self.widget)
        self.change_data_length_text.setObjectName(u"change_data_length_text")
        self.change_data_length_text.setEnabled(False)
        self.change_data_length_text.setMinimumSize(QSize(41, 20))
        self.change_data_length_text.setMaximumSize(QSize(41, 20))
        self.change_data_length_text.setMaxLength(4)
        self.change_data_length_text.setFrame(True)
        self.change_data_length_text.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.change_data_length_text)

        self.change_sampling_rate_label = QLabel(self.widget)
        self.change_sampling_rate_label.setObjectName(u"change_sampling_rate_label")
        self.change_sampling_rate_label.setMinimumSize(QSize(141, 16))
        self.change_sampling_rate_label.setMaximumSize(QSize(141, 16))

        self.horizontalLayout_4.addWidget(self.change_sampling_rate_label)

        self.change_sampling_rate_box = QComboBox(self.widget)
        self.change_sampling_rate_box.addItem("")
        self.change_sampling_rate_box.addItem("")
        self.change_sampling_rate_box.addItem("")
        self.change_sampling_rate_box.addItem("")
        self.change_sampling_rate_box.setObjectName(u"change_sampling_rate_box")
        self.change_sampling_rate_box.setEnabled(False)
        self.change_sampling_rate_box.setMinimumSize(QSize(61, 21))
        self.change_sampling_rate_box.setMaximumSize(QSize(61, 21))
        self.change_sampling_rate_box.setEditable(False)

        self.horizontalLayout_4.addWidget(self.change_sampling_rate_box)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.send_button = QPushButton(self.widget)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setEnabled(False)
        self.send_button.setMinimumSize(QSize(75, 23))
        self.send_button.setMaximumSize(QSize(75, 23))

        self.horizontalLayout_4.addWidget(self.send_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.packet_list_widget = QListWidget(self.widget)
        self.packet_list_widget.setObjectName(u"packet_list_widget")
        self.packet_list_widget.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout.addWidget(self.packet_list_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.port_box, self.baud_box)
        QWidget.setTabOrder(self.baud_box, self.data_box)
        QWidget.setTabOrder(self.data_box, self.stop_box)
        QWidget.setTabOrder(self.stop_box, self.parity_box)
        QWidget.setTabOrder(self.parity_box, self.connect_button)
        QWidget.setTabOrder(self.connect_button, self.protocol_box)
        QWidget.setTabOrder(self.protocol_box, self.dle_text)
        QWidget.setTabOrder(self.dle_text, self.stx_text)
        QWidget.setTabOrder(self.stx_text, self.etx_text)
        QWidget.setTabOrder(self.etx_text, self.datalength_text)
        QWidget.setTabOrder(self.datalength_text, self.clear_button)

        self.retranslateUi(MainWindow)

        self.port_box.setCurrentIndex(-1)
        self.baud_box.setCurrentIndex(3)
        self.data_box.setCurrentIndex(3)
        self.sampling_box.setCurrentIndex(-1)
        self.change_sampling_rate_box.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.port_label.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.port_box.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.port_box.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.port_box.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.port_box.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.port_box.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))

        self.baud_label.setText(QCoreApplication.translate("MainWindow", u"Baud", None))
        self.baud_box.setItemText(0, QCoreApplication.translate("MainWindow", u"1200", None))
        self.baud_box.setItemText(1, QCoreApplication.translate("MainWindow", u"2400", None))
        self.baud_box.setItemText(2, QCoreApplication.translate("MainWindow", u"4800", None))
        self.baud_box.setItemText(3, QCoreApplication.translate("MainWindow", u"9600", None))
        self.baud_box.setItemText(4, QCoreApplication.translate("MainWindow", u"14400", None))
        self.baud_box.setItemText(5, QCoreApplication.translate("MainWindow", u"19200", None))
        self.baud_box.setItemText(6, QCoreApplication.translate("MainWindow", u"115200", None))

        self.data_label.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.data_box.setItemText(0, QCoreApplication.translate("MainWindow", u"5", None))
        self.data_box.setItemText(1, QCoreApplication.translate("MainWindow", u"6", None))
        self.data_box.setItemText(2, QCoreApplication.translate("MainWindow", u"7", None))
        self.data_box.setItemText(3, QCoreApplication.translate("MainWindow", u"8", None))

        self.stop_label.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.stop_box.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.stop_box.setItemText(1, QCoreApplication.translate("MainWindow", u"1.5", None))
        self.stop_box.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.parity_label.setText(QCoreApplication.translate("MainWindow", u"Parity", None))
        self.parity_box.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.parity_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Even", None))
        self.parity_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Odd", None))
        self.parity_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Mark", None))
        self.parity_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Space", None))

        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.protocol_label.setText(QCoreApplication.translate("MainWindow", u"Protocol", None))
        self.protocol_box.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.protocol_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Static", None))
        self.protocol_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Variable", None))

        self.dle_label.setText(QCoreApplication.translate("MainWindow", u"DLE", None))
        self.dle_text.setText("")
        self.stx_label.setText(QCoreApplication.translate("MainWindow", u"STX", None))
        self.etx_label.setText(QCoreApplication.translate("MainWindow", u"ETX", None))
        self.datalength_label.setText(QCoreApplication.translate("MainWindow", u"Data Length", None))
        self.datalength_text.setText("")
        self.format_label.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.format_box.setItemText(0, QCoreApplication.translate("MainWindow", u"ASCII", None))
        self.format_box.setItemText(1, QCoreApplication.translate("MainWindow", u"HEX", None))
        self.format_box.setItemText(2, QCoreApplication.translate("MainWindow", u"DEC", None))

        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Log Clear", None))
        self.outlier_checking_button.setText(QCoreApplication.translate("MainWindow", u"Outlier Checking", None))
        self.sampling_label.setText(QCoreApplication.translate("MainWindow", u"Sampling Rate", None))
        self.sampling_box.setItemText(0, QCoreApplication.translate("MainWindow", u"1Hz", None))
        self.sampling_box.setItemText(1, QCoreApplication.translate("MainWindow", u"2Hz", None))
        self.sampling_box.setItemText(2, QCoreApplication.translate("MainWindow", u"10Hz", None))
        self.sampling_box.setItemText(3, QCoreApplication.translate("MainWindow", u"20Hz", None))

        self.recieved_label.setText(QCoreApplication.translate("MainWindow", u"Recieved", None))
        self.outliers_label.setText(QCoreApplication.translate("MainWindow", u"Outliers", None))
        self.ratio_label.setText(QCoreApplication.translate("MainWindow", u"Ratio", None))
        self.command_label.setText(QCoreApplication.translate("MainWindow", u"Command", None))
        self.change_data_length_label.setText(QCoreApplication.translate("MainWindow", u"Change Data Length", None))
        self.change_data_length_text.setText("")
        self.change_sampling_rate_label.setText(QCoreApplication.translate("MainWindow", u"Change Sampling  Rate", None))
        self.change_sampling_rate_box.setItemText(0, QCoreApplication.translate("MainWindow", u"1Hz", None))
        self.change_sampling_rate_box.setItemText(1, QCoreApplication.translate("MainWindow", u"2Hz", None))
        self.change_sampling_rate_box.setItemText(2, QCoreApplication.translate("MainWindow", u"10Hz", None))
        self.change_sampling_rate_box.setItemText(3, QCoreApplication.translate("MainWindow", u"20Hz", None))

        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

