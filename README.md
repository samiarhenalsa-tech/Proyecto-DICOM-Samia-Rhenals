# Proyecto de Procesamiento DICOM en Python

## Integrantes
- Samia Selena Rhenals Arrieta


## 1. Descripción del proyecto
Este proyecto implementa un procesador de archivos DICOM utilizando Python, simulando el
comportamiento básico de un sistema PACS.
El programa:
- Carga automáticamente todos los archivos DICOM de un directorio.
- Extrae metadatos fundamentales definidos por el estándar DICOM.
- Estructura esta información en un DataFrame de Pandas.
- Calcula la intensidad promedio de la imagen asociada a cada archivo.
- Genera un archivo CSV con los resultados.

Este proyecto aplica conceptos centrales de informática médica, estandarización y bioingeniería.


## 2. ¿Por qué DICOM y HL7 son cruciales para la interoperabilidad en salud?

### DICOM
Es el estándar internacional para imágenes médicas.
Define cómo se almacenan, transmiten y estructuran tanto las imágenes como sus metadatos.
Permite que equipos de diferentes fabricantes (CT, RM, ecógrafos…) puedan comunicarse sin
incompatibilidades.

### HL7
Es el estándar para mensajería clínica, encargado de transmitir:
- datos administrativos,
- órdenes médicas,
- resultados de laboratorio,
- información demográfica del paciente, etc.

### Diferencia conceptual

| DICOM | HL7 |
|-------|-----|
| Maneja imágenes médicas y sus metadatos | Maneja información administrativa/clínica |
| Es binario + metadata | Es texto estructurado |
| Opera en PACS | Opera en HIS, EMR |

Ambos juntos permiten que toda la información de un paciente fluya sin barreras entre sistemas
heterogéneos.


## 3. Relevancia del análisis de la distribución de intensidades en una imagen médica

- Permite identificar ruido, artefactos o errores de adquisición.
- Ayuda a detectar si la imagen requiere normalización, ecualización o ajuste de contraste.
- En imágenes CT, los valores de intensidad (unidades Hounsfield) aportan información sobre el tipo de tejido.
- En segmentación y deep learning, la distribución de intensidades es clave para estandarizar datos,
  detectar valores atípicos y mejorar la estabilidad de los algoritmos.

En resumen, es esencial tanto para un análisis clínico confiable como para un preprocesamiento correcto.



## 4. Dificultades encontradas y relevancia de Python para el análisis de datos médicos

### Dificultades
- Algunos archivos DICOM pueden tener campos vacíos debido al anonimizado.
- Variaciones en los tags según fabricante y modalidad de estudio.
- Diferencias en tamaño, resolución y profundidad de bits entre imágenes.
- Necesidad de manejar errores cuando un archivo no es un DICOM válido.

### Importancia de Python
Python es fundamental en bioingeniería debido a:
- Librerías especializadas como `pydicom`, `numpy`, `pandas` y `scikit-image`.
- Procesamiento eficiente y flexible de datos tabulares con `pandas`.
- Integración directa con frameworks de IA como PyTorch o TensorFlow.
- Código claro, reproducible y con una comunidad muy activa.

Python se ha convertido en uno de los pilares del desarrollo en informática médica y análisis de imágenes.



## Instrucciones de uso

1. Crear y activar un entorno virtual de Python.
2. Instalar las dependencias con:

   ```bash
   pip install -r requirements.txt
   ```

3. Colocar los archivos DICOM de prueba dentro de la carpeta `data/`. (utilice preferiblemente los que ya estn ahí)
4. Ejecutar el script principal:

   ```bash
   python main.py
   ```

5. Revisar el archivo `resultado.csv` generado en el directorio raíz del proyecto.


