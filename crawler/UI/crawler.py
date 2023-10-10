# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crawler.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import icons_rc

class Ui_W_CRAWLER(object):
    def setupUi(self, W_CRAWLER):
        if not W_CRAWLER.objectName():
            W_CRAWLER.setObjectName(u"W_CRAWLER")
        W_CRAWLER.resize(1108, 708)
        self.gridLayout = QGridLayout(W_CRAWLER)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_worksapce = QGroupBox(W_CRAWLER)
        self.gb_worksapce.setObjectName(u"gb_worksapce")
        self.gb_worksapce.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.gb_worksapce)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lw_file_list = QListWidget(self.gb_worksapce)
        self.lw_file_list.setObjectName(u"lw_file_list")

        self.gridLayout_2.addWidget(self.lw_file_list, 2, 4, 1, 1)

        self.le_check_result = QLineEdit(self.gb_worksapce)
        self.le_check_result.setObjectName(u"le_check_result")
        self.le_check_result.setEnabled(False)

        self.gridLayout_2.addWidget(self.le_check_result, 6, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.groupBox = QGroupBox(self.gb_worksapce)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lb_from = QLabel(self.groupBox)
        self.lb_from.setObjectName(u"lb_from")

        self.gridLayout_3.addWidget(self.lb_from, 0, 0, 1, 1)

        self.lb_to = QLabel(self.groupBox)
        self.lb_to.setObjectName(u"lb_to")

        self.gridLayout_3.addWidget(self.lb_to, 1, 0, 1, 1)

        self.le_check_files = QLineEdit(self.groupBox)
        self.le_check_files.setObjectName(u"le_check_files")
        self.le_check_files.setEnabled(False)

        self.gridLayout_3.addWidget(self.le_check_files, 4, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.pb_crawling = QPushButton(self.groupBox)
        self.pb_crawling.setObjectName(u"pb_crawling")
        self.pb_crawling.setEnabled(True)

        self.gridLayout_3.addWidget(self.pb_crawling, 3, 0, 1, 3)

        self.pb_processing = QPushButton(self.groupBox)
        self.pb_processing.setObjectName(u"pb_processing")
        self.pb_processing.setEnabled(False)
        self.pb_processing.setCheckable(False)
        self.pb_processing.setAutoDefault(False)
        self.pb_processing.setFlat(False)

        self.gridLayout_3.addWidget(self.pb_processing, 5, 0, 1, 3)

        self.dte_from = QDateTimeEdit(self.groupBox)
        self.dte_from.setObjectName(u"dte_from")
        self.dte_from.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.dte_from.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.dte_from, 0, 1, 1, 2)

        self.dte_to = QDateTimeEdit(self.groupBox)
        self.dte_to.setObjectName(u"dte_to")
        self.dte_to.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.dte_to.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.dte_to, 1, 1, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 4)

        self.cb_rule1 = QCheckBox(self.gb_worksapce)
        self.cb_rule1.setObjectName(u"cb_rule1")

        self.gridLayout_2.addWidget(self.cb_rule1, 0, 0, 1, 1)

        self.cb_rule2 = QCheckBox(self.gb_worksapce)
        self.cb_rule2.setObjectName(u"cb_rule2")

        self.gridLayout_2.addWidget(self.cb_rule2, 0, 1, 1, 1)

        self.cb_rule3 = QCheckBox(self.gb_worksapce)
        self.cb_rule3.setObjectName(u"cb_rule3")

        self.gridLayout_2.addWidget(self.cb_rule3, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.gb_worksapce, 0, 0, 1, 1)


        self.retranslateUi(W_CRAWLER)

        QMetaObject.connectSlotsByName(W_CRAWLER)
    # setupUi

    def retranslateUi(self, W_CRAWLER):
        W_CRAWLER.setWindowTitle(QCoreApplication.translate("W_CRAWLER", u"Sample_Window", None))
        self.gb_worksapce.setTitle("")
        self.le_check_result.setText("")
        self.groupBox.setTitle("")
        self.lb_from.setText(QCoreApplication.translate("W_CRAWLER", u"FROM", None))
        self.lb_to.setText(QCoreApplication.translate("W_CRAWLER", u"TO", None))
        self.pb_crawling.setText(QCoreApplication.translate("W_CRAWLER", u"Start Crawling", None))
        self.pb_processing.setText(QCoreApplication.translate("W_CRAWLER", u"Start Processing", None))
        self.cb_rule1.setText(QCoreApplication.translate("W_CRAWLER", u"RULE1", None))
        self.cb_rule2.setText(QCoreApplication.translate("W_CRAWLER", u"RULE2", None))
        self.cb_rule3.setText(QCoreApplication.translate("W_CRAWLER", u"RULE3", None))
    # retranslateUi

