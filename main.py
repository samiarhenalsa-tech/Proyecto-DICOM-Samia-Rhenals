
import os
from dicom_processor.procesador_dicom import ProcesadorDICOM


def main():
    # Directorio donde se encuentran los archivos DICOM (relativo a este archivo)
    ruta_dicom = os.path.join(os.path.dirname(__file__), "data")

    procesador = ProcesadorDICOM()

    print("📌 Cargando archivos DICOM...")
    procesador.cargar_archivos(ruta_dicom)

    print("📌 Extrayendo metadatos...")
    df = procesador.extraer_metadatos()

    print("📌 Calculando intensidades promedio...")
    df = procesador.calcular_intensidad_promedio(df)

    print("📌 Resultado final:\n")
    print(df)

    # Guardar resultados en un archivo CSV con separador ';'
    df.to_csv("resultado.csv", index=False, sep=";")
    print("📁 Archivo 'resultado.csv' generado con éxito")


if __name__ == "__main__":
    main()
