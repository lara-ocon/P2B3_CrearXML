# Práctica 2 Bloque 3 - Adquisición de datos - IMAT
# Informe de datos XML
# Autor: Lara Ocón Madrid

# Importamos las librerías necesarias
import pandas as pd
import xml.etree.ElementTree as ET

def extract():
    # cargamos los dataframes
    df_pizzas = pd.read_csv('ficheros/pizzas.csv')
    df_pizza_types = pd.read_csv('ficheros/pizza_types.csv')
    df_data_dictionary = pd.read_csv('ficheros/data_dictionary.csv')
    df_order_details_2015 = pd.read_csv('ficheros/order_details_2015.csv')
    df_order_details_2016 = pd.read_csv('ficheros/order_details_2016.csv', delimiter=';')
    df_orders_2015 = pd.read_csv('ficheros/orders_2015.csv')
    df_orders_2016 = pd.read_csv('ficheros/orders_2016.csv', delimiter=';')

    return [df_pizzas, df_pizza_types, df_data_dictionary, df_order_details_2015, df_order_details_2016, df_orders_2015, df_orders_2016]


if __name__ == "__main__":

    # Estos son los nombres de los csv que vamos a leer
    nombres_csv = ['pizzas', 'pizza_types', 'data_dictionary', 'order_details_2015', 'order_details_2016', 'orders_2015', 'orders_2016']

    dfs = extract()

    # inicializamos el árbol
    root = ET.Element('root')
    arbol = ET.ElementTree(root)
    datos = {}

    # recorremos los dataframes y los añadimos al arbol
    i = 0
    for nombre in nombres_csv:
        datos[nombre] = ET.SubElement(root, "csv")
        # mostramos el nombre del csv
        ET.SubElement(datos[nombre], "nombre").text = nombre
        # mostramos el tamaño del dataframe
        ET.SubElement(datos[nombre], 'size').text = str(dfs[i].shape)
        # contamos el numero de nans por columnas
        columnas = {}
        for columna in dfs[i].columns:
            columnas[columna] = ET.SubElement(datos[nombre], "columna")
            nans = dfs[i][columna].isna().sum()
            tipo = dfs[i][columna].dtype
            ET.SubElement(columnas[columna], "nombre").text = columna
            ET.SubElement(columnas[columna], 'nans').text = str(nans)
            ET.SubElement(columnas[columna], 'tipo').text = str(tipo)
        

        i += 1

    # guardamos el árbol en un fichero xml
    arbol.write('reporte_tipologia_datos2.xml')