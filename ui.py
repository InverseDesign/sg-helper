# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sg-util.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(220, 455)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(220, 455))
        MainWindow.setMaximumSize(QSize(248, 455))
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u"QQSG_101.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.groupWindow = QWidget(self.centralwidget)
        self.groupWindow.setObjectName(u"groupWindow")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupWindow.sizePolicy().hasHeightForWidth())
        self.groupWindow.setSizePolicy(sizePolicy2)
        self.formWindow = QFormLayout(self.groupWindow)
        self.formWindow.setObjectName(u"formWindow")
        self.formWindow.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        self.formWindow.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.groupWindow)
        self.label.setObjectName(u"label")

        self.formWindow.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.windowSelecterContainer = QWidget(self.groupWindow)
        self.windowSelecterContainer.setObjectName(u"windowSelecterContainer")
        self.windowSelecterContainer.setMinimumSize(QSize(0, 24))
        self.windowSelecterContainer.setMaximumSize(QSize(16777215, 24))
        self.hBoxWindowSelecter = QHBoxLayout(self.windowSelecterContainer)
        self.hBoxWindowSelecter.setObjectName(u"hBoxWindowSelecter")
        self.hBoxWindowSelecter.setContentsMargins(0, 0, 0, 0)
        self.WindowSelecter = QComboBox(self.windowSelecterContainer)
        self.WindowSelecter.setObjectName(u"WindowSelecter")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.WindowSelecter.sizePolicy().hasHeightForWidth())
        self.WindowSelecter.setSizePolicy(sizePolicy3)
        self.WindowSelecter.setMinimumSize(QSize(0, 24))
        self.WindowSelecter.setMaximumSize(QSize(16777215, 24))

        self.hBoxWindowSelecter.addWidget(self.WindowSelecter)

        self.RefreshWindowBtn = QPushButton(self.windowSelecterContainer)
        self.RefreshWindowBtn.setObjectName(u"RefreshWindowBtn")
        sizePolicy.setHeightForWidth(self.RefreshWindowBtn.sizePolicy().hasHeightForWidth())
        self.RefreshWindowBtn.setSizePolicy(sizePolicy)
        self.RefreshWindowBtn.setMinimumSize(QSize(24, 24))
        self.RefreshWindowBtn.setMaximumSize(QSize(24, 24))
        self.RefreshWindowBtn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.RefreshWindowBtn.setIcon(icon1)
        self.RefreshWindowBtn.setIconSize(QSize(10, 10))
        self.RefreshWindowBtn.setCheckable(False)
        self.RefreshWindowBtn.setAutoRepeat(False)
        self.RefreshWindowBtn.setAutoExclusive(False)
        self.RefreshWindowBtn.setFlat(False)

        self.hBoxWindowSelecter.addWidget(self.RefreshWindowBtn)


        self.formWindow.setWidget(0, QFormLayout.ItemRole.FieldRole, self.windowSelecterContainer)


        self.mainLayout.addWidget(self.groupWindow)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setDocumentMode(False)
        self.tab_start = QWidget()
        self.tab_start.setObjectName(u"tab_start")
        self.verticalLayoutTabStart = QVBoxLayout(self.tab_start)
        self.verticalLayoutTabStart.setSpacing(4)
        self.verticalLayoutTabStart.setObjectName(u"verticalLayoutTabStart")
        self.verticalLayoutTabStart.setContentsMargins(4, 4, 4, 4)
        self.groupGamePath = QGroupBox(self.tab_start)
        self.groupGamePath.setObjectName(u"groupGamePath")
        sizePolicy2.setHeightForWidth(self.groupGamePath.sizePolicy().hasHeightForWidth())
        self.groupGamePath.setSizePolicy(sizePolicy2)
        self.groupGamePath.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #a0a0a0;\n"
