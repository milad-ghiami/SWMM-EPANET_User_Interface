# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EPANET\frmReportOptionsDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmReportOptions(object):
    def setupUi(self, frmReportOptions):
        frmReportOptions.setObjectName("frmReportOptions")
        frmReportOptions.resize(386, 892)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmReportOptions.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmReportOptions)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fraTop = QtWidgets.QFrame(self.centralWidget)
        self.fraTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraTop.setObjectName("fraTop")
        self.gridLayout = QtWidgets.QGridLayout(self.fraTop)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lblPageSize = QtWidgets.QLabel(self.fraTop)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPageSize.setFont(font)
        self.lblPageSize.setObjectName("lblPageSize")
        self.gridLayout.addWidget(self.lblPageSize, 0, 0, 1, 1)
        self.txtPageSize = QtWidgets.QLineEdit(self.fraTop)
        self.txtPageSize.setObjectName("txtPageSize")
        self.gridLayout.addWidget(self.txtPageSize, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.lblReportFileName = QtWidgets.QLabel(self.fraTop)
        self.lblReportFileName.setObjectName("lblReportFileName")
        self.gridLayout.addWidget(self.lblReportFileName, 1, 0, 1, 1)
        self.txtReportFileName = QtWidgets.QLineEdit(self.fraTop)
        self.txtReportFileName.setObjectName("txtReportFileName")
        self.gridLayout.addWidget(self.txtReportFileName, 1, 1, 1, 2)
        self.lblStatus = QtWidgets.QLabel(self.fraTop)
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout.addWidget(self.lblStatus, 2, 0, 1, 1)
        self.cboStatus = QtWidgets.QComboBox(self.fraTop)
        self.cboStatus.setObjectName("cboStatus")
        self.gridLayout.addWidget(self.cboStatus, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.lblSummary = QtWidgets.QLabel(self.fraTop)
        self.lblSummary.setObjectName("lblSummary")
        self.gridLayout.addWidget(self.lblSummary, 3, 0, 1, 1)
        self.cboSummary = QtWidgets.QComboBox(self.fraTop)
        self.cboSummary.setObjectName("cboSummary")
        self.gridLayout.addWidget(self.cboSummary, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        self.lblEnergy = QtWidgets.QLabel(self.fraTop)
        self.lblEnergy.setObjectName("lblEnergy")
        self.gridLayout.addWidget(self.lblEnergy, 4, 0, 1, 1)
        self.cboEnergy = QtWidgets.QComboBox(self.fraTop)
        self.cboEnergy.setObjectName("cboEnergy")
        self.gridLayout.addWidget(self.cboEnergy, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 2, 1, 1)
        self.verticalLayout.addWidget(self.fraTop)
        self.gbxNode = QtWidgets.QGroupBox(self.centralWidget)
        self.gbxNode.setObjectName("gbxNode")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gbxNode)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblLimit = QtWidgets.QLabel(self.gbxNode)
        self.lblLimit.setObjectName("lblLimit")
        self.gridLayout_2.addWidget(self.lblLimit, 0, 1, 1, 1)
        self.lblPrecision = QtWidgets.QLabel(self.gbxNode)
        self.lblPrecision.setObjectName("lblPrecision")
        self.gridLayout_2.addWidget(self.lblPrecision, 0, 3, 1, 1)
        self.cbxNode1 = QtWidgets.QCheckBox(self.gbxNode)
        self.cbxNode1.setObjectName("cbxNode1")
        self.gridLayout_2.addWidget(self.cbxNode1, 1, 0, 1, 1)
        self.cboNode1 = QtWidgets.QComboBox(self.gbxNode)
        self.cboNode1.setObjectName("cboNode1")
        self.gridLayout_2.addWidget(self.cboNode1, 1, 1, 1, 1)
        self.txtNode1 = QtWidgets.QLineEdit(self.gbxNode)
        self.txtNode1.setObjectName("txtNode1")
        self.gridLayout_2.addWidget(self.txtNode1, 1, 2, 1, 1)
        self.txtNode6 = QtWidgets.QLineEdit(self.gbxNode)
        self.txtNode6.setObjectName("txtNode6")
        self.gridLayout_2.addWidget(self.txtNode6, 1, 3, 1, 1)
        self.cbxNode2 = QtWidgets.QCheckBox(self.gbxNode)
        self.cbxNode2.setObjectName("cbxNode2")
        self.gridLayout_2.addWidget(self.cbxNode2, 2, 0, 1, 1)
        self.cboNode2 = QtWidgets.QComboBox(self.gbxNode)
        self.cboNode2.setObjectName("cboNode2")
        self.gridLayout_2.addWidget(self.cboNode2, 2, 1, 1, 1)
        self.txtNode2 = QtWidgets.QLineEdit(self.gbxNode)
        self.txtNode2.setObjectName("txtNode2")
        self.gridLayout_2.addWidget(self.txtNode2, 2, 2, 1, 1)
        self.txtNode7 = QtWidgets.QLineEdit(self.gbxNode)
        self.txtNode7.setObjectName("txtNode7")
        self.gridLayout_2.addWidget(self.txtNode7, 2, 3, 1, 1)
        self.cbxNode3 = QtWidgets.QCheckBox(self.gbxNode)
        self.cbxNode3.setObjectName("cbxNode3")
        self.gridLayout_2.addWidget(self.cbxNode3, 3, 0, 1, 1)
        self.cboNode3 = QtWidgets.QComboBox(self.gbxNode)
        self.cboNode3.setObjectName("cboNode3")
        self.gridLayout_2.addWidget(self.cboNode3, 3, 1, 1, 1)
        self.txtNode3 = QtWidgets.QLineEdit(self.gbxNode)
        self.txtNode3.setObjectName("txtNode3")
        self.gridLayout_2.addWidget(self.txtNode3, 3, 2, 1, 1)
        self.txtNode8 = QtWidgets.QLineEdit(self.gbxNode)
        self.txtNode8.setObjectName("txtNode8")
        self.gridLayout_2.addWidget(self.txtNode8, 3, 3, 1, 1)
        self.cbxNode4 = QtWidgets.QCheckBox(self.gbxNode)
        self.cbxNode4.setObjectName("cbxNode4")
        self.gridLayout_2.addWidget(self.cbxNode4, 4, 0, 1, 1)
        self.cboNode4 = QtWidgets.QComboBox(self.gbxNode)
        self.cboNode4.setObjectName("cboNode4")
        self.gridLayout_2.addWidget(self.cboNode4, 4, 1, 1, 1)
        self.txtNode4 = QtWidgets.QLineEdit(self.gbxNode)
        self.txtNode4.setObjectName("txtNode4")
        self.gridLayout_2.addWidget(self.txtNode4, 4, 2, 1, 1)
        self.txtNode9 = QtWidgets.QLineEdit(self.gbxNode)
        self.txtNode9.setObjectName("txtNode9")
        self.gridLayout_2.addWidget(self.txtNode9, 4, 3, 1, 1)
        self.cbxNode5 = QtWidgets.QCheckBox(self.gbxNode)
        self.cbxNode5.setObjectName("cbxNode5")
        self.gridLayout_2.addWidget(self.cbxNode5, 5, 0, 1, 1)
        self.cboNode5 = QtWidgets.QComboBox(self.gbxNode)
        self.cboNode5.setObjectName("cboNode5")
        self.gridLayout_2.addWidget(self.cboNode5, 5, 1, 1, 1)
        self.txtNode5 = QtWidgets.QLineEdit(self.gbxNode)
        self.txtNode5.setObjectName("txtNode5")
        self.gridLayout_2.addWidget(self.txtNode5, 5, 2, 1, 1)
        self.txtNode10 = QtWidgets.QLineEdit(self.gbxNode)
        self.txtNode10.setObjectName("txtNode10")
        self.gridLayout_2.addWidget(self.txtNode10, 5, 3, 1, 1)
        self.verticalLayout.addWidget(self.gbxNode)
        self.gbxLink = QtWidgets.QGroupBox(self.centralWidget)
        self.gbxLink.setObjectName("gbxLink")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gbxLink)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblLimitLink = QtWidgets.QLabel(self.gbxLink)
        self.lblLimitLink.setObjectName("lblLimitLink")
        self.gridLayout_3.addWidget(self.lblLimitLink, 0, 1, 1, 1)
        self.lblPrecisionLink = QtWidgets.QLabel(self.gbxLink)
        self.lblPrecisionLink.setObjectName("lblPrecisionLink")
        self.gridLayout_3.addWidget(self.lblPrecisionLink, 0, 3, 1, 1)
        self.cbxLink1 = QtWidgets.QCheckBox(self.gbxLink)
        self.cbxLink1.setObjectName("cbxLink1")
        self.gridLayout_3.addWidget(self.cbxLink1, 1, 0, 1, 1)
        self.cboLink1 = QtWidgets.QComboBox(self.gbxLink)
        self.cboLink1.setObjectName("cboLink1")
        self.gridLayout_3.addWidget(self.cboLink1, 1, 1, 1, 1)
        self.txtLink1 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink1.setObjectName("txtLink1")
        self.gridLayout_3.addWidget(self.txtLink1, 1, 2, 1, 1)
        self.txtLink10 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink10.setObjectName("txtLink10")
        self.gridLayout_3.addWidget(self.txtLink10, 1, 3, 1, 1)
        self.cbxLink2 = QtWidgets.QCheckBox(self.gbxLink)
        self.cbxLink2.setObjectName("cbxLink2")
        self.gridLayout_3.addWidget(self.cbxLink2, 2, 0, 1, 1)
        self.cboLink2 = QtWidgets.QComboBox(self.gbxLink)
        self.cboLink2.setObjectName("cboLink2")
        self.gridLayout_3.addWidget(self.cboLink2, 2, 1, 1, 1)
        self.txtLink2 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink2.setObjectName("txtLink2")
        self.gridLayout_3.addWidget(self.txtLink2, 2, 2, 1, 1)
        self.txtLink11 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink11.setObjectName("txtLink11")
        self.gridLayout_3.addWidget(self.txtLink11, 2, 3, 1, 1)
        self.cbxLink3 = QtWidgets.QCheckBox(self.gbxLink)
        self.cbxLink3.setObjectName("cbxLink3")
        self.gridLayout_3.addWidget(self.cbxLink3, 3, 0, 1, 1)
        self.cboLink3 = QtWidgets.QComboBox(self.gbxLink)
        self.cboLink3.setObjectName("cboLink3")
        self.gridLayout_3.addWidget(self.cboLink3, 3, 1, 1, 1)
        self.txtLink3 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink3.setObjectName("txtLink3")
        self.gridLayout_3.addWidget(self.txtLink3, 3, 2, 1, 1)
        self.txtLink12 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink12.setObjectName("txtLink12")
        self.gridLayout_3.addWidget(self.txtLink12, 3, 3, 1, 1)
        self.cbxLink4 = QtWidgets.QCheckBox(self.gbxLink)
        self.cbxLink4.setObjectName("cbxLink4")
        self.gridLayout_3.addWidget(self.cbxLink4, 4, 0, 1, 1)
        self.cboLink4 = QtWidgets.QComboBox(self.gbxLink)
        self.cboLink4.setObjectName("cboLink4")
        self.gridLayout_3.addWidget(self.cboLink4, 4, 1, 1, 1)
        self.txtLink4 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink4.setObjectName("txtLink4")
        self.gridLayout_3.addWidget(self.txtLink4, 4, 2, 1, 1)
        self.txtLink13 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink13.setObjectName("txtLink13")
        self.gridLayout_3.addWidget(self.txtLink13, 4, 3, 1, 1)
        self.cbxLink5 = QtWidgets.QCheckBox(self.gbxLink)
        self.cbxLink5.setObjectName("cbxLink5")
        self.gridLayout_3.addWidget(self.cbxLink5, 5, 0, 1, 1)
        self.cboLink5 = QtWidgets.QComboBox(self.gbxLink)
        self.cboLink5.setObjectName("cboLink5")
        self.gridLayout_3.addWidget(self.cboLink5, 5, 1, 1, 1)
        self.txtLink5 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink5.setObjectName("txtLink5")
        self.gridLayout_3.addWidget(self.txtLink5, 5, 2, 1, 1)
        self.txtLink14 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink14.setObjectName("txtLink14")
        self.gridLayout_3.addWidget(self.txtLink14, 5, 3, 1, 1)
        self.cbxLink6 = QtWidgets.QCheckBox(self.gbxLink)
        self.cbxLink6.setObjectName("cbxLink6")
        self.gridLayout_3.addWidget(self.cbxLink6, 6, 0, 1, 1)
        self.cboLink6 = QtWidgets.QComboBox(self.gbxLink)
        self.cboLink6.setObjectName("cboLink6")
        self.gridLayout_3.addWidget(self.cboLink6, 6, 1, 1, 1)
        self.txtLink6 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink6.setObjectName("txtLink6")
        self.gridLayout_3.addWidget(self.txtLink6, 6, 2, 1, 1)
        self.txtLink15 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink15.setObjectName("txtLink15")
        self.gridLayout_3.addWidget(self.txtLink15, 6, 3, 1, 1)
        self.cbxLink7 = QtWidgets.QCheckBox(self.gbxLink)
        self.cbxLink7.setObjectName("cbxLink7")
        self.gridLayout_3.addWidget(self.cbxLink7, 7, 0, 1, 1)
        self.cboLink7 = QtWidgets.QComboBox(self.gbxLink)
        self.cboLink7.setObjectName("cboLink7")
        self.gridLayout_3.addWidget(self.cboLink7, 7, 1, 1, 1)
        self.txtLink7 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink7.setObjectName("txtLink7")
        self.gridLayout_3.addWidget(self.txtLink7, 7, 2, 1, 1)
        self.txtLink16 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink16.setObjectName("txtLink16")
        self.gridLayout_3.addWidget(self.txtLink16, 7, 3, 1, 1)
        self.cbxLink8 = QtWidgets.QCheckBox(self.gbxLink)
        self.cbxLink8.setObjectName("cbxLink8")
        self.gridLayout_3.addWidget(self.cbxLink8, 8, 0, 1, 1)
        self.cboLink8 = QtWidgets.QComboBox(self.gbxLink)
        self.cboLink8.setObjectName("cboLink8")
        self.gridLayout_3.addWidget(self.cboLink8, 8, 1, 1, 1)
        self.txtLink8 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink8.setObjectName("txtLink8")
        self.gridLayout_3.addWidget(self.txtLink8, 8, 2, 1, 1)
        self.txtLink17 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink17.setObjectName("txtLink17")
        self.gridLayout_3.addWidget(self.txtLink17, 8, 3, 1, 1)
        self.cbxLink9 = QtWidgets.QCheckBox(self.gbxLink)
        self.cbxLink9.setObjectName("cbxLink9")
        self.gridLayout_3.addWidget(self.cbxLink9, 9, 0, 1, 1)
        self.cboLink9 = QtWidgets.QComboBox(self.gbxLink)
        self.cboLink9.setObjectName("cboLink9")
        self.gridLayout_3.addWidget(self.cboLink9, 9, 1, 1, 1)
        self.txtLink9 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink9.setObjectName("txtLink9")
        self.gridLayout_3.addWidget(self.txtLink9, 9, 2, 1, 1)
        self.txtLink18 = QtWidgets.QLineEdit(self.gbxLink)
        self.txtLink18.setObjectName("txtLink18")
        self.gridLayout_3.addWidget(self.txtLink18, 9, 3, 1, 1)
        self.verticalLayout.addWidget(self.gbxLink)
        self.fraOKCancel = QtWidgets.QFrame(self.centralWidget)
        self.fraOKCancel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraOKCancel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraOKCancel.setObjectName("fraOKCancel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fraOKCancel)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(183, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.cmdOK = QtWidgets.QPushButton(self.fraOKCancel)
        self.cmdOK.setObjectName("cmdOK")
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtWidgets.QPushButton(self.fraOKCancel)
        self.cmdCancel.setObjectName("cmdCancel")
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout.addWidget(self.fraOKCancel)
        frmReportOptions.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmReportOptions)
        QtCore.QMetaObject.connectSlotsByName(frmReportOptions)

    def retranslateUi(self, frmReportOptions):
        _translate = QtCore.QCoreApplication.translate
        frmReportOptions.setWindowTitle(_translate("frmReportOptions", "EPANET Report Options"))
        self.lblPageSize.setText(_translate("frmReportOptions", "Page Size"))
        self.lblReportFileName.setText(_translate("frmReportOptions", "<html><head/><body><p>Report File Name</p></body></html>"))
        self.lblStatus.setText(_translate("frmReportOptions", "Status"))
        self.lblSummary.setText(_translate("frmReportOptions", "Summary"))
        self.lblEnergy.setText(_translate("frmReportOptions", "Energy"))
        self.gbxNode.setTitle(_translate("frmReportOptions", "Node Parameters:"))
        self.lblLimit.setText(_translate("frmReportOptions", "Limit"))
        self.lblPrecision.setText(_translate("frmReportOptions", "Precision"))
        self.cbxNode1.setText(_translate("frmReportOptions", "Elevation"))
        self.cbxNode2.setText(_translate("frmReportOptions", "Demand"))
        self.cbxNode3.setText(_translate("frmReportOptions", "Head"))
        self.cbxNode4.setText(_translate("frmReportOptions", "Pressure"))
        self.cbxNode5.setText(_translate("frmReportOptions", "Quality"))
        self.gbxLink.setTitle(_translate("frmReportOptions", "Link Parameters:"))
        self.lblLimitLink.setText(_translate("frmReportOptions", "Limit"))
        self.lblPrecisionLink.setText(_translate("frmReportOptions", "Precision"))
        self.cbxLink1.setText(_translate("frmReportOptions", "Length"))
        self.cbxLink2.setText(_translate("frmReportOptions", "Diameter"))
        self.cbxLink3.setText(_translate("frmReportOptions", "Flow"))
        self.cbxLink4.setText(_translate("frmReportOptions", "Velocity"))
        self.cbxLink5.setText(_translate("frmReportOptions", "Headloss"))
        self.cbxLink6.setText(_translate("frmReportOptions", "Position"))
        self.cbxLink7.setText(_translate("frmReportOptions", "Setting"))
        self.cbxLink8.setText(_translate("frmReportOptions", "Reaction"))
        self.cbxLink9.setText(_translate("frmReportOptions", "F-Factor"))
        self.cmdOK.setText(_translate("frmReportOptions", "OK"))
        self.cmdCancel.setText(_translate("frmReportOptions", "Cancel"))

