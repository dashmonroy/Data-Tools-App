import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel

class CSVtoExcelApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """ Configura la interfaz gráfica de la aplicación. """
        layout = QVBoxLayout()

        self.label = QLabel("Seleccione una carpeta con archivos CSV para convertir a Excel:")
        layout.addWidget(self.label)

        # Botón para convertir CSV a Excel
        self.btn_csv_to_excel = QPushButton("Convertir CSV a Excel")
        self.btn_csv_to_excel.clicked.connect(self.convert_csv_to_excel)
        layout.addWidget(self.btn_csv_to_excel)

        self.setLayout(layout)
        self.setWindowTitle("CSV to Excel Converter")

    def convert_csv_to_excel(self):
        """ Abre un cuadro de diálogo para seleccionar carpetas y convierte archivos CSV a Excel. """
        folder = QFileDialog.getExistingDirectory(self, "Selecciona la carpeta con archivos CSV")
        if folder:
            dest_folder = QFileDialog.getExistingDirectory(self, "Selecciona la carpeta de destino")
            if dest_folder:
                self.csv_a_excel(folder, dest_folder)

    def csv_a_excel(self, carpeta_origen, carpeta_destino):
        """ Convierte todos los archivos CSV en la carpeta origen a archivos Excel en la carpeta destino. """
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        archivos_csv = [archivo for archivo in os.listdir(carpeta_origen) if archivo.endswith('.csv')]

        for archivo in archivos_csv:
            ruta_completa_csv = os.path.join(carpeta_origen, archivo)
            df = pd.read_csv(ruta_completa_csv, delimiter=',')
            ruta_completa_xlsx = os.path.join(carpeta_destino, f"{os.path.splitext(archivo)[0]}.xlsx")
            df.to_excel(ruta_completa_xlsx, index=False)

        self.label.setText("CSV convertidos a Excel exitosamente.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CSVtoExcelApp()
    window.show()
    sys.exit(app.exec())