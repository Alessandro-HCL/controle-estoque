import streamlit as st
import pandas as pd
from datetime import datetime
import yagmail
from itens_classificados import itens_classificados

# 💵 Dicionário com valores unitários por item
valores_unitarios = {
    "492 - granola (KG)": 5.00,
    "495 - leite em po (KG)": 1.00,
}

# 📋 Opções de contagem
opcoes_contagem = {
    "1": "consumo_cafe_da_manha",
    "2": "consumo_casamento_cozinha",
    "3": "consumo_casamento_salao",
    "4": "consumo_pre_wedding",
    "5": "consumo_pos_wedding",
    "6": "contagem_estoque"
}

st.title("📦 Contagem de Itens - Villa Sonali")

# 📌 Menu para objetivo
escolha = st.selectbox("Selecione o objetivo da contagem:", list(opcoes_contagem.values()))
objetivo = escolha

# 📦 Organiza os itens por categoria
categorias_estoque = {}
for item, categoria in itens_classificados:
    if categoria not in categorias_estoque:
        categorias_estoque[categoria] = []
    categorias_estoque[categoria].append(item)

estoque = {}

st.write("### 📋 Insira as quantidades dos itens:")

# Interface de entrada para os itens
for categoria, itens in categorias_estoque.items():
    with st.expander(f"📂 {categoria.title()}"):
        for item in itens:
            quantidade = st.number_input(f"{item}", min_value=0.0, step=0.1, key=item)
            valor_unitario = valores_unitarios.get(item, 1.00)
            valor_total = round(quantidade * valor_unitario, 2)

            if quantidade > 0:
                estoque[item] = {
                    "Quantidade": quantidade,
                    "Valor Unitário (R$)": valor_unitario,
                    "Valor Total (R$)": valor_total
                }

# 📁 Botão para gerar planilha
if st.button("📥 Gerar Planilha e Enviar por Email"):
    if not estoque:
        st.warning("⚠️ Nenhum item com quantidade informada.")
    else:
        df = pd.DataFrame.from_dict(estoque, orient="index")
        df.reset_index(inplace=True)
        df.rename(columns={"index": "Item"}, inplace=True)

        data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nome_arquivo = f"{objetivo}_{data_hora}.xlsx"
        df.to_excel(nome_arquivo, index=False)

        # Envio de e-mail
        try:
            yag = yagmail.SMTP(user="ale.moreira@gmail.com", password="gncuqrzzkstgeamn")
            yag.send(
                to="ale.moreira@gmail.com",
                subject=f"📋 Relatório - {objetivo.replace('_', ' ').title()}",
                contents=f"Segue em anexo o controle de estoque referente a: {objetivo.replace('_', ' ').title()}",
                attachments=nome_arquivo
            )
            st.success(f"📧 Email enviado com sucesso! Planilha: `{nome_arquivo}`")
        except Exception as e:
            st.error(f"❌ Erro ao enviar e-mail: {e}")
