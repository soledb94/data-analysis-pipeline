import pandas as pd


def dataSet():
    data=pd.read_csv("input/clean.csv")
    return data

def information(df):
    data_max=int(df.value.max())
    data_min=int(df.value.min())
    info=f"The min value for the month was {data_min} µg/m³, and the max value, {data_max} µg/m³"
    return info

def mean_information(df):
    data_mean=int(df.value.mean())
    return data_mean

    

def filters(df,city,measurement):
    filtered=df[(df["city"] == (city)) & (df["parameter"] ==(measurement))]
    return filtered