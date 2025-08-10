# hello_dashboard.py
import streamlit as st

# Título da aplicação
st.title("📊 Meu Primeiro Dashboard em Streamlit")

# Texto de apresentação
st.write("Olá, mundo! 👋 Este é o meu primeiro dashboard usando Streamlit.")

# Caixa de entrada de texto
nome = st.text_input("Digite seu nome:")

# Botão de ação
if st.button("Enviar"):
    st.success(f"Bem-vindo ao dashboard, {nome}!")

# Gráfico simples
import pandas as pd
import numpy as np

dados = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(dados)
