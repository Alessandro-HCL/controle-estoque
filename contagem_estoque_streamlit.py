# import streamlit as st
# import pandas as pd
# from datetime import datetime
# from itens_classificados import itens_classificados
#
# st.set_page_config(page_title="Contagem de Estoque", page_icon="📦", layout="wide")
#
# st.title("📋 Contagem de Estoque do Restaurante")
# st.markdown("Preencha as quantidades de cada item por categoria.")
#
# # Organiza os itens por categoria
# categorias_estoque = {}
# for item, categoria in itens_classificados:
#     if categoria not in categorias_estoque:
#         categorias_estoque[categoria] = []
#     categorias_estoque[categoria].append(item)
#
# estoque = {}
#
# with st.form("form_estoque"):
#     for categoria, itens in categorias_estoque.items():
#         st.subheader(f"{categoria}")
#         for item in itens:
#             quantidade = st.number_input(f"{item}", min_value=0.0, step=0.1, key=f"{categoria}_{item}")
#             estoque[item] = quantidade
#
#     submitted = st.form_submit_button("📥 Gerar planilha de estoque")
#
# if submitted:
#     df = pd.DataFrame(list(estoque.items()), columns=["Item", "Quantidade"])
#     data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     nome_arquivo = f"estoque_{data_hora}.xlsx"
#     df.to_excel(nome_arquivo, index=False)
#
#     with open(nome_arquivo, "rb") as f:
#         st.success("✅ Planilha gerada com sucesso!")
#         st.download_button(
#             label="📎 Clique aqui para baixar a planilha",
#             data=f,
#             file_name=nome_arquivo,
#             mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         )

import streamlit as st
import pandas as pd
from datetime import datetime
import yagmail
from itens_classificados import itens_classificados

# 📦 Organiza os itens por categoria
categorias_estoque = {}
for item, categoria in itens_classificados:
    if categoria not in categorias_estoque:
        categorias_estoque[categoria] = []
    categorias_estoque[categoria].append(item)

st.set_page_config(page_title="Contagem de Estoque", layout="wide")
st.title("📋 Controle de Estoque - Contagem Manual")

estoque = {}

st.write("Preencha as quantidades por item:")

for categoria, itens in categorias_estoque.items():
    with st.expander(f"📦 {categoria}"):
        for item in itens:
            quantidade = st.number_input(f"{item}", min_value=0.0, step=0.1, key=item)
            estoque[item] = quantidade

# 📤 Função para enviar e-mail
def enviar_email(destinatario, assunto, corpo, anexo):
    try:
        yag = yagmail.SMTP(user="ale.moreira@gmail.com", password="gncuqrzzkstgeamn")
        yag.send(to=destinatario, subject=assunto, contents=corpo, attachments=anexo)
        st.success("📧 Email enviado com sucesso!")
    except Exception as e:
        st.error(f"❌ Erro ao enviar e-mail: {e}")

# 📥 Botão de ação
if st.button("✅ Gerar Planilha e Enviar por Email"):
    df = pd.DataFrame(list(estoque.items()), columns=["Item", "Quantidade"])
    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"estoque_{data_hora}.xlsx"
    df.to_excel(nome_arquivo, index=False)

    st.success(f"📄 Planilha gerada com sucesso: {nome_arquivo}")

    enviar_email(
        destinatario="ale.moreira@gmail.com",
        assunto="📦 Relatório de Estoque - Contagem Manual",
        corpo="Segue em anexo o controle de estoque atualizado conforme a contagem manual.",
        anexo=nome_arquivo
    )