"    margin-top: 1ex;\n"
"    margin-bottom: 1px;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    padding-top: 6px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 12px;\n"
"    padding: 0 4px;\n"
"    color: #1e466e;\n"
"    font: 8pt \"Segoe UI\";\n"
"}")
        self.layoutGamePath = QVBoxLayout(self.groupGamePath)
        self.layoutGamePath.setSpacing(4)
        self.layoutGamePath.setObjectName(u"layoutGamePath")
        self.layoutPathDisplay = QHBoxLayout()
        self.layoutPathDisplay.setObjectName(u"layoutPathDisplay")
        self.GamePathEdit = QLineEdit(self.groupGamePath)
        self.GamePathEdit.setObjectName(u"GamePathEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.GamePathEdit.sizePolicy().hasHeightForWidth())
        self.GamePathEdit.setSizePolicy(sizePolicy4)
        self.GamePathEdit.setReadOnly(True)

        self.layoutPathDisplay.addWidget(self.GamePathEdit)

        self.BtnBrowsePath = QPushButton(self.groupGamePath)
        self.BtnBrowsePath.setObjectName(u"BtnBrowsePath")
        sizePolicy.setHeightForWidth(self.BtnBrowsePath.sizePolicy().hasHeightForWidth())
        self.BtnBrowsePath.setSizePolicy(sizePolicy)
        self.BtnBrowsePath.setMinimumSize(QSize(40, 24))
        self.BtnBrowsePath.setMaximumSize(QSize(40, 24))

        self.layoutPathDisplay.addWidget(self.BtnBrowsePath)


        self.layoutGamePath.addLayout(self.layoutPathDisplay)

        self.BtnSearchGame = QPushButton(self.groupGamePath)
        self.BtnSearchGame.setObjectName(u"BtnSearchGame")
        self.BtnSearchGame.setMinimumSize(QSize(0, 24))

        self.layoutGamePath.addWidget(self.BtnSearchGame)


        self.verticalLayoutTabStart.addWidget(self.groupGamePath)

        self.BtnLaunchGame = QPushButton(self.tab_start)
        self.BtnLaunchGame.setObjectName(u"BtnLaunchGame")
        self.BtnLaunchGame.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.BtnLaunchGame.sizePolicy().hasHeightForWidth())
        self.BtnLaunchGame.setSizePolicy(sizePolicy2)
        self.BtnLaunchGame.setMinimumSize(QSize(0, 32))
        self.BtnLaunchGame.setStyleSheet(u"QPushButton { background: #2e7d32; color: white; border: none; border-radius: 4px; font: bold 9pt; }\n"
"QPushButton:hover { background: #388e3c; }\n"
"QPushButton:pressed { background: #1b5e20; }\n"
"QPushButton:disabled { background: #a0a0a0; color: #e0e0e0; }")

        self.verticalLayoutTabStart.addWidget(self.BtnLaunchGame)

        self.spacerStart = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayoutTabStart.addItem(self.spacerStart)

        self.tabWidget.addTab(self.tab_start, "")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tab_1.setEnabled(True)
        self.verticalLayoutTab1 = QVBoxLayout(self.tab_1)
        self.verticalLayoutTab1.setSpacing(4)
        self.verticalLayoutTab1.setObjectName(u"verticalLayoutTab1")
        self.verticalLayoutTab1.setContentsMargins(4, 4, 4, 4)
        self.groupBlood = QGroupBox(self.tab_1)
        self.groupBlood.setObjectName(u"groupBlood")
        sizePolicy2.setHeightForWidth(self.groupBlood.sizePolicy().hasHeightForWidth())
        self.groupBlood.setSizePolicy(sizePolicy2)
        self.groupBlood.setAutoFillBackground(False)
        self.groupBlood.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #a0a0a0;\n"
