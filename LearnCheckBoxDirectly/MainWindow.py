# Form implementation generated from reading ui file 'C:\Users\Huy\PycharmProjects\LearnCheckBoxDirectly\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chkShowHide = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.chkShowHide.setGeometry(QtCore.QRect(70, 40, 181, 21))
        self.chkShowHide.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.chkShowHide.setObjectName("chkShowHide")
        self.lblImage = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblImage.setGeometry(QtCore.QRect(70, 100, 231, 201))
        self.lblImage.setText("")
        self.lblImage.setPixmap(QtGui.QPixmap("C:\\Users\\Huy\\PycharmProjects\\LearnCheckBoxDirectly\\24406h.jpg"))
        self.lblImage.setScaledContents(True)
        self.lblImage.setObjectName("lblImage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chkShowHide.setText(_translate("MainWindow", "SHow/Hide Image"))
