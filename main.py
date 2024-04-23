import sys
from PyQt6.QtWidgets import QDialog, QApplication
from PyQt6.uic.properties import QtCore

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Kalkulator kalorii")
        self.ui.dodaj.clicked.connect(self.dodaj_kalorii)
        self.show()

    def dodaj_kalorii(self):
        nazwa_posilku = self.ui.nazwaposilku.text()
        kalorie = self.ui.liczbakalorii.text()
        suma = 0
        self.ui.listaspozytychkalorii.addItem(nazwa_posilku + ' ' + kalorie)
        for i in range (self.ui.listaspozytychkalorii.count()):
            suma = float(kalorie)+suma
        self.ui.wynik.setText(str(suma))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec())