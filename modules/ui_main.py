# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowDjvlZS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1060, 651)
        MainWindow.setMinimumSize(QSize(1060, 600))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color: rgba(40, 44, 52, 150);")
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sidemenu = QFrame(MainWindow)
        self.sidemenu.setObjectName(u"sidemenu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidemenu.sizePolicy().hasHeightForWidth())
        self.sidemenu.setSizePolicy(sizePolicy)
        self.sidemenu.setMinimumSize(QSize(50, 0))
        self.sidemenu.setMaximumSize(QSize(50, 16777215))
        self.sidemenu.setStyleSheet(u"background-color: rgba(30, 35, 40, 150);")
        self.sidemenu.setFrameShape(QFrame.StyledPanel)
        self.sidemenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.sidemenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bg = QFrame(self.sidemenu)
        self.bg.setObjectName(u"bg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bg.sizePolicy().hasHeightForWidth())
        self.bg.setSizePolicy(sizePolicy1)
        self.bg.setMinimumSize(QSize(51, 41))
        self.bg.setMaximumSize(QSize(240, 41))
        self.bg.setFrameShape(QFrame.StyledPanel)
        self.bg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.bg)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.icon = QPushButton(self.bg)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(40, 40))
        self.icon.setMaximumSize(QSize(240, 40))
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI")
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.icon.setFont(font1)
        self.icon.setStyleSheet(u"QPushButton{\n"
                                "	text-align: left;\n"
                                "	padding-left: 10px;\n"
                                "	color: rgb(255, 255, 255);\n"
                                "	background-color: rgba(0, 0, 0, 0);\n"
                                "}\n"
                                "QPushButton::hover {\n"
                                "	background-color: rgba(90, 90, 90, 128);\n"
                                "}\n"
                                "QPushButton::pressed {\n"
                                "	background-color: rgba(90, 90, 90, 50);\n"
                                "}")
        icon1 = QIcon()
        icon1.addFile(u"resources/ning-white-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon.setIcon(icon1)
        self.icon.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.icon)

        self.verticalLayout.addWidget(self.bg)

        self.home_tab = QPushButton(self.sidemenu)
        self.home_tab.setObjectName(u"home_tab")
        self.home_tab.setMinimumSize(QSize(40, 40))
        self.home_tab.setMaximumSize(QSize(16777215, 50))
        self.home_tab.setFont(font1)
        self.home_tab.setStyleSheet(u"QPushButton{\n"
                                    "	text-align: left;\n"
                                    "	padding-left: 15px;\n"
                                    "	color: rgb(255, 255, 255);\n"
                                    "	background-color: rgba(0, 0, 0, 0);\n"
                                    "    border:1px solid transparent;\n"
                                    "}\n"
                                    "QPushButton::hover {\n"
                                    "	background-color: rgba(90, 90, 90, 128);\n"
                                    " 	border: 1px solid rgb(101, 110, 126);\n"
                                    "}\n"
                                    "QPushButton::pressed {\n"
                                    "	background-color: rgba(90, 90, 90, 50);\n"
                                    "}")
        icon2 = QIcon()
        icon2.addFile(u"resources/ic_home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_tab.setIcon(icon2)
        self.home_tab.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.home_tab)

        self.VS = QSpacerItem(20, 476, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.VS)

        self.settings = QPushButton(self.sidemenu)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(49, 49))
        self.settings.setMaximumSize(QSize(16777215, 50))
        self.settings.setSizeIncrement(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Microsoft YaHei UI")
        font2.setPointSize(12)
        self.settings.setFont(font2)
        self.settings.setStyleSheet(u"QPushButton{\n"
                                    "	text-align: left;\n"
                                    "	padding-left: 16px;\n"
                                    "	color: rgb(255, 255, 255);\n"
                                    "	background-color: rgba(0, 0, 0, 0);\n"
                                    "    border:1px solid transparent;\n"
                                    "}\n"
                                    "QPushButton::hover {\n"
                                    "	background-color: rgba(90, 90, 90, 128);\n"
                                    " 	border: 1px solid rgb(101, 110, 126);\n"
                                    "}\n"
                                    "QPushButton::pressed {\n"
                                    "	background-color: rgba(90, 90, 90, 50);\n"
                                    "}")
        icon3 = QIcon()
        icon3.addFile(u"resources/ic_cog.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon3)

        self.verticalLayout.addWidget(self.settings)

        self.gridLayout.addWidget(self.sidemenu, 0, 0, 3, 1)

        self.contentTopBg = QFrame(MainWindow)
        self.contentTopBg.setObjectName(u"contentTopBg")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.contentTopBg.sizePolicy().hasHeightForWidth())
        self.contentTopBg.setSizePolicy(sizePolicy2)
        self.contentTopBg.setStyleSheet(u"background-color: rgba(30, 35, 40, 150);")
        self.contentTopBg.setFrameShape(QFrame.StyledPanel)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.contentTopBg.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.contentTopBg)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 40))
        self.title.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setFamily(u"Microsoft YaHei UI")
        font3.setPointSize(11)
        self.title.setFont(font3)
        self.title.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "padding-left: 5px;")

        self.horizontalLayout.addWidget(self.title)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 40))
        self.rightButtons.setMaximumSize(QSize(100, 40))
        self.rightButtons.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.rightButtons.setFrameShape(QFrame.StyledPanel)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MinimizeBtn = QPushButton(self.rightButtons)
        self.MinimizeBtn.setObjectName(u"MinimizeBtn")
        self.MinimizeBtn.setMinimumSize(QSize(28, 28))
        self.MinimizeBtn.setMaximumSize(QSize(28, 28))
        self.MinimizeBtn.setStyleSheet(u"/* Top Buttons */\n"
                                       "QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
                                       "QPushButton:hover { background-color: rgb(84, 89, 97); border-style: solid; border-radius: 4px; }\n"
                                       "QPushButton:pressed { background-color: rgb(53, 56, 60); border-style: solid; border-radius: 4px; }")
        icon4 = QIcon()
        icon4.addFile(u"resources/ic_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MinimizeBtn.setIcon(icon4)
        self.MinimizeBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.MinimizeBtn)

        self.MaximizeBtn = QPushButton(self.rightButtons)
        self.MaximizeBtn.setObjectName(u"MaximizeBtn")
        self.MaximizeBtn.setMinimumSize(QSize(28, 28))
        self.MaximizeBtn.setMaximumSize(QSize(28, 28))
        self.MaximizeBtn.setStyleSheet(u"/* Top Buttons */\n"
                                       "QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
                                       "QPushButton:hover { background-color: rgb(84, 89, 97); border-style: solid; border-radius: 4px; }\n"
                                       "QPushButton:pressed { background-color: rgb(53, 56, 60); border-style: solid; border-radius: 4px; }")
        icon5 = QIcon()
        icon5.addFile(u"resources/ic_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MaximizeBtn.setIcon(icon5)
        self.MaximizeBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.MaximizeBtn)

        self.CloseBtn = QPushButton(self.rightButtons)
        self.CloseBtn.setObjectName(u"CloseBtn")
        self.CloseBtn.setMinimumSize(QSize(28, 28))
        self.CloseBtn.setMaximumSize(QSize(28, 28))
        self.CloseBtn.setStyleSheet(u"/* Top Buttons */\n"
                                    "QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
                                    "QPushButton:hover { background-color: rgb(157, 47, 47); border-style: solid; border-radius: 4px; }\n"
                                    "QPushButton:pressed { background-color: rgb(117, 57, 57); border-style: solid; border-radius: 4px; }")
        icon6 = QIcon()
        icon6.addFile(u"resources/ic_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseBtn.setIcon(icon6)
        self.CloseBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.CloseBtn)

        self.horizontalLayout.addWidget(self.rightButtons)

        self.gridLayout.addWidget(self.contentTopBg, 0, 1, 1, 1)

        self.frame = QFrame(MainWindow)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.VST = QSpacerItem(20, 175, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.VST)

        self.Center_icon = QHBoxLayout()
        self.Center_icon.setObjectName(u"Center_icon")
        self.Title_icon = QLabel(self.frame)
        self.Title_icon.setObjectName(u"Title_icon")
        self.Title_icon.setEnabled(True)
        self.Title_icon.setMinimumSize(QSize(180, 180))
        self.Title_icon.setMaximumSize(QSize(180, 180))
        self.Title_icon.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.Title_icon.setPixmap(QPixmap(u"resources/ning-white-2.png"))
        self.Title_icon.setScaledContents(True)

        self.Center_icon.addWidget(self.Title_icon)

        self.verticalLayout_2.addLayout(self.Center_icon)

        self.Title01 = QLabel(self.frame)
        self.Title01.setObjectName(u"Title01")
        self.Title01.setMinimumSize(QSize(0, 70))
        self.Title01.setMaximumSize(QSize(16777215, 70))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(22)
        self.Title01.setFont(font4)
        self.Title01.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                   "background-color: rgba(0, 0, 0, 0);")
        self.Title01.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Title01)

        self.VSB = QSpacerItem(20, 131, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.VSB)

        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.BottomButtons = QFrame(MainWindow)
        self.BottomButtons.setObjectName(u"BottomButtons")
        sizePolicy2.setHeightForWidth(self.BottomButtons.sizePolicy().hasHeightForWidth())
        self.BottomButtons.setSizePolicy(sizePolicy2)
        self.BottomButtons.setMinimumSize(QSize(0, 50))
        self.BottomButtons.setMaximumSize(QSize(16777215, 50))
        self.BottomButtons.setStyleSheet(u"background-color: rgba(30, 35, 40, 150);")
        self.BottomButtons.setFrameShape(QFrame.StyledPanel)
        self.BottomButtons.setFrameShadow(QFrame.Raised)
        self.BottomButtons.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.BottomButtons)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Status = QLabel(self.BottomButtons)
        self.Status.setObjectName(u"Status")
        self.Status.setMinimumSize(QSize(0, 49))
        self.Status.setMaximumSize(QSize(16777215, 49))
        self.Status.setBaseSize(QSize(0, 0))
        self.Status.setFont(font2)
        self.Status.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "padding-left: 5px;")

        self.horizontalLayout_2.addWidget(self.Status)

        self.SettingsButton = QPushButton(self.BottomButtons)
        self.SettingsButton.setObjectName(u"SettingsButton")
        self.SettingsButton.setMinimumSize(QSize(49, 49))
        self.SettingsButton.setMaximumSize(QSize(49, 49))
        font5 = QFont()
        font5.setFamily(u"AmdtSymbols")
        self.SettingsButton.setFont(font5)
        self.SettingsButton.setStyleSheet(u"QPushButton{\n"
                                          "	background-color: rgba(0, 0, 0, 0);\n"
                                          "    border:0px;\n"
                                          "}\n"
                                          "QPushButton::hover {\n"
                                          "	background-color: rgba(90, 90, 90, 128);\n"
                                          " 	border: 2px solid rgb(101, 110, 126);\n"
                                          "}\n"
                                          "QPushButton::pressed {\n"
                                          "	background-color: rgba(90, 90, 90, 50);\n"
                                          " 	border: 2px solid rgb(101, 110, 126);\n"
                                          "}")
        icon7 = QIcon()
        icon7.addFile(u"resources/ic_cube.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SettingsButton.setIcon(icon7)
        self.SettingsButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.SettingsButton)

        self.LaunchButton = QPushButton(self.BottomButtons)
        self.LaunchButton.setObjectName(u"LaunchButton")
        self.LaunchButton.setMinimumSize(QSize(180, 49))
        self.LaunchButton.setMaximumSize(QSize(180, 49))
        font6 = QFont()
        font6.setFamily(u"Microsoft YaHei UI")
        font6.setPointSize(18)
        self.LaunchButton.setFont(font6)
        self.LaunchButton.setStyleSheet(u"QPushButton{\n"
                                        "	color: rgb(255, 255, 255);\n"
                                        "	background-color: rgb(0, 110, 180);\n"
                                        " 	border: none;\n"
                                        "    border:0px;\n"
                                        "}\n"
                                        "QPushButton::hover {\n"
                                        "	background-color: rgb(0, 99, 169);\n"
                                        " 	border: 2px solid rgb(101, 110, 126);\n"
                                        "}\n"
                                        "QPushButton::pressed {\n"
                                        "	background-color: rgba(0, 79, 149, 170);\n"
                                        " 	border: 2px solid rgb(101, 110, 126);\n"
                                        "}")

        self.horizontalLayout_2.addWidget(self.LaunchButton)

        self.gridLayout.addWidget(self.BottomButtons, 2, 1, 1, 1)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ning Launcher", None))
        # if QT_CONFIG(tooltip)
        self.icon.setToolTip(QCoreApplication.translate("MainWindow", u"Expand Menu", None))
        # endif // QT_CONFIG(tooltip)
        self.icon.setText(QCoreApplication.translate("MainWindow", u"  Menu", None))
        # if QT_CONFIG(tooltip)
        self.home_tab.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
        # endif // QT_CONFIG(tooltip)
        self.home_tab.setText(QCoreApplication.translate("MainWindow", u"   Home", None))
        # if QT_CONFIG(tooltip)
        self.settings.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
        # endif // QT_CONFIG(tooltip)
        self.settings.setText(QCoreApplication.translate("MainWindow", u"   Settings", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Ning Launcher", None))
        # if QT_CONFIG(tooltip)
        self.MinimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        # endif // QT_CONFIG(tooltip)
        self.MinimizeBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.MaximizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        # endif // QT_CONFIG(tooltip)
        self.MaximizeBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.CloseBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        # endif // QT_CONFIG(tooltip)
        self.CloseBtn.setText("")
        self.Title_icon.setText("")
        self.Title01.setText(QCoreApplication.translate("MainWindow", u"Welcome To Ning Launcher!", None))
        self.Status.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        # if QT_CONFIG(tooltip)
        self.SettingsButton.setToolTip(QCoreApplication.translate("MainWindow", u"Choose Version", None))
        # endif // QT_CONFIG(tooltip)
        self.SettingsButton.setText("")
        # if QT_CONFIG(tooltip)
        self.LaunchButton.setToolTip(QCoreApplication.translate("MainWindow", u"Launch Game", None))
        # endif // QT_CONFIG(tooltip)
        self.LaunchButton.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
    # retranslateUi

