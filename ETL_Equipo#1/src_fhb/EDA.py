#%%
# -----LIBRERIAS------

# Tratamiento de datos
import pandas as pd
import numpy as np
import re

# Imputación de the_null usando métodos avanzados estadísticos
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

# Gestión de los warnings
import warnings
warnings.filterwarnings("ignore")

# Configuración
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

#%%

# LEER ARCHIVOS
def leer_csv(ruta_archivo):
    try:
        df = pd.read_csv(ruta_archivo, index_col=0)
        return df
    except:
        print(f"El archivo '{ruta_archivo}' no se encontró.")
#%%

# EXPLORAR LOS DATAFRAME EN GENERAL 
def exploracion_df(df):
    
    print(' Filas y Columnas del DATAFRAME \n')
    print(f"El número de filas que tenemos es de {df.shape[0]}.\nEl número de columnas es de {df.shape[1]}\n")
    print('____________________________________________________________\n')
    
    print(' Nombre de todas las Columnas del DATAFRAME: \n')
    print(df.columns)
    print('____________________________________________________________\n')
    
    print('INFORMACIÓN GENERAL DEL DATAFRAME \n')
    print(df.info())
    print('____________________________________________________________\n')
    
    print('Ver los NULOS del DataFrame \n')
    print(f'Los nulos: --> {df.isnull().sum().mean() * 100} \n')
    for columna in df.columns:
        cantidad_valores_the_null = df[columna].isnull().mean() * 100
        print(f'La columna {columna}: {cantidad_valores_the_null}')
    print('____________________________________________________________\n')
    
    print('Valores ÚNICOS por columna:\n')
    for columna in df.columns:
        cantidad_valores_unicos = df[columna].unique()
        print(f'La columna {columna}: {len(cantidad_valores_unicos)}')
        print(f'La columna {columna}: {cantidad_valores_unicos}')
        
    print('____________________________________________________________\n')
    
    print('Valores DUPLICADOS por columna es de:\n')
    for columna in df.columns:
        cantidad_duplicados = df[columna].duplicated().sum()
        print(f'La columna {columna}: {cantidad_duplicados}')
    print('____________________________________________________________\n')
  
    print('--> RESUMEN ESTADÍSTICO \n')
    
    try:
        numeric_summary = df.describe().select_dtypes(include=['number']).T
        if not numeric_summary.empty:
            print('<<< Variables Numéricas >>> \n')
            print(f'{numeric_summary} \n')     
    except:
        print('No hay variables numéricas en el DataFrame.')
    
    try:
        categorical_summary = df.describe(include='object').T
        if not categorical_summary.empty:
            print('<<< Variables Categóricas >>> \n')
            print(f'{categorical_summary} \n')     
    except:
        print('No hay variables categóricas en el DataFrame.')
# %%
# LIMPIEZA Y TRANSFORMACIÓN DEL DATASET

def limpiar_datos(df):
    # Definir las columnas categóricas y las columnas a eliminar
    columnas_categoricas = ['country', 'arrival_date_year']
    # Reemplazar valores nulos por la moda en columnas categóricas
    def reemplazar_nulos_por_moda(df, columnas_categoricas):
        for columna in columnas_categoricas:
            # Calcular la moda de la columna
            moda = df[columna].mode()[0]
            # Reemplazar los valores nulos por la moda
            df[columna] = df[columna].fillna(moda)
            print(f"Después del 'fillna' la columna '{columna}' tiene {df[columna].isnull().sum()} nulos")
        return df
    # Reemplazar nulos por la moda
    df = reemplazar_nulos_por_moda(df, columnas_categoricas)

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Eliminar columnas específicas
    col_eliminar = ['company', '0', 'reservation_status_date']
    df.drop(columns=col_eliminar, axis=1, inplace=True)
    
    months = {'1': 'January', '2': 'February', '3': 'March'}
    # Aplica la sustitución en la columna 'arrival_date_month'
    df['arrival_date_month'] = df['arrival_date_month'].replace(months)

    # Imputar nulos 
    media = df['children'].mean()
    df['children'].fillna(media, inplace=True)
    
    return df

#%%

def reemplazar_booleanos_por_strings(df):
    col_bool = ['is_canceled', 'is_repeated_guest']
    def map_values(value):
        if isinstance(value, bool):
            return 'Yes' if value else 'No'
        return value  # Devuelve el valor original si no es booleano

    # Reemplazar valores en las columnas especificadas
    for columna in col_bool:
        if columna in df.columns:
            df[columna] = df[columna].apply(map_values)
            df[columna] = df[columna].fillna('Unknown')

    # Guardar el DataFrame limpio como un archivo CSV
    df.to_csv("df_limpio.csv", index=False)

    return df
        