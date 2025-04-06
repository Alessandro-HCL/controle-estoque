# import pandas as pd
# from datetime import datetime
# import yagmail
#
# # Lista de itens de controle de estoque
# itens = ['Água com gás', 'Água sem gás', 'Coca-Cola']
#
# # Dicionário para armazenar as quantidades
# estoque = {}
#
# print("Insira as quantidades dos itens:")
#
# for item in itens:
#     while True:
#         try:
#             quantidade = int(input(f"{item}: "))
#             estoque[item] = quantidade
#             break
#         except ValueError:
#             print("Digite um número válido.")
#
# # Criar DataFrame com os dados
# df = pd.DataFrame(list(estoque.items()), columns=['Item', 'Quantidade'])
#
# # Gerar o nome do arquivo com data e hora
# data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# nome_arquivo = f"estoque_{data_hora}.xlsx"
# df.to_excel(nome_arquivo, index=False)
#
# print(f"Planilha gerada: {nome_arquivo}")
#
# # Enviar por e-mail
# def enviar_email(destinatario, assunto, corpo, anexo):
#     try:
#         # Coloque aqui seu e-mail e senha de aplicativo
#         yag = yagmail.SMTP(user="ale.moreira@gmail.com", password="gncuqrzzkstgeamn")
#         yag.send(to=destinatario, subject=assunto, contents=corpo, attachments=anexo)
#         print("Email enviado com sucesso!")
#     except Exception as e:
#         print("Erro ao enviar e-mail:", e)
#
# # Exemplo de envio
# email_destino = "ale.moreira@gmail.com"
# enviar_email(
#     destinatario=email_destino,
#     assunto="Relatório de Estoque",
#     corpo="Segue em anexo o controle de estoque do dia.",
#     anexo=nome_arquivo
# )





# import pandas as pd
# from datetime import datetime
# import yagmail
#
# # Lista de itens atualizada
# itens = [
#     "492 - granola (KG)",
#     "495 - leite em po (KG)",
#     "496 - achocolatado (KG)",
#     "499 - açai  (KG)"
# ]
#
# # Dicionário para armazenar as quantidades
# estoque = {}
#
# print("Insira as quantidades dos itens:")
#
# for item in itens:
#     while True:
#         try:
#             quantidade = float(input(f"{item}: "))
#             estoque[item] = quantidade
#             break
#         except ValueError:
#             print("⚠️ Digite um número válido.")
#
# # Criar DataFrame com os dados
# df = pd.DataFrame(list(estoque.items()), columns=['Item', 'Quantidade'])
#
# # Gerar o nome do arquivo com data e hora
# data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# nome_arquivo = f"estoque_{data_hora}.xlsx"
# df.to_excel(nome_arquivo, index=False)
#
# print(f"✅ Planilha gerada: {nome_arquivo}")
#
# # Função para envio de e-mail
# def enviar_email(destinatario, assunto, corpo, anexo):
#     try:
#         yag = yagmail.SMTP(user="ale.moreira@gmail.com", password="gncuqrzzkstgeamn")
#         yag.send(to=destinatario, subject=assunto, contents=corpo, attachments=anexo)
#         print("📧 Email enviado com sucesso!")
#     except Exception as e:
#         print("❌ Erro ao enviar e-mail:", e)
#
# # Enviar para o e-mail definido
# email_destino = "ale.moreira@gmail.com"
# enviar_email(
#     destinatario=email_destino,
#     assunto="Relatório de Estoque",
#     corpo="Segue em anexo o controle de estoque do dia.",
#     anexo=nome_arquivo
# )


# import pandas as pd
# from datetime import datetime
# import yagmail
# from itens_estoque_completo_final import itens
#
# # Lista completa de itens de estoque (trecho de exemplo, para não ficar gigante aqui)
# # itens = [
# #     "499 - açai  (kg)",
# #     "495 - leite em po (kg)",
# #     "492 - granola (kg)",
# #     "100 - suco del valle uva (un)",
# #     "101 - suco del valle pessego (un)",
# #     "102 - espumante bossa dem sec n2 (un)",
# #     "104 - espumante bossa brut (un)",
# #     "106 - espumante la linda extra brut (un)",
# #     "108 - vinho branco fausto pizzato chardonnay (un)",
# #     "113 - vinho branco muros antigos  (un)",
# #     "115 - vinho branco claude val paul mas gewustraminer (un)",
# #     "12 - agua c/gas (un)",
# #     # ... (adicione o restante da lista completa aqui)
# # ]
#
# estoque = {}
#
# print("📦 Insira as quantidades dos itens de estoque:")
#
# for item in itens:
#     while True:
#         try:
#             quantidade = float(input(f"{item}: "))
#             estoque[item] = quantidade
#             break
#         except ValueError:
#             print("⚠️ Por favor, digite um número válido.")
#
# # Gerar planilha com os dados
# df = pd.DataFrame(list(estoque.items()), columns=['Item', 'Quantidade'])
# data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# nome_arquivo = f"estoque_{data_hora}.xlsx"
# df.to_excel(nome_arquivo, index=False)
#
# print(f"✅ Planilha gerada: {nome_arquivo}")
#
# # Função para enviar e-mail
# def enviar_email(destinatario, assunto, corpo, anexo):
#     try:
#         yag = yagmail.SMTP(user="ale.moreira@gmail.com", password="gncuqrzzkstgeamn")
#         yag.send(to=destinatario, subject=assunto, contents=corpo, attachments=anexo)
#         print("📧 Email enviado com sucesso!")
#     except Exception as e:
#         print("❌ Erro ao enviar e-mail:", e)
#
# # Envia o arquivo por e-mail
# email_destino = "ale.moreira@gmail.com"
# enviar_email(
#     destinatario=email_destino,
#     assunto="📋 Relatório de Estoque - Contagem do Dia",
#     corpo="Segue em anexo o controle de estoque atualizado conforme a contagem manual.",
#     anexo=nome_arquivo
# )


