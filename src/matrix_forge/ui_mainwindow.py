# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)
from .glyph_canvas import GlyphCanvas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(733, 518)
        MainWindow.setMinimumSize(QSize(707, 498))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_to_new_file = QAction(MainWindow)
        self.actionSave_to_new_file.setObjectName(u"actionSave_to_new_file")
        self.actionLeft = QAction(MainWindow)
        self.actionLeft.setObjectName(u"actionLeft")
        self.actionUp = QAction(MainWindow)
        self.actionUp.setObjectName(u"actionUp")
        self.actionDown = QAction(MainWindow)
        self.actionDown.setObjectName(u"actionDown")
        self.actionRight = QAction(MainWindow)
        self.actionRight.setObjectName(u"actionRight")
        self.actionInvert = QAction(MainWindow)
        self.actionInvert.setObjectName(u"actionInvert")
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        self.actionAdd = QAction(MainWindow)
        self.actionAdd.setObjectName(u"actionAdd")
        self.actionSelected = QAction(MainWindow)
        self.actionSelected.setObjectName(u"actionSelected")
        self.actionAll = QAction(MainWindow)
        self.actionAll.setObjectName(u"actionAll")
        self.actionTo_defaults = QAction(MainWindow)
        self.actionTo_defaults.setObjectName(u"actionTo_defaults")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.glyphSelector = QWidget(self.centralwidget)
        self.glyphSelector.setObjectName(u"glyphSelector")
        self.glyphSelector.setMaximumSize(QSize(240, 16777215))
        self.verticalLayout = QVBoxLayout(self.glyphSelector)
        self.verticalLayout.setSpacing(14)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 12, -1, -1)
        self.selectorList = QWidget(self.glyphSelector)
        self.selectorList.setObjectName(u"selectorList")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectorList.sizePolicy().hasHeightForWidth())
        self.selectorList.setSizePolicy(sizePolicy)
        self.selectorList.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.selectorList)
        self.verticalLayout_3.setSpacing(14)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.glyphSelectorTitle = QLabel(self.selectorList)
        self.glyphSelectorTitle.setObjectName(u"glyphSelectorTitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.glyphSelectorTitle.sizePolicy().hasHeightForWidth())
        self.glyphSelectorTitle.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setBold(True)
        self.glyphSelectorTitle.setFont(font)
        self.glyphSelectorTitle.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.glyphSelectorTitle)

        self.glyphSelectorList = QListWidget(self.selectorList)
        self.glyphSelectorList.setObjectName(u"glyphSelectorList")

        self.verticalLayout_3.addWidget(self.glyphSelectorList)

        self.verticalLayout_3.setStretch(0, 1)

        self.verticalLayout.addWidget(self.selectorList)

        self.fontSettings = QWidget(self.glyphSelector)
        self.fontSettings.setObjectName(u"fontSettings")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fontSettings.sizePolicy().hasHeightForWidth())
        self.fontSettings.setSizePolicy(sizePolicy2)
        self.verticalLayout_4 = QVBoxLayout(self.fontSettings)
        self.verticalLayout_4.setSpacing(14)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.fontSettingsTitle = QLabel(self.fontSettings)
        self.fontSettingsTitle.setObjectName(u"fontSettingsTitle")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fontSettingsTitle.sizePolicy().hasHeightForWidth())
        self.fontSettingsTitle.setSizePolicy(sizePolicy3)
        self.fontSettingsTitle.setFont(font)

        self.verticalLayout_4.addWidget(self.fontSettingsTitle)

        self.fontSettingsWidget = QWidget(self.fontSettings)
        self.fontSettingsWidget.setObjectName(u"fontSettingsWidget")
        sizePolicy3.setHeightForWidth(self.fontSettingsWidget.sizePolicy().hasHeightForWidth())
        self.fontSettingsWidget.setSizePolicy(sizePolicy3)
        self.gridLayout = QGridLayout(self.fontSettingsWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.fontDefaultWidthBox = QSpinBox(self.fontSettingsWidget)
        self.fontDefaultWidthBox.setObjectName(u"fontDefaultWidthBox")
        sizePolicy3.setHeightForWidth(self.fontDefaultWidthBox.sizePolicy().hasHeightForWidth())
        self.fontDefaultWidthBox.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.fontDefaultWidthBox, 4, 1, 1, 1)

        self.fontHeightTitle = QLabel(self.fontSettingsWidget)
        self.fontHeightTitle.setObjectName(u"fontHeightTitle")
        sizePolicy3.setHeightForWidth(self.fontHeightTitle.sizePolicy().hasHeightForWidth())
        self.fontHeightTitle.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.fontHeightTitle, 2, 0, 1, 1)

        self.fontDefaultSpacingTitle = QLabel(self.fontSettingsWidget)
        self.fontDefaultSpacingTitle.setObjectName(u"fontDefaultSpacingTitle")
        sizePolicy3.setHeightForWidth(self.fontDefaultSpacingTitle.sizePolicy().hasHeightForWidth())
        self.fontDefaultSpacingTitle.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.fontDefaultSpacingTitle, 3, 0, 1, 1)

        self.fontDefaultSpacingBox = QSpinBox(self.fontSettingsWidget)
        self.fontDefaultSpacingBox.setObjectName(u"fontDefaultSpacingBox")
        sizePolicy3.setHeightForWidth(self.fontDefaultSpacingBox.sizePolicy().hasHeightForWidth())
        self.fontDefaultSpacingBox.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.fontDefaultSpacingBox, 3, 1, 1, 1)

        self.fontNameTitle = QLabel(self.fontSettingsWidget)
        self.fontNameTitle.setObjectName(u"fontNameTitle")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.fontNameTitle.sizePolicy().hasHeightForWidth())
        self.fontNameTitle.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.fontNameTitle, 0, 0, 1, 1)

        self.fontDefaultWidthTitle = QLabel(self.fontSettingsWidget)
        self.fontDefaultWidthTitle.setObjectName(u"fontDefaultWidthTitle")
        sizePolicy3.setHeightForWidth(self.fontDefaultWidthTitle.sizePolicy().hasHeightForWidth())
        self.fontDefaultWidthTitle.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.fontDefaultWidthTitle, 4, 0, 1, 1)

        self.fontHeightBox = QSpinBox(self.fontSettingsWidget)
        self.fontHeightBox.setObjectName(u"fontHeightBox")
        sizePolicy3.setHeightForWidth(self.fontHeightBox.sizePolicy().hasHeightForWidth())
        self.fontHeightBox.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.fontHeightBox, 2, 1, 1, 1)

        self.fontNameBox = QLineEdit(self.fontSettingsWidget)
        self.fontNameBox.setObjectName(u"fontNameBox")
        self.fontNameBox.setMinimumSize(QSize(0, 0))
        self.fontNameBox.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.fontNameBox, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.fontSettingsWidget)


        self.verticalLayout.addWidget(self.fontSettings)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout.addWidget(self.glyphSelector)

        self.glyphDesigner = QWidget(self.centralwidget)
        self.glyphDesigner.setObjectName(u"glyphDesigner")
        self.glyphDesigner.setMaximumSize(QSize(100000, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.glyphDesigner)
        self.verticalLayout_5.setSpacing(14)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 12, -1, -1)
        self.glyphDesignerContainer = QWidget(self.glyphDesigner)
        self.glyphDesignerContainer.setObjectName(u"glyphDesignerContainer")
        sizePolicy.setHeightForWidth(self.glyphDesignerContainer.sizePolicy().hasHeightForWidth())
        self.glyphDesignerContainer.setSizePolicy(sizePolicy)
        self.glyphDesignerContainer.setMinimumSize(QSize(0, 0))
        self.verticalLayout_6 = QVBoxLayout(self.glyphDesignerContainer)
        self.verticalLayout_6.setSpacing(14)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.selectedGlyphTitle = QLabel(self.glyphDesignerContainer)
        self.selectedGlyphTitle.setObjectName(u"selectedGlyphTitle")
        sizePolicy1.setHeightForWidth(self.selectedGlyphTitle.sizePolicy().hasHeightForWidth())
        self.selectedGlyphTitle.setSizePolicy(sizePolicy1)
        self.selectedGlyphTitle.setFont(font)
        self.selectedGlyphTitle.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_6.addWidget(self.selectedGlyphTitle)

        self.glyphCanvas = GlyphCanvas(self.glyphDesignerContainer)
        self.glyphCanvas.setObjectName(u"glyphCanvas")

        self.verticalLayout_6.addWidget(self.glyphCanvas)


        self.verticalLayout_5.addWidget(self.glyphDesignerContainer)

        self.glyphSettings = QWidget(self.glyphDesigner)
        self.glyphSettings.setObjectName(u"glyphSettings")
        sizePolicy2.setHeightForWidth(self.glyphSettings.sizePolicy().hasHeightForWidth())
        self.glyphSettings.setSizePolicy(sizePolicy2)
        self.glyphSettings.setMinimumSize(QSize(0, 157))
        self.verticalLayout_2 = QVBoxLayout(self.glyphSettings)
        self.verticalLayout_2.setSpacing(14)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.glyphSettingsTitle = QLabel(self.glyphSettings)
        self.glyphSettingsTitle.setObjectName(u"glyphSettingsTitle")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.glyphSettingsTitle.sizePolicy().hasHeightForWidth())
        self.glyphSettingsTitle.setSizePolicy(sizePolicy5)
        self.glyphSettingsTitle.setFont(font)

        self.verticalLayout_2.addWidget(self.glyphSettingsTitle)

        self.glyphSettingsGrid = QWidget(self.glyphSettings)
        self.glyphSettingsGrid.setObjectName(u"glyphSettingsGrid")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.glyphSettingsGrid.sizePolicy().hasHeightForWidth())
        self.glyphSettingsGrid.setSizePolicy(sizePolicy6)
        self.gridLayout_2 = QGridLayout(self.glyphSettingsGrid)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.identiferCharBox = QLineEdit(self.glyphSettingsGrid)
        self.identiferCharBox.setObjectName(u"identiferCharBox")
        self.identiferCharBox.setMinimumSize(QSize(0, 0))
        self.identiferCharBox.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self.identiferCharBox, 0, 1, 1, 1)

        self.widthBox = QSpinBox(self.glyphSettingsGrid)
        self.widthBox.setObjectName(u"widthBox")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widthBox.sizePolicy().hasHeightForWidth())
        self.widthBox.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.widthBox, 1, 1, 1, 1)

        self.widthLabel = QLabel(self.glyphSettingsGrid)
        self.widthLabel.setObjectName(u"widthLabel")

        self.gridLayout_2.addWidget(self.widthLabel, 1, 0, 1, 1)

        self.identiferCharLabel = QLabel(self.glyphSettingsGrid)
        self.identiferCharLabel.setObjectName(u"identiferCharLabel")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.identiferCharLabel.sizePolicy().hasHeightForWidth())
        self.identiferCharLabel.setSizePolicy(sizePolicy8)

        self.gridLayout_2.addWidget(self.identiferCharLabel, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.glyphSettingsGrid)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout_5.addWidget(self.glyphSettings)

        self.verticalLayout_5.setStretch(0, 3)

        self.horizontalLayout.addWidget(self.glyphDesigner)

        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(1, 13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 733, 30))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuGrid = QMenu(self.menuBar)
        self.menuGrid.setObjectName(u"menuGrid")
        self.menuShift = QMenu(self.menuGrid)
        self.menuShift.setObjectName(u"menuShift")
        self.menuGlyph = QMenu(self.menuBar)
        self.menuGlyph.setObjectName(u"menuGlyph")
        self.menuDelete = QMenu(self.menuGlyph)
        self.menuDelete.setObjectName(u"menuDelete")
        self.menuPreview = QMenu(self.menuBar)
        self.menuPreview.setObjectName(u"menuPreview")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuGrid.menuAction())
        self.menuBar.addAction(self.menuGlyph.menuAction())
        self.menuBar.addAction(self.menuPreview.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_to_new_file)
        self.menuGrid.addAction(self.menuShift.menuAction())
        self.menuGrid.addAction(self.actionInvert)
        self.menuGrid.addSeparator()
        self.menuGrid.addAction(self.actionClear)
        self.menuShift.addAction(self.actionUp)
        self.menuShift.addAction(self.actionDown)
        self.menuShift.addAction(self.actionLeft)
        self.menuShift.addAction(self.actionRight)
        self.menuGlyph.addAction(self.actionAdd)
        self.menuGlyph.addSeparator()
        self.menuGlyph.addAction(self.menuDelete.menuAction())
        self.menuDelete.addAction(self.actionSelected)
        self.menuDelete.addAction(self.actionAll)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_to_new_file.setText(QCoreApplication.translate("MainWindow", u"Save as...", None))
        self.actionLeft.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.actionUp.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.actionDown.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.actionRight.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.actionInvert.setText(QCoreApplication.translate("MainWindow", u"Invert", None))
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.actionAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.actionSelected.setText(QCoreApplication.translate("MainWindow", u"Selected", None))
        self.actionAll.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.actionTo_defaults.setText(QCoreApplication.translate("MainWindow", u"To defaults", None))
        self.glyphSelectorTitle.setText(QCoreApplication.translate("MainWindow", u"Glyph selector", None))
        self.fontSettingsTitle.setText(QCoreApplication.translate("MainWindow", u"Font settings", None))
        self.fontHeightTitle.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.fontDefaultSpacingTitle.setText(QCoreApplication.translate("MainWindow", u"Default spacing", None))
        self.fontNameTitle.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.fontDefaultWidthTitle.setText(QCoreApplication.translate("MainWindow", u"Default width", None))
        self.selectedGlyphTitle.setText(QCoreApplication.translate("MainWindow", u"Selected glyph: X", None))
        self.glyphSettingsTitle.setText(QCoreApplication.translate("MainWindow", u"Glyph settings", None))
        self.widthLabel.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.identiferCharLabel.setText(QCoreApplication.translate("MainWindow", u"Identifier / char", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuGrid.setTitle(QCoreApplication.translate("MainWindow", u"Grid", None))
        self.menuShift.setTitle(QCoreApplication.translate("MainWindow", u"Shift", None))
        self.menuGlyph.setTitle(QCoreApplication.translate("MainWindow", u"Glyph", None))
        self.menuDelete.setTitle(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.menuPreview.setTitle(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.actionOpenPreview = QAction(MainWindow)
        self.actionOpenPreview.setObjectName("actionOpenPreview")
        self.menuPreview.addAction(self.actionOpenPreview)
        self.actionOpenPreview.setText(
            QCoreApplication.translate("MainWindow", "Open preview", None)
        )
        
    # retranslateUi

