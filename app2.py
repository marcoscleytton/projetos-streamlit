import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

model = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

model.fit(x, y)

st.title("Prevendo o valor de uma pizza")
st.divider()

diametro = int(st.number_input("Digite o tamanho do diâmetro da Pizza: ",step=1))

if diametro > 0:
    preco_previsto = model.predict([[diametro]])[0][0]
    st.write(f'O valor da pizza com diametro de {diametro} é de R$ {preco_previsto:.2f}.')