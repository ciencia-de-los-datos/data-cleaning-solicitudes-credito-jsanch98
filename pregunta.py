"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def to_lower(valor):
    return str(valor).lower().strip()

def remplazar_strip(valor):
    return str(valor).lower().replace("-"," ").replace("_"," ").strip()

def remplazar(valor):
    return str(valor).lower().replace("-"," ").replace("_"," ")

def convertir_int(valor):
    nuevo_valor = 0
    try:
        nuevo_valor = int(float(valor))
    except:
        nuevo_valor = valor
    return nuevo_valor

def limpiar_montos(monto):
    return  str(monto).strip("$").strip().replace(".00", "").replace(",", "")

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    #
    # Inserte su código aquí
    #

    df = df.dropna()
    df = df.drop(['Unnamed: 0'], axis=1)
    df[["sexo", "tipo_de_emprendimiento", "idea_negocio", "monto_del_credito", "línea_credito"]] \
          = df[["sexo", "tipo_de_emprendimiento", "idea_negocio", "monto_del_credito", "línea_credito"]].applymap(to_lower)
    df[["idea_negocio", "línea_credito"]] = df[["idea_negocio", "línea_credito"]].applymap(remplazar_strip)
    df["barrio"] = df["barrio"].apply(remplazar)
    df["comuna_ciudadano"] = df["comuna_ciudadano"].transform(convertir_int)
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True)
    df["monto_del_credito"] = df["monto_del_credito"].apply(limpiar_montos)
    df = df.drop_duplicates()

    return df