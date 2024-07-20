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
df_clear = ed.reemplazar_bool_and_num_por_strings(limpiando)
df_clear
#%%
ed.exploracion_df(df_clear)
#%%
m = ed.leer_csv('df_hotel.csv')
m.sample(10)

# %%
ed.exploracion_df(m)