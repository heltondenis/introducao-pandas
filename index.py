import streamlit as st
import pandas as pd
import matplotlib
import numpy as np

st.write("""
# Introdução ao Pandas
""")

# importar o arquivo csv para o Pandas
df = pd.read_csv("https://raw.githubusercontent.com/carlosfab/curso_data_science_na_pratica/master/modulo_02/BBAS3.SA.csv")

# Média de fechamento
st.write("""
Média de fechamento
""");
media = df["Close"].mean()
media

# Colunas dataset
st.write("""
Colunas
""");
df.columns

# Descrição dataset
st.write("""
Descrição
""");
descricaoDF = df.describe()
descricaoDF

# Maior valor de compra
st.write("""
Maior valor de compra
""");
maiorCompra = df.Open.max()
maiorCompra

# Gráfico dados históricos de compra
st.write("""
Dados históricos de compras
""")

df.High.plot(figsize=(10, 2))
st.pyplot()
