import pandas as pd

# leitura dos dados csv
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")


def getDataHead(n):
    # vizualiando as primeiras linhas
    return df.head(n)


def getDescribe():
    # estatisticas básicas
    return df.describe()


def getInfo():
    # dataframe info
    return df.info()
