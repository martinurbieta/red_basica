# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.calcTab = QtWidgets.QWidget()
        self.calcTab.setObjectName("calcTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.calcTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calcTable = QtWidgets.QTableView(self.calcTab)
        self.calcTable.setObjectName("calcTable")
        self.horizontalLayout.addWidget(self.calcTable)
        self.tabWidget.addTab(self.calcTab, "")
        self.contribTab = QtWidgets.QWidget()
        self.contribTab.setObjectName("contribTab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.contribTab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.contribTable = QtWidgets.QTableView(self.contribTab)
        self.contribTable.setObjectName("contribTable")
        self.horizontalLayout_2.addWidget(self.contribTable)
        self.tabWidget.addTab(self.contribTab, "")
        self.wlaTab = QtWidgets.QWidget()
        self.wlaTab.setObjectName("wlaTab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.wlaTab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.wlaTable = QtWidgets.QTableView(self.wlaTab)
        self.wlaTable.setObjectName("wlaTable")
        self.horizontalLayout_3.addWidget(self.wlaTable)
        self.tabWidget.addTab(self.wlaTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 25))
        self.menubar.setObjectName("menubar")
        self.menuParametros = QtWidgets.QMenu(self.menubar)
        self.menuParametros.setObjectName("menuParametros")
        self.menuFunciones = QtWidgets.QMenu(self.menubar)
        self.menuFunciones.setObjectName("menuFunciones")
        self.menuExportaci_n = QtWidgets.QMenu(self.menubar)
        self.menuExportaci_n.setObjectName("menuExportaci_n")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionProject = QtWidgets.QAction(MainWindow)
        self.actionProject.setObjectName("actionProject")
        self.actionParameters = QtWidgets.QAction(MainWindow)
        self.actionParameters.setObjectName("actionParameters")
        self.actionPipes = QtWidgets.QAction(MainWindow)
        self.actionPipes.setObjectName("actionPipes")
        self.actionInspectionDevices = QtWidgets.QAction(MainWindow)
        self.actionInspectionDevices.setObjectName("actionInspectionDevices")
        self.actionMin_Excav = QtWidgets.QAction(MainWindow)
        self.actionMin_Excav.setObjectName("actionMin_Excav")
        self.actionMin_Desnivel = QtWidgets.QAction(MainWindow)
        self.actionMin_Desnivel.setObjectName("actionMin_Desnivel")
        self.actionAjuste_NA = QtWidgets.QAction(MainWindow)
        self.actionAjuste_NA.setObjectName("actionAjuste_NA")
        self.actionCalcular_DN_Creciente = QtWidgets.QAction(MainWindow)
        self.actionCalcular_DN_Creciente.setObjectName("actionCalcular_DN_Creciente")
        self.actionCalculara_DN = QtWidgets.QAction(MainWindow)
        self.actionCalculara_DN.setObjectName("actionCalculara_DN")
        self.actionCrear_Capa_QGIS = QtWidgets.QAction(MainWindow)
        self.actionCrear_Capa_QGIS.setObjectName("actionCrear_Capa_QGIS")
        self.actionGenerar_Hoja_Impresi_n = QtWidgets.QAction(MainWindow)
        self.actionGenerar_Hoja_Impresi_n.setObjectName("actionGenerar_Hoja_Impresi_n")
        self.menuParametros.addAction(self.actionProject)
        self.menuParametros.addAction(self.actionParameters)
        self.menuFunciones.addAction(self.actionMin_Excav)
        self.menuFunciones.addAction(self.actionMin_Desnivel)
        self.menuFunciones.addAction(self.actionAjuste_NA)
        self.menuFunciones.addAction(self.actionCalcular_DN_Creciente)
        self.menuFunciones.addAction(self.actionCalculara_DN)
        self.menuExportaci_n.addAction(self.actionCrear_Capa_QGIS)
        self.menuExportaci_n.addAction(self.actionGenerar_Hoja_Impresi_n)
        self.menubar.addAction(self.menuParametros.menuAction())
        self.menubar.addAction(self.menuFunciones.menuAction())
        self.menubar.addAction(self.menuExportaci_n.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SANIBIDapp"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.calcTab), _translate("MainWindow", "Red básica"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.contribTab), _translate("MainWindow", "Contribuciones"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wlaTab), _translate("MainWindow", "Nivel de agua"))
        self.menuParametros.setTitle(_translate("MainWindow", "Configuración"))
        self.menuFunciones.setTitle(_translate("MainWindow", "Funciones"))
        self.menuExportaci_n.setTitle(_translate("MainWindow", "Exportación"))
        self.actionProject.setText(_translate("MainWindow", "Proyecto"))
        self.actionParameters.setText(_translate("MainWindow", "Parámetros"))
        self.actionPipes.setText(_translate("MainWindow", "Tubos"))
        self.actionInspectionDevices.setText(_translate("MainWindow", "Dispositivos de Inspección"))
        self.actionMin_Excav.setText(_translate("MainWindow", "Min. Excav."))
        self.actionMin_Desnivel.setText(_translate("MainWindow", "Min. Desnivel"))
        self.actionAjuste_NA.setText(_translate("MainWindow", "Ajuste NA"))
        self.actionCalcular_DN_Creciente.setText(_translate("MainWindow", "Calcular DN Creciente"))
        self.actionCalculara_DN.setText(_translate("MainWindow", "Calculara DN"))
        self.actionCrear_Capa_QGIS.setText(_translate("MainWindow", "Crear Capa QGIS"))
        self.actionGenerar_Hoja_Impresi_n.setText(_translate("MainWindow", "Generar Hoja Impresión"))

