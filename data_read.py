import pandas as pd

# Ruta del archivo excel
archivo_excel = 'Transferencias por fecha setiembre.xlsx' 

try:
    # Leer el archivo Excel
    data = pd.read_excel(archivo_excel)
    
    # Guardar los datos en un archivo CSV temporal
    archivo_csv = 'reporteset.csv'
    data.to_csv(archivo_csv, index=False)
    
    print(f"Datos leídos y guardados en {archivo_csv}")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
