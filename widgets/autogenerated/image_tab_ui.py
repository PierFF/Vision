# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:\Data\Devel\AnalyseImage\widgets\ui\image_tab.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_image_tab(object):
    def setupUi(self, image_tab):
        image_tab.setObjectName("image_tab")
        image_tab.resize(831, 602)
        self.horizontalLayout = QtWidgets.QHBoxLayout(image_tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frameL = QtWidgets.QFrame(image_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameL.sizePolicy().hasHeightForWidth())
        self.frameL.setSizePolicy(sizePolicy)
        self.frameL.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameL.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameL.setObjectName("frameL")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameL)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.graphicsViewL = ImageView(self.frameL)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsViewL.sizePolicy().hasHeightForWidth())
        self.graphicsViewL.setSizePolicy(sizePolicy)
        self.graphicsViewL.setObjectName("graphicsViewL")
        self.verticalLayout_5.addWidget(self.graphicsViewL)
        self.frame_4 = QtWidgets.QFrame(self.frameL)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setLineWidth(2)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame_4)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_5.addWidget(self.toolButton_2)
        self.toolButton = QtWidgets.QToolButton(self.frame_4)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_5.addWidget(self.toolButton)
        self.toolButton_3 = QtWidgets.QToolButton(self.frame_4)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_5.addWidget(self.toolButton_3)
        self.toolButton_4 = QtWidgets.QToolButton(self.frame_4)
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_5.addWidget(self.toolButton_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.toolButton_5 = QtWidgets.QToolButton(self.frame_4)
        self.toolButton_5.setObjectName("toolButton_5")
        self.horizontalLayout_5.addWidget(self.toolButton_5)
        self.toolButton_6 = QtWidgets.QToolButton(self.frame_4)
        self.toolButton_6.setObjectName("toolButton_6")
        self.horizontalLayout_5.addWidget(self.toolButton_6)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frameL)
        self.frame = QtWidgets.QFrame(image_tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.linkButton = QtWidgets.QPushButton(self.frame)
        self.linkButton.setEnabled(False)
        self.linkButton.setCheckable(True)
        self.linkButton.setFlat(False)
        self.linkButton.setObjectName("linkButton")
        self.verticalLayout.addWidget(self.linkButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.frame)
        self.frameR = QtWidgets.QFrame(image_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameR.sizePolicy().hasHeightForWidth())
        self.frameR.setSizePolicy(sizePolicy)
        self.frameR.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameR.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameR.setObjectName("frameR")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frameR)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graphicsViewR = ImageView(self.frameR)
        self.graphicsViewR.setObjectName("graphicsViewR")
        self.verticalLayout_6.addWidget(self.graphicsViewR)
        self.tollFrameR = QtWidgets.QFrame(self.frameR)
        self.tollFrameR.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tollFrameR.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tollFrameR.setObjectName("tollFrameR")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tollFrameR)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.toolButton_8 = QtWidgets.QToolButton(self.tollFrameR)
        self.toolButton_8.setObjectName("toolButton_8")
        self.horizontalLayout_4.addWidget(self.toolButton_8)
        self.toolButton_9 = QtWidgets.QToolButton(self.tollFrameR)
        self.toolButton_9.setObjectName("toolButton_9")
        self.horizontalLayout_4.addWidget(self.toolButton_9)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.toolButton_10 = QtWidgets.QToolButton(self.tollFrameR)
        self.toolButton_10.setObjectName("toolButton_10")
        self.horizontalLayout_4.addWidget(self.toolButton_10)
        self.toolButton_7 = QtWidgets.QToolButton(self.tollFrameR)
        self.toolButton_7.setObjectName("toolButton_7")
        self.horizontalLayout_4.addWidget(self.toolButton_7)
        self.verticalLayout_6.addWidget(self.tollFrameR)
        self.horizontalLayout.addWidget(self.frameR)

        self.retranslateUi(image_tab)
        QtCore.QMetaObject.connectSlotsByName(image_tab)

    def retranslateUi(self, image_tab):
        _translate = QtCore.QCoreApplication.translate
        image_tab.setWindowTitle(_translate("image_tab", "Image Tab"))
        self.toolButton_2.setText(_translate("image_tab", "..."))
        self.toolButton.setText(_translate("image_tab", "..."))
        self.toolButton_3.setText(_translate("image_tab", "..."))
        self.toolButton_4.setText(_translate("image_tab", "..."))
        self.toolButton_5.setText(_translate("image_tab", "..."))
        self.toolButton_6.setText(_translate("image_tab", "..."))
        self.pushButton.setText(_translate("image_tab", "PushButton"))
        self.linkButton.setText(_translate("image_tab", "PushButton"))
        self.toolButton_8.setText(_translate("image_tab", "..."))
        self.toolButton_9.setText(_translate("image_tab", "..."))
        self.toolButton_10.setText(_translate("image_tab", "..."))
        self.toolButton_7.setText(_translate("image_tab", "..."))
from widgets.image_view import ImageView
