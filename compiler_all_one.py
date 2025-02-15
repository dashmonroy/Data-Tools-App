import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel

class ExcelMergerSingleSheetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """ Configura la interfaz gráfica de la aplicación. """
        layout = QVBoxLayout()

        self.label = QLabel("Seleccione una carpeta con archivos Excel para compilar en una sola hoja:")
        layout.addWidget(self.label)

        # Botón para compilar archivos Excel en una sola hoja
        self.btn_merge_excel = QPushButton("Compilar Excel en una sola hoja")
        self.btn_merge_excel.clicked.connect(self.merge_excel_files)
        layout.addWidget(self.btn_merge_excel)

        self.setLayout(layout)
        self.setWindowTitle("Excel Single Sheet Merger App")

    def merge_excel_files(self):
        """ Abre un cuadro de diálogo para seleccionar carpetas y compila archivos Excel en una sola hoja. """
        folder = QFileDialog.getExistingDirectory(self, "Selecciona la carpeta con archivos Excel")
        if folder:
            output_path = QFileDialog.getSaveFileName(self, "Guardar archivo compilado", "", "Excel Files (*.xlsx)")[0]
            if output_path:
                self.compile_excel(folder, output_path)

    def compile_excel(self, carpeta_origen, archivo_salida):
        """ Compila múltiples archivos Excel en un solo archivo con una única hoja, añadiendo el nombre del archivo como columna. """
        combined_df = pd.DataFrame()
        archivos_excel = [archivo for archivo in os.listdir(carpeta_origen) if archivo.endswith('.xlsx')]

        for archivo in archivos_excel:
            ruta_completa = os.path.join(carpeta_origen, archivo)
            xls = pd.read_excel(ruta_completa, sheet_name=None)  # Leer todas las hojas
            for _, df in xls.items():
                df.insert(0, 'Archivo_Origen', archivo)  # Agregar el nombre del archivo en la primera columna
                combined_df = pd.concat([combined_df, df], ignore_index=True)

        # Guardar en un solo archivo Excel con una única hoja
        if not combined_df.empty:
            combined_df.to_excel(archivo_salida, sheet_name="Compilado", index=False)
            self.label.setText("Archivos Excel compilados exitosamente en una sola hoja.")
        else:
            self.label.setText("No se encontraron datos para compilar.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExcelMergerSingleSheetApp()
    window.show()
    sys.exit(app.exec())
