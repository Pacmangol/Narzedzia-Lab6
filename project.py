import sys
import argparse
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QMessageBox

def parse_arguments():
    parser = argparse.ArgumentParser(description='Konwersja plików.')
    parser.add_argument('source', help='Ścieżka do pliku źródłowego')
    parser.add_argument('destination', help='Ścieżka do pliku docelowego')
    return parser.parse_args()

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print("JSON data:", data)
            return data
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return None
    except FileNotFoundError:
        print("File not found.")
        return None

def save_json(data, file_path):
    if data is None:
        print("No data to save.")
        return
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Failed to save data: {e}")

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'File Converter'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        layout = QVBoxLayout()

        self.label = QLabel('Wybierz plik źródłowy i docelowy')
        layout.addWidget(self.label)

        self.sourceButton = QPushButton('Wybierz plik źródłowy', self)
        self.sourceButton.clicked.connect(self.openSourceFileNameDialog)
        layout.addWidget(self.sourceButton)

        self.destinationButton = QPushButton('Wybierz plik docelowy', self)
        self.destinationButton.clicked.connect(self.openDestinationFileNameDialog)
        layout.addWidget(self.destinationButton)

        self.convertButton = QPushButton('Konwertuj', self)
        self.convertButton.clicked.connect(self.convertFiles)
        layout.addWidget(self.convertButton)

        self.setLayout(layout)
        self.show()

    def openSourceFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "Wybierz plik źródłowy", "", "JSON Files (*.json);;All Files (*)", options=options)
        if fileName:
            self.sourceFileName = fileName
            self.label.setText(f"Źródło: {fileName}")

    def openDestinationFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getSaveFileName(self, "Wybierz plik docelowy", "", "JSON Files (*.json);;All Files (*)", options=options)
        if fileName:
            self.destinationFileName = fileName
            self.label.setText(f"Cel: {fileName}")

    def convertFiles(self):
        try:
            data = load_json(self.sourceFileName)
            save_json(data, self.destinationFileName)
            QMessageBox.information(self, 'Sukces', 'Plik został przekonwertowany.')
        except Exception as e:
            QMessageBox.critical(self, 'Błąd', str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

