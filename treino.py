import pandas as pd
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

df = pd.read_csv('./data/netflix_clientes_churn_traduzido.csv')

df = pd.get_dummies(df, columns=['regiao'], prefix='regiao', drop_first=True)
df = pd.get_dummies(df, columns=['tipo_assinatura'], prefix='assinatura', drop_first=True)
df = pd.get_dummies(df, columns=['dispositivo'], prefix='dispositivo', drop_first=True)
df = pd.get_dummies(df, columns=['genero'], prefix='genero', drop_first=True)
df = pd.get_dummies(df, columns=['metodo_pagamento'], prefix='pagamento', drop_first=True)
df = pd.get_dummies(df, columns=['genero_favorito'], prefix='genero_favorito', drop_first=True)

for column in df.columns:
    if df[column].dtype == 'bool':
        df[column] = df[column].astype(int)
df.drop(columns=['id_cliente'], inplace=True)

X = df.drop('churn', axis=1)
y = df['churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

