import os
import pydicom
import pandas as pd
import numpy as np


class ProcesadorDICOM:
    """
    Clase para cargar, procesar y extraer metadatos de archivos DICOM.
    """

    def __init__(self):
        # Lista donde se almacenan los objetos DICOM cargados
        self.data = []

    def cargar_archivos(self, ruta_directorio: str):
        """
        Escanea un directorio y carga todos los archivos DICOM válidos.

        Parámetros
        ----------
        ruta_directorio : str
            Ruta del directorio donde se encuentran los archivos DICOM.
        """

        if not os.path.isdir(ruta_directorio):
            raise ValueError(f"La ruta '{ruta_directorio}' no es un directorio válido.")

        archivos = os.listdir(ruta_directorio)

        for file in archivos:
            ruta = os.path.join(ruta_directorio, file)

            # Intentar leer como DICOM
            try:
                dicom_file = pydicom.dcmread(ruta)
                self.data.append(dicom_file)
            except Exception:
                # Ignorar archivos que no son DICOM válidos
                continue

    def extraer_metadatos(self) -> pd.DataFrame:
        """
        Extrae metadatos clave de cada archivo DICOM cargado
        y los organiza en un DataFrame de Pandas.

        Returns
        -------
        pandas.DataFrame
            DataFrame con una fila por archivo DICOM y columnas
            para cada metadato extraído.
        """
        registros = []

        for dicom in self.data:

            def safe_get(tag):
                # Devuelve el atributo si existe, de lo contrario un texto por defecto
                return getattr(dicom, tag, "No disponible")

            fila = {
                "PatientID": safe_get("PatientID"),
                "PatientName": safe_get("PatientName"),
                "StudyInstanceUID": safe_get("StudyInstanceUID"),
                "StudyDescription": safe_get("StudyDescription"),
                "StudyDate": safe_get("StudyDate"),
                "Modality": safe_get("Modality"),
                "Rows": safe_get("Rows"),
                "Columns": safe_get("Columns"),
            }

            # Guardamos temporalmente el array de píxeles para el cálculo posterior
            if hasattr(dicom, "pixel_array"):
                fila["PixelArray"] = dicom.pixel_array
            else:
                fila["PixelArray"] = None

            registros.append(fila)

        df = pd.DataFrame(registros)
        return df

    def calcular_intensidad_promedio(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calcula la intensidad promedio de cada imagen DICOM usando numpy
        y la agrega al DataFrame como una nueva columna 'IntensidadPromedio'.

        Después de calcularla, elimina la columna 'PixelArray' para que
        el DataFrame quede listo para exportarse a CSV sin problemas.

        Parámetros
        ----------
        df : pandas.DataFrame
            DataFrame devuelto por extraer_metadatos(). Debe contener
            la columna 'PixelArray'.

        Returns
        -------
        pandas.DataFrame
            Mismo DataFrame de entrada pero con la columna
            'IntensidadPromedio' añadida y sin la columna 'PixelArray'.
        """

        if "PixelArray" not in df.columns:
            raise ValueError(
                "El DataFrame no contiene la columna 'PixelArray'. "
                "Asegúrate de llamar primero a extraer_metadatos()."
            )

        intensidades = []

        for arr in df["PixelArray"]:
            if arr is None:
                intensidades.append(None)
            else:
                intensidades.append(float(np.mean(arr)))

        # Convertimos a string con coma decimal para que Excel en español lo muestre bien
        serie = pd.Series(intensidades)

        df["IntensidadPromedio"] = (
            serie.round(6)
                 .astype(str)
                 .str.replace(".", ",", regex=False)
        )

        # Eliminamos PixelArray para no romper el CSV ni ocupar memoria innecesaria
        df = df.drop(columns=["PixelArray"])

        return df



