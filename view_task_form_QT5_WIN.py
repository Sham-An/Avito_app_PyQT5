# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PycharmProjects\Avito_app_PyQT5\app_View_task_GPT_WINVER.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TaskEDIT(object):
    def setupUi(self, TaskEDIT):
        TaskEDIT.setObjectName("TaskEDIT")
        TaskEDIT.resize(962, 785)
        self.centralwidget = QtWidgets.QWidget(TaskEDIT)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.Get_Task = QtWidgets.QPushButton(self.centralwidget)
        self.Get_Task.setObjectName("Get_Task")
        self.gridLayout_4.addWidget(self.Get_Task, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(268, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 3)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.parse = QtWidgets.QWidget()
        self.parse.setObjectName("parse")
        self.groupBox = QtWidgets.QGroupBox(self.parse)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 761, 101))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Copy = QtWidgets.QPushButton(self.groupBox)
        self.Copy.setObjectName("Copy")
        self.verticalLayout_3.addWidget(self.Copy)
        self.tabWidget.addTab(self.parse, "")
        self.view = QtWidgets.QWidget()
        self.view.setObjectName("view")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.view)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Task_view_text = QtWidgets.QTextEdit(self.view)
        self.Task_view_text.setObjectName("Task_view_text")
        self.gridLayout_3.addWidget(self.Task_view_text, 0, 0, 1, 1)
        self.Get_slug_Id = QtWidgets.QPushButton(self.view)
        self.Get_slug_Id.setObjectName("Get_slug_Id")
        self.gridLayout_3.addWidget(self.Get_slug_Id, 1, 0, 1, 1)
        self.tabWidget.addTab(self.view, "")
        self.gridLayout_5.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.Path_scheme = QtWidgets.QLineEdit(self.centralwidget)
        self.Path_scheme.setObjectName("Path_scheme")
        self.gridLayout.addWidget(self.Path_scheme, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.Path_host = QtWidgets.QLineEdit(self.centralwidget)
        self.Path_host.setMaximumSize(QtCore.QSize(559, 22))
        self.Path_host.setMaxLength(200)
        self.Path_host.setCursorPosition(0)
        self.Path_host.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Path_host.setDragEnabled(True)
        self.Path_host.setReadOnly(True)
        self.Path_host.setObjectName("Path_host")
        self.gridLayout.addWidget(self.Path_host, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        self.Path_parts = QtWidgets.QLineEdit(self.centralwidget)
        self.Path_parts.setEnabled(True)
        self.Path_parts.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Path_parts.setText("")
        self.Path_parts.setMaxLength(2000)
        self.Path_parts.setFrame(True)
        self.Path_parts.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Path_parts.setCursorPosition(0)
        self.Path_parts.setDragEnabled(True)
        self.Path_parts.setReadOnly(True)
        self.Path_parts.setObjectName("Path_parts")
        self.gridLayout.addWidget(self.Path_parts, 0, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.Path_local = QtWidgets.QLineEdit(self.centralwidget)
        self.Path_local.setObjectName("Path_local")
        self.gridLayout.addWidget(self.Path_local, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1)
        self.list_Query = QtWidgets.QListWidget(self.centralwidget)
        self.list_Query.setObjectName("list_Query")
        self.gridLayout.addWidget(self.list_Query, 1, 5, 3, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.Path_cat1 = QtWidgets.QLineEdit(self.centralwidget)
        self.Path_cat1.setObjectName("Path_cat1")
        self.gridLayout.addWidget(self.Path_cat1, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.Path_cat2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Path_cat2.setObjectName("Path_cat2")
        self.gridLayout.addWidget(self.Path_cat2, 3, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.View_Task = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.View_Task.setFont(font)
        self.View_Task.setObjectName("View_Task")
        self.gridLayout_2.addWidget(self.View_Task, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        TaskEDIT.setCentralWidget(self.centralwidget)

        self.retranslateUi(TaskEDIT)
        self.tabWidget.setCurrentIndex(1)
        self.Get_slug_Id.clicked.connect(self.Task_view_text.update) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(TaskEDIT)

    def retranslateUi(self, TaskEDIT):
        _translate = QtCore.QCoreApplication.translate
        TaskEDIT.setWindowTitle(_translate("TaskEDIT", "Task Edit"))
        self.label.setText(_translate("TaskEDIT", "Enter a URL:"))
        self.Get_Task.setText(_translate("TaskEDIT", "Get Task"))
        self.groupBox.setTitle(_translate("TaskEDIT", "URL Components"))
        self.Copy.setText(_translate("TaskEDIT", "Copy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parse), _translate("TaskEDIT", "Path_parse"))
        self.Get_slug_Id.setText(_translate("TaskEDIT", "Get from headers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.view), _translate("TaskEDIT", "Task_view"))
        self.label_2.setText(_translate("TaskEDIT", "Scheme:"))
        self.label_3.setText(_translate("TaskEDIT", "Host:"))
        self.label_4.setText(_translate("TaskEDIT", "Parts:"))
        self.label_9.setText(_translate("TaskEDIT", "Parts local:"))
        self.label_5.setText(_translate("TaskEDIT", "Param:"))
        self.label_10.setText(_translate("TaskEDIT", "Parts cat1:"))
        self.label_11.setText(_translate("TaskEDIT", "Parts cat2:"))
        self.label_6.setText(_translate("TaskEDIT", "Task:"))
