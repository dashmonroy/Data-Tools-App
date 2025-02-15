# 🚀 Data Tools App

**Autor**: Ricardo Monroy Palacios  
**Repositorio**: [dashmonroy/Data-Tools-App](https://github.com/dashmonroy/Data-Tools-App)

Data Tools App es una herramienta interactiva que facilita la manipulación de archivos **CSV y Excel** de forma rápida y eficiente mediante una **interfaz gráfica**.  
Es ideal para **analistas de datos**, **ingenieros** y **profesionales** que trabajan con grandes volúmenes de información.

---

## 🛠 **Características Principales**

### 🔹 1. **Convertir CSV a Excel**

- Transforma archivos `.csv` en `.xlsx` de forma automática.
- Detecta automáticamente el delimitador (`,`, `;`, `tab`).
- Permite seleccionar la carpeta de archivos CSV y la carpeta de destino.

### 🔹 2. **Compilar archivos Excel en múltiples hojas**

- Combina varios archivos `.xlsx` en un solo libro.
- Mantiene el nombre de cada hoja original.
- Agrega una columna con el **nombre del archivo de origen**.

### 🔹 3. **Compilar archivos Excel en una sola hoja**

- Fusiona todos los datos en **una sola hoja**.
- Agrega el **nombre del archivo original** como referencia.
- Ideal para consolidar información dispersa en múltiples archivos.

### 🔹 4. **Super App**

- Interfaz gráfica **intuitiva** para seleccionar fácilmente cualquier función.
- **Automatiza** todo el proceso con solo unos clics.
- **Optimiza** el tiempo al trabajar con archivos de gran volumen.

---

## 📂 **Estructura del Proyecto**

```
📂 DataToolsExcel
 ├── 📄 compiler_all_one.py  # Compila Excel en una sola hoja
 ├── 📄 cvs_excel.py         # Convierte CSV a Excel
 ├── 📄 excel_merge.py       # Compila Excel en múltiples hojas
 ├── 📄 super_app.py         # Super App con todas las funciones
 ├── 📄 requirements.txt     # Dependencias del proyecto
 ├── 📄 LICENSE              # Licencia MIT
 ├── 📄 README.md            # Documentación del proyecto
```

---

## 💻 **Instalación y Uso**

### **1️⃣ Clonar el repositorio**

Abre tu terminal y ejecuta:

```bash
git clone https://github.com/dashmonroy/Data-Tools-App.git
cd Data-Tools-App
```

### **2️⃣ Crear un entorno virtual (opcional, recomendado)**

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Instalar dependencias**

```bash
pip install -r requirements.txt
```

### **4️⃣ Ejecutar la Super App**

```bash
python super_app.py
```

🔹 Se abrirá la **interfaz gráfica** con las opciones para seleccionar la funcionalidad deseada.

---

## 🛠 **Tecnologías Usadas**

- **Python** 🐍 - Lenguaje principal.
- **PyQt6** 🖥 - Creación de la interfaz gráfica.
- **Pandas** 📊 - Procesamiento y manipulación de datos.
- **OpenPyXL** 📄 - Manejo de archivos Excel.

---

## 📌 **Mejoras Futuras**

✅ **Agregar barra de progreso** para procesos largos.  
✅ Soporte para más formatos de entrada/salida (`CSV`, `JSON`, `TXT`).  
✅ **Exportación a PDF** para reportes.  
✅ **Automatización con programación de tareas** en Windows/Linux.

---

## 📝 **Licencia**

Este proyecto está bajo la **Licencia MIT**.  
Puedes usarlo, modificarlo y distribuirlo libremente.

---

## ⭐ **¡Contribuye y Apoya el Proyecto!**

Si esta herramienta te resultó útil, **dale un ⭐ en GitHub** y compártela con otros.  
¡Cualquier sugerencia o contribución es bienvenida! 🚀
