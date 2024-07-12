#%%
import pandas as pd
import numpy as np
from src_fhb import EDA

#%%
dataset = EDA.leer_csv('finanzas-hotel-bookings.csv')
dataset
#%%
EDA.exploracion_df(dataset)
# %%
