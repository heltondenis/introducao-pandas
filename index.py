import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
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

# Gráfico de disperção
st.write("""
Análise de disperção
""")
st.text("""
As variáveis utilizadas não representam uma disperção equivalente, porém em situações como
a dengue, se correlacionarmos a temperatura com os casos são duas variáveis que fazem
sentido a utilização do gráfico
""")
df.plot.scatter('Low', 'High')
st.pyplot()

# exemplo de Waffle
st.write("""
Gráfico de Waffle
""")
st.text("""
Exemplo de gráfico de Waffle com a média das variáveis altas e baixas.
""")

fig = plt.figure(
                FigureClass=Waffle,
                rows=4,
                columns=6,
                values={ df['High'].mean(),
                         df['Close'].mean()}, 
                         icons='plane',
                legend={
                        'bbox_to_anchor': (1.1, 1)}
                )
 
fig.set_tight_layout(False)
st.pyplot()
