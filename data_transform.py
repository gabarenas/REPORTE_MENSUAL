import pandas as pd

# Ruta del archivo CSV intermedio
archivo_csv = 'reporteset.csv'

try:
    # Leer el archivo CSV
    data = pd.read_csv(archivo_csv)
    
    # Filtrar la columna 'Motivo' para mostrar solo los datos de 'despacho'
    despachos = data[data['Motivo'] == 'DESPACHO']
    # Filtrar los despachos con número de serie vacío o nulo
    despachos_filtrados = despachos[despachos['Número de serie'].notna() & (despachos['Número de serie'] != '')]

    # Exportar a Excel
    archivo_excel = 'data_filtrada.xlsx'
    despachos_filtrados.to_excel(archivo_excel, index=False)
    
    print(f"Datos exportados exitosamente a {archivo_excel}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")