# import pandas as pd
# from datetime import datetime
# import yagmail
#
# # Dicionário com categorias e itens
# categorias_estoque = {
#     "Proteínas": [
#         "300 - coxa sobre coxa de frango (KG)",
#         "301 - peito de frango (KG)",
#         "314 - picanha suina (KG)",
#         "298 - file mignon (KG)",
#         "299 - entrecot (KG)",
#         "313 - frango passarinho (KG)"
#     ],
#     "Bebidas": [
#         "12 - agua c/gas (UN)",
#         "16 - coca cola lata (UN)",
#         "28 - cerveja original 600ml (UN)",
#         "102 - espumante bossa dem sec n2 (UN)",
#         "128 - vinho tinto terranoble cabernet sauvignon 375ml (UN)"
#     ],
#     "Frios e Laticínios": [
#         "272 - manteiga (KG)",
#         "283 - creme de leite (KG)",
#         "284 - leite (LT)",
#         "281 - cream cheese (KG)",
#         "274 - queijo parmesao (KG)"
#     ],
#     "Hortifruti": [
#         "317 - cebola branca (KG)",
#         "318 - cebola roxa (KG)",
#         "319 - alho (KG)",
#         "342 - cenoura (KG)",
#         "328 - rucula (KG)"
#     ]
#     # Adicione outras categorias conforme necessário
# }
#
# estoque = {}
#
# print("📦 Insira as quantidades dos itens de estoque por categoria:\n")
#
# for categoria, itens in categorias_estoque.items():
#     print(f"\n=== {categoria.upper()} ===")
#     for item in itens:
#         while True:
#             try:
#                 quantidade = float(input(f"{item}: "))
#                 estoque[item] = quantidade
#                 break
#             except ValueError:
#                 print("⚠️ Por favor, digite um número válido.")
#
# # Gera a planilha com os dados
# df = pd.DataFrame(list(estoque.items()), columns=['Item', 'Quantidade'])
# data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# nome_arquivo = f"estoque_{data_hora}.xlsx"
# df.to_excel(nome_arquivo, index=False)
#
# print(f"\n✅ Planilha gerada com sucesso: {nome_arquivo}")
#
# # Função para enviar e-mail
# def enviar_email(destinatario, assunto, corpo, anexo):
#     try:
#         yag = yagmail.SMTP(user="ale.moreira@gmail.com", password="gncuqrzzkstgeamn")
#         yag.send(to=destinatario, subject=assunto, contents=corpo, attachments=anexo)
#         print("📧 Email enviado com sucesso!")
#     except Exception as e:
#         print("❌ Erro ao enviar e-mail:", e)
#
# # Envia o arquivo por e-mail
# email_destino = "ale.moreira@gmail.com"
# enviar_email(
#     destinatario=email_destino,
#     assunto="📋 Relatório de Estoque - Contagem do Dia",
#     corpo="Segue em anexo o controle de estoque atualizado conforme a contagem manual.",
#     anexo=nome_arquivo
# )

import pandas as pd
from datetime import datetime
import yagmail

# Importa os itens classificados (arquivo deve estar no mesmo diretório)
from itens_classificados import itens_classificados

# Organiza os itens por categoria
categorias_estoque = {}
for item, categoria in itens_classificados:
    if categoria not in categorias_estoque:
        categorias_estoque[categoria] = []
    categorias_estoque[categoria].append(item)

estoque = {}

print("📦 Insira as quantidades dos itens de estoque por categoria:\n")

for categoria, itens in categorias_estoque.items():
    print(f"\n=== {categoria.upper()} ===")
    for item in itens:
        while True:
            try:
                quantidade = float(input(f"{item}: "))
                estoque[item] = quantidade
                break
            except ValueError:
                print("⚠️ Por favor, digite um número válido.")

# Gera a planilha com os dados
df = pd.DataFrame(list(estoque.items()), columns=['Item', 'Quantidade'])
data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nome_arquivo = f"estoque_{data_hora}.xlsx"
df.to_excel(nome_arquivo, index=False)

print(f"\n✅ Planilha gerada com sucesso: {nome_arquivo}")

# Envia o e-mail com o relatório de estoque
def enviar_email(destinatario, assunto, corpo, anexo):
    try:
        yag = yagmail.SMTP(user="ale.moreira@gmail.com", password="gncuqrzzkstgeamn")
        yag.send(to=destinatario, subject=assunto, contents=corpo, attachments=anexo)
        print("📧 Email enviado com sucesso!")
    except Exception as e:
        print("❌ Erro ao enviar e-mail:", e)

# Enviar planilha por e-mail
email_destino = "ale.moreira@gmail.com"
enviar_email(
    destinatario=email_destino,
    assunto="📋 Relatório de Estoque - Contagem do Dia",
    corpo="Segue em anexo o controle de estoque atualizado conforme a contagem manual.",
    anexo=nome_arquivo
)