"    margin-top: 1ex;\n"
"    margin-bottom: 1px;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    padding-top: 6px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 12px;\n"
"    padding: 0 4px;\n"
"    color: #1e466e;\n"
"    font: 8pt \"Segoe UI\";\n"
"}")
        self.groupBlood.setFlat(False)
        self.formBlood = QFormLayout(self.groupBlood)
        self.formBlood.setObjectName(u"formBlood")
        self.formBlood.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formBlood.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        self.label_role = QLabel(self.groupBlood)
        self.label_role.setObjectName(u"label_role")

        self.formBlood.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_role)

        self.CurrentRolePicture = QGraphicsView(self.groupBlood)
        self.CurrentRolePicture.setObjectName(u"CurrentRolePicture")
        self.CurrentRolePicture.setMinimumSize(QSize(0, 20))
        self.CurrentRolePicture.setMaximumSize(QSize(16777215, 20))
        self.CurrentRolePicture.setInteractive(False)

        self.formBlood.setWidget(0, QFormLayout.ItemRole.FieldRole, self.CurrentRolePicture)

        self.label_blood_pic = QLabel(self.groupBlood)
        self.label_blood_pic.setObjectName(u"label_blood_pic")

        self.formBlood.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_blood_pic)

        self.CurrentBloodPicture = QGraphicsView(self.groupBlood)
        self.CurrentBloodPicture.setObjectName(u"CurrentBloodPicture")
        self.CurrentBloodPicture.setMinimumSize(QSize(0, 20))
        self.CurrentBloodPicture.setMaximumSize(QSize(16777215, 20))
        self.CurrentBloodPicture.setInteractive(False)

        self.formBlood.setWidget(1, QFormLayout.ItemRole.FieldRole, self.CurrentBloodPicture)

        self.label_magic_pic = QLabel(self.groupBlood)
        self.label_magic_pic.setObjectName(u"label_magic_pic")

        self.formBlood.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_magic_pic)

        self.CurrentMagicPicture = QGraphicsView(self.groupBlood)
        self.CurrentMagicPicture.setObjectName(u"CurrentMagicPicture")
        self.CurrentMagicPicture.setMinimumSize(QSize(0, 20))
        self.CurrentMagicPicture.setMaximumSize(QSize(16777215, 20))
        self.CurrentMagicPicture.setInteractive(False)

        self.formBlood.setWidget(2, QFormLayout.ItemRole.FieldRole, self.CurrentMagicPicture)

        self.label_5 = QLabel(self.groupBlood)
        self.label_5.setObjectName(u"label_5")

        self.formBlood.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.widget1 = QWidget(self.groupBlood)
        self.widget1.setObjectName(u"widget1")
        sizePolicy2.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.EnableBloodHelper = QCheckBox(self.widget1)
        self.EnableBloodHelper.setObjectName(u"EnableBloodHelper")
        sizePolicy.setHeightForWidth(self.EnableBloodHelper.sizePolicy().hasHeightForWidth())
        self.EnableBloodHelper.setSizePolicy(sizePolicy)
        self.EnableBloodHelper.setChecked(False)

        self.horizontalLayout.addWidget(self.EnableBloodHelper)

        self.MinBloodKeySelecter = QComboBox(self.widget1)
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.addItem("")
        self.MinBloodKeySelecter.setObjectName(u"MinBloodKeySelecter")
        self.MinBloodKeySelecter.setMinimumSize(QSize(0, 24))

        self.horizontalLayout.addWidget(self.MinBloodKeySelecter)


        self.formBlood.setWidget(3, QFormLayout.ItemRole.FieldRole, self.widget1)

        self.widget2 = QWidget(self.groupBlood)
        self.widget2.setObjectName(u"widget2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.EnableMagicHelper = QCheckBox(self.widget2)
        self.EnableMagicHelper.setObjectName(u"EnableMagicHelper")
        sizePolicy.setHeightForWidth(self.EnableMagicHelper.sizePolicy().hasHeightForWidth())
        self.EnableMagicHelper.setSizePolicy(sizePolicy)
        self.EnableMagicHelper.setChecked(False)

        self.horizontalLayout_2.addWidget(self.EnableMagicHelper)

        self.MinMagicKeySelecter = QComboBox(self.widget2)
        self.MinMagicKeySelecter.addItem("")
        self.MinMagicKeySelecter.addItem("")
        self.MinMagicKeySelecter.addItem("")
        self.MinMagicKeySelecter.setObjectName(u"MinMagicKeySelecter")
        self.MinMagicKeySelecter.setMinimumSize(QSize(0, 24))

        self.horizontalLayout_2.addWidget(self.MinMagicKeySelecter)


        self.formBlood.setWidget(4, QFormLayout.ItemRole.FieldRole, self.widget2)

        self.label_7 = QLabel(self.groupBlood)
        self.label_7.setObjectName(u"label_7")

        self.formBlood.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.MinBloodPrecentageSelecter = QComboBox(self.groupBlood)
        self.MinBloodPrecentageSelecter.addItem("")
        self.MinBloodPrecentageSelecter.addItem("")
        self.MinBloodPrecentageSelecter.addItem("")
        self.MinBloodPrecentageSelecter.addItem("")
        self.MinBloodPrecentageSelecter.setObjectName(u"MinBloodPrecentageSelecter")
        sizePolicy2.setHeightForWidth(self.MinBloodPrecentageSelecter.sizePolicy().hasHeightForWidth())
        self.MinBloodPrecentageSelecter.setSizePolicy(sizePolicy2)
        self.MinBloodPrecentageSelecter.setMinimumSize(QSize(0, 24))

        self.formBlood.setWidget(5, QFormLayout.ItemRole.FieldRole, self.MinBloodPrecentageSelecter)

        self.label_6 = QLabel(self.groupBlood)
        self.label_6.setObjectName(u"label_6")

        self.formBlood.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)


        self.verticalLayoutTab1.addWidget(self.groupBlood)

        self.groupStuck = QGroupBox(self.tab_1)
        self.groupStuck.setObjectName(u"groupStuck")
        sizePolicy2.setHeightForWidth(self.groupStuck.sizePolicy().hasHeightForWidth())
        self.groupStuck.setSizePolicy(sizePolicy2)
        self.groupStuck.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #a0a0a0;\n"
