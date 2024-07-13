#%%
import pandas as pd
import numpy as np
from src_fhb import EDA as ed

#%%
dataset = ed.leer_csv('finanzas-hotel-bookings.csv')
dataset.sample(10)
#%%
ed.exploracion_df(dataset)
# %%
limpiando = ed.limpiar_datos(dataset)
limpiando.sample(20)
#%%
df_clear = ed.reemplazar_booleanos_por_strings(limpiando)
df_clear
#%%
ed.exploracion_df(df_clear)
