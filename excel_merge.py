import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel

class ExcelMergerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """ Configura la interfaz gráfica de la aplicación. """
        layout = QVBoxLayout()

        self.label = QLabel("Seleccione una carpeta con archivos Excel para compilar:")
        layout.addWidget(self.label)

        # Botón para compilar archivos Excel en un solo documento
        self.btn_merge_excel = QPushButton("Compilar Excel en un solo documento")
        self.btn_merge_excel.clicked.connect(self.merge_excel_files)
        layout.addWidget(self.btn_merge_excel)

        self.setLayout(layout)
        self.setWindowTitle("Excel Merger App")

    def merge_excel_files(self):
        """ Abre un cuadro de diálogo para seleccionar carpetas y compila archivos Excel en un solo documento. """
        folder = QFileDialog.getExistingDirectory(self, "Selecciona la carpeta con archivos Excel")
        if folder:
            output_path = QFileDialog.getSaveFileName(self, "Guardar archivo compilado", "", "Excel Files (*.xlsx)")[0]
            if output_path:
                self.compile_excel(folder, output_path)

    def compile_excel(self, carpeta_origen, archivo_salida):
        """ Compila múltiples archivos Excel en un solo archivo, agrupando por columnas y nombres de hojas. """
        dfs = {}
        archivos_excel = [archivo for archivo in os.listdir(carpeta_origen) if archivo.endswith('.xlsx')]

        for archivo in archivos_excel:
            ruta_completa = os.path.join(carpeta_origen, archivo)
            xls = pd.read_excel(ruta_completa, sheet_name=None)  # Leer todas las hojas
            for hoja, df in xls.items():
                df['Archivo'] = archivo  # Agregar el nombre del archivo como referencia
                if hoja in dfs:
                    dfs[hoja].append(df)
                else:
                    dfs[hoja] = [df]

        # Guardar en un solo archivo Excel con hojas separadas
        with pd.ExcelWriter(archivo_salida) as writer:
            for hoja, df_list in dfs.items():
                combinado_df = pd.concat(df_list, ignore_index=True)
                combinado_df.to_excel(writer, sheet_name=hoja, index=False)
        
        self.label.setText("Archivos Excel compilados exitosamente.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExcelMergerApp()
    window.show()
    sys.exit(app.exec())
