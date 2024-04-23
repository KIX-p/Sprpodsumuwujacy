# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(537, 739)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 511, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nazwaposilku = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.nazwaposilku.setObjectName("nazwaposilku")
        self.horizontalLayout.addWidget(self.nazwaposilku)
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.liczbakalorii = QtWidgets.QDoubleSpinBox(parent=self.horizontalLayoutWidget)
        self.liczbakalorii.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.liczbakalorii.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.liczbakalorii.setSpecialValueText("")
        self.liczbakalorii.setAccelerated(False)
        self.liczbakalorii.setObjectName("liczbakalorii")
        self.horizontalLayout.addWidget(self.liczbakalorii)
        self.dodaj = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dodaj.setFont(font)
        self.dodaj.setStyleSheet("background: rgb(85, 255, 127)")
        self.dodaj.setObjectName("dodaj")
        self.horizontalLayout.addWidget(self.dodaj)
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 300, 151, 16))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: rgb(0, 255, 0)")
        self.label_3.setObjectName("label_3")
        self.wynik = QtWidgets.QLabel(parent=Dialog)
        self.wynik.setGeometry(QtCore.QRect(330, 300, 55, 16))
        self.wynik.setText("")
        self.wynik.setObjectName("wynik")
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(0, 490, 561, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.malaaktywnosc = QtWidgets.QRadioButton(parent=Dialog)
        self.malaaktywnosc.setGeometry(QtCore.QRect(20, 580, 171, 20))
        self.malaaktywnosc.setCheckable(True)
        self.malaaktywnosc.setChecked(False)
        self.malaaktywnosc.setObjectName("malaaktywnosc")
        self.sredniaaktywnosc = QtWidgets.QRadioButton(parent=Dialog)
        self.sredniaaktywnosc.setGeometry(QtCore.QRect(20, 620, 191, 20))
        self.sredniaaktywnosc.setCheckable(True)
        self.sredniaaktywnosc.setChecked(False)
        self.sredniaaktywnosc.setObjectName("sredniaaktywnosc")
        self.duzaaktywnosc = QtWidgets.QRadioButton(parent=Dialog)
        self.duzaaktywnosc.setGeometry(QtCore.QRect(20, 660, 181, 20))
        self.duzaaktywnosc.setCheckable(True)
        self.duzaaktywnosc.setChecked(False)
        self.duzaaktywnosc.setObjectName("duzaaktywnosc")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 500, 166, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.kobieta = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_2)
        self.kobieta.setChecked(False)
        self.kobieta.setObjectName("kobieta")
        self.horizontalLayout_2.addWidget(self.kobieta)
        self.mezczyzna = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_2)
        self.mezczyzna.setChecked(True)
        self.mezczyzna.setObjectName("mezczyzna")
        self.horizontalLayout_2.addWidget(self.mezczyzna)
        self.listaspozytychkalorii = QtWidgets.QListWidget(parent=Dialog)
        self.listaspozytychkalorii.setEnabled(False)
        self.listaspozytychkalorii.setGeometry(QtCore.QRect(20, 100, 481, 192))
        self.listaspozytychkalorii.setObjectName("listaspozytychkalorii")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "nazwa posiłku"))
        self.label_2.setText(_translate("Dialog", "Liczba kalorii"))
        self.dodaj.setText(_translate("Dialog", "Dodaj"))
        self.label_3.setText(_translate("Dialog", "Suma spożytych kalorii:"))
        self.malaaktywnosc.setText(_translate("Dialog", "Mała aktywność fizyczna"))
        self.sredniaaktywnosc.setText(_translate("Dialog", "Średnia aktywność fizyczna"))
        self.duzaaktywnosc.setText(_translate("Dialog", "Duża aktywność fizyczna"))
        self.kobieta.setText(_translate("Dialog", "Kobieta"))
        self.mezczyzna.setText(_translate("Dialog", "Mężczyzna"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())