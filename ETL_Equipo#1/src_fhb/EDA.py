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
