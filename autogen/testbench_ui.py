# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:\Data\Devel\AnalyseImage\widgets\ui\testbench.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TestBench(object):
    def setupUi(self, TestBench):
        TestBench.setObjectName("TestBench")
        TestBench.resize(1133, 890)
        self.centralwidget = QtWidgets.QWidget(TestBench)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(5)
        self.splitter.setObjectName("splitter")
        self.UpFrame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.UpFrame.sizePolicy().hasHeightForWidth())
        self.UpFrame.setSizePolicy(sizePolicy)
        self.UpFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UpFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UpFrame.setObjectName("UpFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.UpFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabsWidget = QtWidgets.QTabWidget(self.UpFrame)
        self.tabsWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabsWidget.sizePolicy().hasHeightForWidth())
        self.tabsWidget.setSizePolicy(sizePolicy)
        self.tabsWidget.setTabsClosable(True)
        self.tabsWidget.setMovable(True)
        self.tabsWidget.setObjectName("tabsWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tabsWidget.addTab(self.tab, "")
        self.horizontalLayout.addWidget(self.tabsWidget)
        self.filtersGroup = QtWidgets.QGroupBox(self.UpFrame)
        self.filtersGroup.setObjectName("filtersGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.filtersGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.filtersGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(False)
        self.verticalLayout.addWidget(self.treeWidget)
        self.groupBox = QtWidgets.QGroupBox(self.filtersGroup)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setObjectName("tabWidget")
        self.defaultPipelineTab = QtWidgets.QWidget()
        self.defaultPipelineTab.setObjectName("defaultPipelineTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.defaultPipelineTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.defaultPipelineTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.tabWidget.addTab(self.defaultPipelineTab, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.Up = QtWidgets.QPushButton(self.frame_2)
        self.Up.setObjectName("Up")
        self.verticalLayout_2.addWidget(self.Up)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addWidget(self.filtersGroup)
        self.DownFrame = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.DownFrame.sizePolicy().hasHeightForWidth())
        self.DownFrame.setSizePolicy(sizePolicy)
        self.DownFrame.setObjectName("DownFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.DownFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.messagesWidget = QtWidgets.QPlainTextEdit(self.DownFrame)
        self.messagesWidget.setObjectName("messagesWidget")
        self.verticalLayout_3.addWidget(self.messagesWidget)
        self.verticalLayout_4.addWidget(self.splitter)
        TestBench.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TestBench)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1133, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        TestBench.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TestBench)
        self.statusbar.setObjectName("statusbar")
        TestBench.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(TestBench)
        self.toolBar.setObjectName("toolBar")
        TestBench.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Quit = QtWidgets.QAction(TestBench)
        icon = QtGui.QIcon.fromTheme(":/img/close.png")
        self.action_Quit.setIcon(icon)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Open = QtWidgets.QAction(TestBench)
        icon = QtGui.QIcon.fromTheme(":/img/open.png")
        self.action_Open.setIcon(icon)
        self.action_Open.setObjectName("action_Open")
        self.action_Save = QtWidgets.QAction(TestBench)
        icon = QtGui.QIcon.fromTheme(":/img/save.png")
        self.action_Save.setIcon(icon)
        self.action_Save.setObjectName("action_Save")
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_Quit)
        self.menubar.addAction(self.menu_File.menuAction())
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addAction(self.action_Save)
        self.toolBar.addAction(self.action_Quit)

        self.retranslateUi(TestBench)
        self.tabsWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TestBench)

    def retranslateUi(self, TestBench):
        _translate = QtCore.QCoreApplication.translate
        TestBench.setWindowTitle(_translate("TestBench", "MainWindow"))
        self.tabsWidget.setTabText(self.tabsWidget.indexOf(self.tab), _translate("TestBench", "No Images"))
        self.filtersGroup.setTitle(_translate("TestBench", "Filters"))
        self.treeWidget.headerItem().setText(0, _translate("TestBench", "Name"))
        self.groupBox.setTitle(_translate("TestBench", "Filters Pipeline"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.defaultPipelineTab), _translate("TestBench", "Default"))
        self.pushButton_4.setText(_translate("TestBench", "Add Filter"))
        self.Up.setText(_translate("TestBench", "Move Up"))
        self.pushButton.setText(_translate("TestBench", "Move Down"))
        self.pushButton_2.setText(_translate("TestBench", "Properties"))
        self.pushButton_3.setText(_translate("TestBench", "Delete"))
        self.pushButton_5.setText(_translate("TestBench", "Show Result"))
        self.DownFrame.setTitle(_translate("TestBench", "Messages"))
        self.menu_File.setTitle(_translate("TestBench", "&File"))
        self.toolBar.setWindowTitle(_translate("TestBench", "toolBar"))
        self.action_Quit.setText(_translate("TestBench", "&Quit"))
        self.action_Open.setText(_translate("TestBench", "&Open"))
        self.action_Save.setText(_translate("TestBench", "Save"))
from . import resources_rc