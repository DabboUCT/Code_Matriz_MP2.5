import pandas as pd
import numpy as np
df = pd.read_excel("datosPython.xlsx",sheet_name="Hoja1",engine="openpyxl")

def clasificar_pm(valor):
    if valor<=79:
        return "Bajo"
    elif valor<=109:
        return "Medio"
    elif valor<=169:
        return "Alto"
    else:
        return "Muy alto"
def clasificar_temp(valor):
    return "Frio" if valor<=10 else "Templado"
def clasificar_lluvia(valor):
    return "Sin lluvia" if valor<=1 else "Con lluvia"
def clasificar_viento(valor):
    return "Sin Viento" if valor<6 else "Con Viento"

df["Clasif_PM"]=df["Registros validados (μg/m3)"].apply(clasificar_pm)
df["Clasif_Temp"]=df["Temperatura media (C°)"].apply(clasificar_temp)
df["Clasif_Lluvia"]=df["Precipitaciones (mm)"].apply(clasificar_lluvia)
df["Clasif_Viento"]=df["Viento (km/hora)"].apply(clasificar_viento)

df["Estado"]=df["Clasif_PM"]+" - "+df["Clasif_Temp"]+" - "+df["Clasif_Lluvia"]+" - "+df["Clasif_Viento"]
estado_dict = {
    "Bajo - Frio - Sin lluvia - Sin Viento": 0,
    "Bajo - Frio - Sin lluvia - Con Viento": 1,
    "Bajo - Frio - Con lluvia - Sin Viento": 2,
    "Bajo - Frio - Con lluvia - Con Viento": 3,
    "Bajo - Templado - Sin lluvia - Sin Viento": 4,
    "Bajo - Templado - Sin lluvia - Con Viento": 5,
    "Bajo - Templado - Con lluvia - Sin Viento": 6,
    "Bajo - Templado - Con lluvia - Con Viento": 7,
    "Medio - Frio - Sin lluvia - Sin Viento": 8,
    "Medio - Frio - Sin lluvia - Con Viento": 9,
    "Medio - Frio - Con lluvia - Sin Viento": 10,
    "Medio - Frio - Con lluvia - Con Viento": 11,
    "Medio - Templado - Sin lluvia - Sin Viento": 12,
    "Medio - Templado - Sin lluvia - Con Viento": 13,
    "Medio - Templado - Con lluvia - Sin Viento": 14,
    "Medio - Templado - Con lluvia - Con Viento": 15,
    "Alto - Frio - Sin lluvia - Sin Viento": 16,
    "Alto - Frio - Sin lluvia - Con Viento": 17,
    "Alto - Frio - Con lluvia - Sin Viento": 18,
    "Alto - Frio - Con lluvia - Con Viento": 19,
    "Alto - Templado - Sin lluvia - Sin Viento": 20,
    "Alto - Templado - Sin lluvia - Con Viento": 21,
    "Alto - Templado - Con lluvia - Sin Viento": 22,
    "Alto - Templado - Con lluvia - Con Viento": 23,
    "Muy alto - Frio - Sin lluvia - Sin Viento": 24,
    "Muy alto - Frio - Sin lluvia - Con Viento": 25,
    "Muy alto - Frio - Con lluvia - Sin Viento": 26,
    "Muy alto - Frio - Con lluvia - Con Viento": 27,
    "Muy alto - Templado - Sin lluvia - Sin Viento": 28,
    "Muy alto - Templado - Sin lluvia - Con Viento": 29,
    "Muy alto - Templado - Con lluvia - Sin Viento": 30,
    "Muy alto - Templado - Con lluvia - Con Viento": 31
}

df["Estado_Num"]=df["Estado"].map(estado_dict)
df["Estado_siguiente"]=df["Estado_Num"].shift(-1)  
df=df.iloc[:-1]

conteo_transiciones=df.groupby(["Estado_Num","Estado_siguiente"]).size().unstack(fill_value=0)

matriz_transicion=conteo_transiciones.div(conteo_transiciones.sum(axis=1), axis=0).fillna(0)

matriz_transicion.to_html("matriz_transicion.html")

print(matriz_transicion)
