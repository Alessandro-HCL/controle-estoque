import streamlit as st
import pandas as pd
from datetime import datetime
from itens_classificados import itens_classificados

st.set_page_config(page_title="Contagem de Estoque", page_icon="📦", layout="wide")

st.title("📋 Contagem de Estoque do Restaurante")
st.markdown("Preencha as quantidades de cada item por categoria.")

# Organiza os itens por categoria
categorias_estoque = {}
for item, categoria in itens_classificados:
    if categoria not in categorias_estoque:
        categorias_estoque[categoria] = []
    categorias_estoque[categoria].append(item)

estoque = {}

with st.form("form_estoque"):
    for categoria, itens in categorias_estoque.items():
        st.subheader(f"{categoria}")
        for item in itens:
            quantidade = st.number_input(f"{item}", min_value=0.0, step=0.1, key=f"{categoria}_{item}")
            estoque[item] = quantidade

    submitted = st.form_submit_button("📥 Gerar planilha de estoque")

if submitted:
    df = pd.DataFrame(list(estoque.items()), columns=["Item", "Quantidade"])
    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"estoque_{data_hora}.xlsx"
    df.to_excel(nome_arquivo, index=False)

    with open(nome_arquivo, "rb") as f:
        st.success("✅ Planilha gerada com sucesso!")
        st.download_button(
            label="📎 Clique aqui para baixar a planilha",
            data=f,
            file_name=nome_arquivo,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )