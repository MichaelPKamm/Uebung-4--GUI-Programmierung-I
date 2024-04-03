#Uebung 4

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.createLayout()
        self.createConnects()

    def createLayout(self):
        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

        # Layout erstellen:
        layout = QFormLayout()

        # Widget-Instanzen erstellen:

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        
        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)


        self.vornameLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        self.geburtstagLineEdit = QDateEdit()
        self.geburtstagLineEdit.setDisplayFormat("dd/mm/yyyy")
        self.adresseLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.countries = QComboBox()
        self.countries.addItems(["Schweiz", "Deutschland", "Österreich"])

        
        self.button = QPushButton("Save")
        

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Name:", self.nameLineEdit)
        layout.addRow("Geburtstag:", self.geburtstagLineEdit)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("Postleitzahl:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:" , self.countries)
        
        layout.addRow(self.button)

        filemenu.addAction("save", self.speichern)
        filemenu.addSeparator()
        filemenu.addAction("quit", self.ende)

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

    def createConnects(self):
        
        self.button.clicked.connect(self.speichern)

    def speichern(self):
        file = open("output.txt", "w")
        daten = [self.vornameLineEdit.text(), 
                 self.nameLineEdit.text(), 
                 self.geburtstagLineEdit.text(), 
                 self.adresseLineEdit.text(), 
                 self.plzLineEdit.text(), 
                 self.ortLineEdit.text(), 
                 self.countries.currentText()
                 ]
        daten_2= ", ".join(str(i) for i in daten)
        file.write (daten_2)
        file.close()
        QMessageBox.information(self, "Speichern", "Daten wurden erfolgreich gespeichert!", QMessageBox.Ok)
        
        
    def ende(self):
        sys.exit()
        #self.close() geht auch  
        






def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()