"    margin-top: 1ex;\n"
"    margin-bottom: 1px;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    padding-top: 6px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 12px;\n"
"    padding: 0 4px;\n"
"    color: #1e466e;\n"
"    font: 8pt \"Segoe UI\";\n"
"}")
        self.groupStuck.setFlat(False)
        self.groupStuck.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupStuck)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelStuckEnable = QLabel(self.groupStuck)
        self.labelStuckEnable.setObjectName(u"labelStuckEnable")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.labelStuckEnable.sizePolicy().hasHeightForWidth())
        self.labelStuckEnable.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.labelStuckEnable)

        self.StuckKeyStatus = QCheckBox(self.groupStuck)
        self.StuckKeyStatus.setObjectName(u"StuckKeyStatus")

        self.horizontalLayout_3.addWidget(self.StuckKeyStatus)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelTick1 = QLabel(self.groupStuck)
        self.labelTick1.setObjectName(u"labelTick1")

        self.gridLayout.addWidget(self.labelTick1, 0, 0, 1, 1)

        self.Tick1 = QComboBox(self.groupStuck)
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.addItem("")
        self.Tick1.setObjectName(u"Tick1")

        self.gridLayout.addWidget(self.Tick1, 0, 1, 1, 1)

        self.labelTick2 = QLabel(self.groupStuck)
        self.labelTick2.setObjectName(u"labelTick2")

        self.gridLayout.addWidget(self.labelTick2, 0, 2, 1, 1)

        self.Tick2 = QComboBox(self.groupStuck)
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.addItem("")
        self.Tick2.setObjectName(u"Tick2")

        self.gridLayout.addWidget(self.Tick2, 0, 3, 1, 1)

        self.labelTick3 = QLabel(self.groupStuck)
        self.labelTick3.setObjectName(u"labelTick3")

        self.gridLayout.addWidget(self.labelTick3, 1, 0, 1, 1)

        self.Tick3 = QComboBox(self.groupStuck)
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.addItem("")
        self.Tick3.setObjectName(u"Tick3")

        self.gridLayout.addWidget(self.Tick3, 1, 1, 1, 1)

        self.labelTick4 = QLabel(self.groupStuck)
        self.labelTick4.setObjectName(u"labelTick4")

        self.gridLayout.addWidget(self.labelTick4, 1, 2, 1, 1)

        self.Tick4 = QComboBox(self.groupStuck)
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.addItem("")
        self.Tick4.setObjectName(u"Tick4")

        self.gridLayout.addWidget(self.Tick4, 1, 3, 1, 1)

        self.labelTick5 = QLabel(self.groupStuck)
        self.labelTick5.setObjectName(u"labelTick5")

        self.gridLayout.addWidget(self.labelTick5, 2, 0, 1, 1)

        self.Tick5 = QComboBox(self.groupStuck)
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.addItem("")
        self.Tick5.setObjectName(u"Tick5")

        self.gridLayout.addWidget(self.Tick5, 2, 1, 1, 1)

        self.labelTick6 = QLabel(self.groupStuck)
        self.labelTick6.setObjectName(u"labelTick6")

        self.gridLayout.addWidget(self.labelTick6, 2, 2, 1, 1)

        self.Tick6 = QComboBox(self.groupStuck)
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.addItem("")
        self.Tick6.setObjectName(u"Tick6")

        self.gridLayout.addWidget(self.Tick6, 2, 3, 1, 1)

        self.labelTick7 = QLabel(self.groupStuck)
        self.labelTick7.setObjectName(u"labelTick7")

        self.gridLayout.addWidget(self.labelTick7, 3, 0, 1, 1)

        self.Tick7 = QComboBox(self.groupStuck)
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.addItem("")
        self.Tick7.setObjectName(u"Tick7")

        self.gridLayout.addWidget(self.Tick7, 3, 1, 1, 1)

        self.labelTick8 = QLabel(self.groupStuck)
        self.labelTick8.setObjectName(u"labelTick8")

        self.gridLayout.addWidget(self.labelTick8, 3, 2, 1, 1)

        self.Tick8 = QComboBox(self.groupStuck)
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.addItem("")
        self.Tick8.setObjectName(u"Tick8")

        self.gridLayout.addWidget(self.Tick8, 3, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayoutTab1.addWidget(self.groupStuck)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, -1, 9, -1)
        self.groupBox = QGroupBox(self.tab_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #a0a0a0;\n"
"    margin-top: 1ex;\n"
"    margin-bottom: 1px;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    padding-top: 6px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 12px;\n"
"    padding: 0 4px;\n"
"    color: #1e466e;\n"
"    font: 8pt \"Segoe UI\";\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 24))

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 24))

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid #a0a0a0;\n"
"    margin-top: 1ex;\n"
"    margin-bottom: 1px;\n"
"    margin-left: 2px;\n"
"    margin-right: 2px;\n"
"    padding-top: 6px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 12px;\n"
"    padding: 0 4px;\n"
"    color: #1e466e;\n"
"    font: 8pt \"Segoe UI\";\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pushButton_3 = QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_3.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.tab_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_3.addWidget(self.pushButton_6, 5, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_3.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_3.addWidget(self.pushButton_5, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.mainLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e09\u56fd\u6309\u952e\u52a9\u624b v1.0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7a97\u53e3:", None))
#if QT_CONFIG(tooltip)
        self.RefreshWindowBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u7a97\u53e3\u5217\u8868", None))
