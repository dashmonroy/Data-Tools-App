import sys
import os
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel

class DataToolsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """ Configura la interfaz gráfica de la aplicación con las tres funciones. """
        layout = QVBoxLayout()

        self.label = QLabel("Seleccione una función a ejecutar:")
        layout.addWidget(self.label)

        # Botón para convertir CSV a Excel
        self.btn_csv_to_excel = QPushButton("Convertir CSV a Excel")
        self.btn_csv_to_excel.clicked.connect(self.convert_csv_to_excel)
        layout.addWidget(self.btn_csv_to_excel)

        # Botón para compilar archivos Excel en múltiples hojas
        self.btn_merge_excel_sheets = QPushButton("Compilar Excel en múltiples hojas")
        self.btn_merge_excel_sheets.clicked.connect(self.merge_excel_files_sheets)
        layout.addWidget(self.btn_merge_excel_sheets)

        # Botón para compilar archivos Excel en una sola hoja
        self.btn_merge_excel_one_sheet = QPushButton("Compilar Excel en una sola hoja")
        self.btn_merge_excel_one_sheet.clicked.connect(self.merge_excel_one_sheet)
        layout.addWidget(self.btn_merge_excel_one_sheet)

        self.setLayout(layout)
        self.setWindowTitle("Data Tools App")

    def convert_csv_to_excel(self):
        """ Convierte archivos CSV a Excel. """
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

    def merge_excel_files_sheets(self):
        """ Compila múltiples archivos Excel en un solo documento con múltiples hojas. """
        folder = QFileDialog.getExistingDirectory(self, "Selecciona la carpeta con archivos Excel")
        if folder:
            output_path = QFileDialog.getSaveFileName(self, "Guardar archivo compilado", "", "Excel Files (*.xlsx)")[0]
            if output_path:
                self.compile_excel_sheets(folder, output_path)

    def compile_excel_sheets(self, carpeta_origen, archivo_salida):
        """ Compila múltiples archivos Excel en un solo archivo con múltiples hojas. """
        dfs = {}
        archivos_excel = [archivo for archivo in os.listdir(carpeta_origen) if archivo.endswith('.xlsx')]

        for archivo in archivos_excel:
            ruta_completa = os.path.join(carpeta_origen, archivo)
            xls = pd.read_excel(ruta_completa, sheet_name=None)
            for hoja, df in xls.items():
                df.insert(0, 'Archivo_Origen', archivo)
                if hoja in dfs:
                    dfs[hoja].append(df)
                else:
                    dfs[hoja] = [df]

        with pd.ExcelWriter(archivo_salida) as writer:
            for hoja, df_list in dfs.items():
                combinado_df = pd.concat(df_list, ignore_index=True)
                combinado_df.to_excel(writer, sheet_name=hoja, index=False)
        
        self.label.setText("Archivos Excel compilados exitosamente en múltiples hojas.")

    def merge_excel_one_sheet(self):
        """ Compila múltiples archivos Excel en una sola hoja. """
        folder = QFileDialog.getExistingDirectory(self, "Selecciona la carpeta con archivos Excel")
        if folder:
            output_path = QFileDialog.getSaveFileName(self, "Guardar archivo compilado", "", "Excel Files (*.xlsx)")[0]
            if output_path:
                self.compile_excel_one_sheet(folder, output_path)

    def compile_excel_one_sheet(self, carpeta_origen, archivo_salida):
        """ Compila múltiples archivos Excel en un solo archivo con una única hoja. """
        combined_df = pd.DataFrame()
        archivos_excel = [archivo for archivo in os.listdir(carpeta_origen) if archivo.endswith('.xlsx')]

        for archivo in archivos_excel:
            ruta_completa = os.path.join(carpeta_origen, archivo)
            xls = pd.read_excel(ruta_completa, sheet_name=None)
            for _, df in xls.items():
                df.insert(0, 'Archivo_Origen', archivo)
                combined_df = pd.concat([combined_df, df], ignore_index=True)

        if not combined_df.empty:
            combined_df.to_excel(archivo_salida, sheet_name="Compilado", index=False)
            self.label.setText("Archivos Excel compilados exitosamente en una sola hoja.")
        else:
            self.label.setText("No se encontraron datos para compilar.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataToolsApp()
    window.show()
    sys.exit(app.exec())
