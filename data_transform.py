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
    
     # Asegurarse de que la columna 'Número de artículo' exista
    if 'Número de artículo' not in despachos_filtrados.columns:
        raise KeyError("La columna 'Número de artículo' no se encontró en el archivo.")
    
    # Crear la nueva columna 'prefijo'
    despachos_filtrados['prefijo'] = despachos_filtrados['Número de artículo'].astype(str).str[:3]
    
    # Crear la nueva columna 'Tipo de servicio'
    despachos_filtrados['Tipo de servicio'] = ''

    # Definir las condiciones para agrupar los servicios
    despachos_filtrados.loc[despachos_filtrados['Servicio'].isin(['BASICO ENTEL', 'BASICO SMART']), 'Tipo de servicio'] = 'BASICO'
    despachos_filtrados.loc[despachos_filtrados['Servicio'].isin(['FLOTA CLARO', 'FLOTA ENTEL GLOBAL']), 'Tipo de servicio'] = 'FLOTA'

    archivo_excel = 'data_filtrada.xlsx'
    despachos_filtrados.to_excel(archivo_excel, index=False)
    
    print(f"Datos exportados exitosamente a {archivo_excel}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")