#endif // QT_CONFIG(tooltip)
        self.RefreshWindowBtn.setText("")
        self.groupGamePath.setTitle(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u8def\u5f84", None))
        self.GamePathEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u672a\u8bbe\u7f6e\u6e38\u620f\u8def\u5f84", None))
        self.BtnBrowsePath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.BtnSearchGame.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u641c\u7d22\u6e38\u620f", None))
        self.BtnLaunchGame.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u6e38\u620f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_start), QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.groupBlood.setTitle(QCoreApplication.translate("MainWindow", u"\u89d2\u8272\u4fe1\u606f", None))
        self.label_role.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u8272", None))
        self.label_blood_pic.setText(QCoreApplication.translate("MainWindow", u"\u751f\u547d\u6761", None))
        self.label_magic_pic.setText(QCoreApplication.translate("MainWindow", u"\u4f53\u529b\u6761", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u56de\u590d\u751f\u547d", None))
        self.EnableBloodHelper.setText("")
        self.MinBloodKeySelecter.setItemText(0, QCoreApplication.translate("MainWindow", u"R", None))
        self.MinBloodKeySelecter.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))
        self.MinBloodKeySelecter.setItemText(2, QCoreApplication.translate("MainWindow", u"A", None))
        self.MinBloodKeySelecter.setItemText(3, QCoreApplication.translate("MainWindow", u"B", None))
        self.MinBloodKeySelecter.setItemText(4, QCoreApplication.translate("MainWindow", u"C", None))
        self.MinBloodKeySelecter.setItemText(5, QCoreApplication.translate("MainWindow", u"D", None))
        self.MinBloodKeySelecter.setItemText(6, QCoreApplication.translate("MainWindow", u"Q", None))
        self.MinBloodKeySelecter.setItemText(7, QCoreApplication.translate("MainWindow", u"W", None))
        self.MinBloodKeySelecter.setItemText(8, QCoreApplication.translate("MainWindow", u"T", None))

        self.EnableMagicHelper.setText("")
        self.MinMagicKeySelecter.setItemText(0, QCoreApplication.translate("MainWindow", u"T", None))
        self.MinMagicKeySelecter.setItemText(1, QCoreApplication.translate("MainWindow", u"R", None))
        self.MinMagicKeySelecter.setItemText(2, QCoreApplication.translate("MainWindow", u"E", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u56de\u590d\u4f53\u529b", None))
        self.MinBloodPrecentageSelecter.setItemText(0, QCoreApplication.translate("MainWindow", u"40", None))
        self.MinBloodPrecentageSelecter.setItemText(1, QCoreApplication.translate("MainWindow", u"20", None))
        self.MinBloodPrecentageSelecter.setItemText(2, QCoreApplication.translate("MainWindow", u"60", None))
        self.MinBloodPrecentageSelecter.setItemText(3, QCoreApplication.translate("MainWindow", u"80", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u56de\u590d\u9608\u503c", None))
        self.groupStuck.setTitle(QCoreApplication.translate("MainWindow", u"\u5361\u952e (Ctrl + ` \u5207\u6362)", None))
        self.labelStuckEnable.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528:", None))
        self.StuckKeyStatus.setText("")
        self.labelTick1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Tick1.setItemText(0, "")
        self.Tick1.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.Tick1.setItemText(2, QCoreApplication.translate("MainWindow", u"S", None))
        self.Tick1.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.Tick1.setItemText(4, QCoreApplication.translate("MainWindow", u"F", None))
        self.Tick1.setItemText(5, QCoreApplication.translate("MainWindow", u"Q", None))
        self.Tick1.setItemText(6, QCoreApplication.translate("MainWindow", u"W", None))
        self.Tick1.setItemText(7, QCoreApplication.translate("MainWindow", u"E", None))
        self.Tick1.setItemText(8, QCoreApplication.translate("MainWindow", u"R", None))
        self.Tick1.setItemText(9, QCoreApplication.translate("MainWindow", u"T", None))
        self.Tick1.setItemText(10, QCoreApplication.translate("MainWindow", u"ALt+A", None))
        self.Tick1.setItemText(11, QCoreApplication.translate("MainWindow", u"ALt+S", None))
        self.Tick1.setItemText(12, QCoreApplication.translate("MainWindow", u"ALt+D", None))
        self.Tick1.setItemText(13, QCoreApplication.translate("MainWindow", u"ALt+F", None))
        self.Tick1.setItemText(14, QCoreApplication.translate("MainWindow", u"ALt+Q", None))
        self.Tick1.setItemText(15, QCoreApplication.translate("MainWindow", u"ALt+W", None))
        self.Tick1.setItemText(16, QCoreApplication.translate("MainWindow", u"ALt+E", None))
        self.Tick1.setItemText(17, QCoreApplication.translate("MainWindow", u"ALt+R", None))
        self.Tick1.setItemText(18, QCoreApplication.translate("MainWindow", u"ALt+T", None))

        self.labelTick2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Tick2.setItemText(0, "")
        self.Tick2.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.Tick2.setItemText(2, QCoreApplication.translate("MainWindow", u"S", None))
        self.Tick2.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.Tick2.setItemText(4, QCoreApplication.translate("MainWindow", u"F", None))
        self.Tick2.setItemText(5, QCoreApplication.translate("MainWindow", u"Q", None))
        self.Tick2.setItemText(6, QCoreApplication.translate("MainWindow", u"W", None))
        self.Tick2.setItemText(7, QCoreApplication.translate("MainWindow", u"E", None))
        self.Tick2.setItemText(8, QCoreApplication.translate("MainWindow", u"R", None))
        self.Tick2.setItemText(9, QCoreApplication.translate("MainWindow", u"T", None))
        self.Tick2.setItemText(10, QCoreApplication.translate("MainWindow", u"ALt+A", None))
        self.Tick2.setItemText(11, QCoreApplication.translate("MainWindow", u"ALt+S", None))
        self.Tick2.setItemText(12, QCoreApplication.translate("MainWindow", u"ALt+D", None))
        self.Tick2.setItemText(13, QCoreApplication.translate("MainWindow", u"ALt+F", None))
        self.Tick2.setItemText(14, QCoreApplication.translate("MainWindow", u"ALt+Q", None))
        self.Tick2.setItemText(15, QCoreApplication.translate("MainWindow", u"ALt+W", None))
        self.Tick2.setItemText(16, QCoreApplication.translate("MainWindow", u"ALt+E", None))
        self.Tick2.setItemText(17, QCoreApplication.translate("MainWindow", u"ALt+R", None))
        self.Tick2.setItemText(18, QCoreApplication.translate("MainWindow", u"ALt+T", None))

        self.labelTick3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Tick3.setItemText(0, "")
        self.Tick3.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.Tick3.setItemText(2, QCoreApplication.translate("MainWindow", u"S", None))
        self.Tick3.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.Tick3.setItemText(4, QCoreApplication.translate("MainWindow", u"F", None))
        self.Tick3.setItemText(5, QCoreApplication.translate("MainWindow", u"Q", None))
        self.Tick3.setItemText(6, QCoreApplication.translate("MainWindow", u"W", None))
        self.Tick3.setItemText(7, QCoreApplication.translate("MainWindow", u"E", None))
        self.Tick3.setItemText(8, QCoreApplication.translate("MainWindow", u"R", None))
        self.Tick3.setItemText(9, QCoreApplication.translate("MainWindow", u"T", None))
        self.Tick3.setItemText(10, QCoreApplication.translate("MainWindow", u"ALt+A", None))
        self.Tick3.setItemText(11, QCoreApplication.translate("MainWindow", u"ALt+S", None))
        self.Tick3.setItemText(12, QCoreApplication.translate("MainWindow", u"ALt+D", None))
        self.Tick3.setItemText(13, QCoreApplication.translate("MainWindow", u"ALt+F", None))
        self.Tick3.setItemText(14, QCoreApplication.translate("MainWindow", u"ALt+Q", None))
        self.Tick3.setItemText(15, QCoreApplication.translate("MainWindow", u"ALt+W", None))
        self.Tick3.setItemText(16, QCoreApplication.translate("MainWindow", u"ALt+E", None))
        self.Tick3.setItemText(17, QCoreApplication.translate("MainWindow", u"ALt+R", None))
        self.Tick3.setItemText(18, QCoreApplication.translate("MainWindow", u"ALt+T", None))

        self.labelTick4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Tick4.setItemText(0, "")
        self.Tick4.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.Tick4.setItemText(2, QCoreApplication.translate("MainWindow", u"S", None))
        self.Tick4.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.Tick4.setItemText(4, QCoreApplication.translate("MainWindow", u"F", None))
        self.Tick4.setItemText(5, QCoreApplication.translate("MainWindow", u"Q", None))
        self.Tick4.setItemText(6, QCoreApplication.translate("MainWindow", u"W", None))
        self.Tick4.setItemText(7, QCoreApplication.translate("MainWindow", u"E", None))
        self.Tick4.setItemText(8, QCoreApplication.translate("MainWindow", u"R", None))
        self.Tick4.setItemText(9, QCoreApplication.translate("MainWindow", u"T", None))
        self.Tick4.setItemText(10, QCoreApplication.translate("MainWindow", u"ALt+A", None))
        self.Tick4.setItemText(11, QCoreApplication.translate("MainWindow", u"ALt+S", None))
        self.Tick4.setItemText(12, QCoreApplication.translate("MainWindow", u"ALt+D", None))
        self.Tick4.setItemText(13, QCoreApplication.translate("MainWindow", u"ALt+F", None))
        self.Tick4.setItemText(14, QCoreApplication.translate("MainWindow", u"ALt+Q", None))
        self.Tick4.setItemText(15, QCoreApplication.translate("MainWindow", u"ALt+W", None))
        self.Tick4.setItemText(16, QCoreApplication.translate("MainWindow", u"ALt+E", None))
        self.Tick4.setItemText(17, QCoreApplication.translate("MainWindow", u"ALt+R", None))
        self.Tick4.setItemText(18, QCoreApplication.translate("MainWindow", u"ALt+T", None))

        self.labelTick5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Tick5.setItemText(0, "")
        self.Tick5.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.Tick5.setItemText(2, QCoreApplication.translate("MainWindow", u"S", None))
        self.Tick5.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.Tick5.setItemText(4, QCoreApplication.translate("MainWindow", u"F", None))
        self.Tick5.setItemText(5, QCoreApplication.translate("MainWindow", u"Q", None))
        self.Tick5.setItemText(6, QCoreApplication.translate("MainWindow", u"W", None))
        self.Tick5.setItemText(7, QCoreApplication.translate("MainWindow", u"E", None))
        self.Tick5.setItemText(8, QCoreApplication.translate("MainWindow", u"R", None))
        self.Tick5.setItemText(9, QCoreApplication.translate("MainWindow", u"T", None))
        self.Tick5.setItemText(10, QCoreApplication.translate("MainWindow", u"ALt+A", None))
        self.Tick5.setItemText(11, QCoreApplication.translate("MainWindow", u"ALt+S", None))
        self.Tick5.setItemText(12, QCoreApplication.translate("MainWindow", u"ALt+D", None))
        self.Tick5.setItemText(13, QCoreApplication.translate("MainWindow", u"ALt+F", None))
        self.Tick5.setItemText(14, QCoreApplication.translate("MainWindow", u"ALt+Q", None))
        self.Tick5.setItemText(15, QCoreApplication.translate("MainWindow", u"ALt+W", None))
        self.Tick5.setItemText(16, QCoreApplication.translate("MainWindow", u"ALt+E", None))
        self.Tick5.setItemText(17, QCoreApplication.translate("MainWindow", u"ALt+R", None))
        self.Tick5.setItemText(18, QCoreApplication.translate("MainWindow", u"ALt+T", None))

        self.labelTick6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Tick6.setItemText(0, "")
        self.Tick6.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.Tick6.setItemText(2, QCoreApplication.translate("MainWindow", u"S", None))
        self.Tick6.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.Tick6.setItemText(4, QCoreApplication.translate("MainWindow", u"F", None))
        self.Tick6.setItemText(5, QCoreApplication.translate("MainWindow", u"Q", None))
        self.Tick6.setItemText(6, QCoreApplication.translate("MainWindow", u"W", None))
        self.Tick6.setItemText(7, QCoreApplication.translate("MainWindow", u"E", None))
        self.Tick6.setItemText(8, QCoreApplication.translate("MainWindow", u"R", None))
        self.Tick6.setItemText(9, QCoreApplication.translate("MainWindow", u"T", None))
        self.Tick6.setItemText(10, QCoreApplication.translate("MainWindow", u"ALt+A", None))
        self.Tick6.setItemText(11, QCoreApplication.translate("MainWindow", u"ALt+S", None))
        self.Tick6.setItemText(12, QCoreApplication.translate("MainWindow", u"ALt+D", None))
        self.Tick6.setItemText(13, QCoreApplication.translate("MainWindow", u"ALt+F", None))
        self.Tick6.setItemText(14, QCoreApplication.translate("MainWindow", u"ALt+Q", None))
        self.Tick6.setItemText(15, QCoreApplication.translate("MainWindow", u"ALt+W", None))
        self.Tick6.setItemText(16, QCoreApplication.translate("MainWindow", u"ALt+E", None))
        self.Tick6.setItemText(17, QCoreApplication.translate("MainWindow", u"ALt+R", None))
        self.Tick6.setItemText(18, QCoreApplication.translate("MainWindow", u"ALt+T", None))

        self.labelTick7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Tick7.setItemText(0, "")
        self.Tick7.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.Tick7.setItemText(2, QCoreApplication.translate("MainWindow", u"S", None))
        self.Tick7.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.Tick7.setItemText(4, QCoreApplication.translate("MainWindow", u"F", None))
        self.Tick7.setItemText(5, QCoreApplication.translate("MainWindow", u"Q", None))
        self.Tick7.setItemText(6, QCoreApplication.translate("MainWindow", u"W", None))
        self.Tick7.setItemText(7, QCoreApplication.translate("MainWindow", u"E", None))
        self.Tick7.setItemText(8, QCoreApplication.translate("MainWindow", u"R", None))
        self.Tick7.setItemText(9, QCoreApplication.translate("MainWindow", u"T", None))
        self.Tick7.setItemText(10, QCoreApplication.translate("MainWindow", u"ALt+A", None))
        self.Tick7.setItemText(11, QCoreApplication.translate("MainWindow", u"ALt+S", None))
        self.Tick7.setItemText(12, QCoreApplication.translate("MainWindow", u"ALt+D", None))
        self.Tick7.setItemText(13, QCoreApplication.translate("MainWindow", u"ALt+F", None))
        self.Tick7.setItemText(14, QCoreApplication.translate("MainWindow", u"ALt+Q", None))
        self.Tick7.setItemText(15, QCoreApplication.translate("MainWindow", u"ALt+W", None))
        self.Tick7.setItemText(16, QCoreApplication.translate("MainWindow", u"ALt+E", None))
        self.Tick7.setItemText(17, QCoreApplication.translate("MainWindow", u"ALt+R", None))
        self.Tick7.setItemText(18, QCoreApplication.translate("MainWindow", u"ALt+T", None))

        self.labelTick8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Tick8.setItemText(0, "")
        self.Tick8.setItemText(1, QCoreApplication.translate("MainWindow", u"A", None))
        self.Tick8.setItemText(2, QCoreApplication.translate("MainWindow", u"S", None))
        self.Tick8.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.Tick8.setItemText(4, QCoreApplication.translate("MainWindow", u"F", None))
        self.Tick8.setItemText(5, QCoreApplication.translate("MainWindow", u"Q", None))
        self.Tick8.setItemText(6, QCoreApplication.translate("MainWindow", u"W", None))
        self.Tick8.setItemText(7, QCoreApplication.translate("MainWindow", u"E", None))
        self.Tick8.setItemText(8, QCoreApplication.translate("MainWindow", u"R", None))
        self.Tick8.setItemText(9, QCoreApplication.translate("MainWindow", u"T", None))
        self.Tick8.setItemText(10, QCoreApplication.translate("MainWindow", u"ALt+A", None))
        self.Tick8.setItemText(11, QCoreApplication.translate("MainWindow", u"ALt+S", None))
        self.Tick8.setItemText(12, QCoreApplication.translate("MainWindow", u"ALt+D", None))
        self.Tick8.setItemText(13, QCoreApplication.translate("MainWindow", u"ALt+F", None))
        self.Tick8.setItemText(14, QCoreApplication.translate("MainWindow", u"ALt+Q", None))
        self.Tick8.setItemText(15, QCoreApplication.translate("MainWindow", u"ALt+W", None))
        self.Tick8.setItemText(16, QCoreApplication.translate("MainWindow", u"ALt+E", None))
        self.Tick8.setItemText(17, QCoreApplication.translate("MainWindow", u"ALt+R", None))
        self.Tick8.setItemText(18, QCoreApplication.translate("MainWindow", u"ALt+T", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"\u57fa\u672c\u529f\u80fd", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u7ebf\u8def", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5207\u6362", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6cb3\u4f2f\u6765\u88ad", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5165", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u66f4\u591a\u529f\u80fd", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5b98\u7235\u4efb\u52a1", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u8c0b\u58eb\u5927\u8d5b", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u753b\u5bb9\u9053", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u63a8\u4e3e\u5b5d\u5ec9", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u65e5\u5e38\u6d3b\u52a8", None))
    # retranslateUi

