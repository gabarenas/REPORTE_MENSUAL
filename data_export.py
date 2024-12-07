import pandas as pd

# Ruta del archivo CSV filtrado
archivo_csv_filtrado = 'data_filtrada.csv'

try:
    # Leer el archivo CSV filtrado
    data_filtrada = pd.read_csv(archivo_csv_filtrado)
    
    # Exportar a Excel
    archivo_excel = 'data_filtrada.xlsx'
    data_filtrada.to_excel(archivo_excel, index=False)
    
    print(f"Datos exportados exitosamente a {archivo_excel}")
except Exception as e:
    print(f"Error al exportar los datos: {e}")