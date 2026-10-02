# Passo a passo do seu programa
# Título do programa
# Seção Cadastrar Vendas
    # Campo Data
    # Campo Vendedor - Ana, Bruno, Carla
    # Campo Produto - Notebook, fone, Celulr
    # Campo Quantidade
    # Campo Valor
    # Botão Cadastrar Venda
        # quando eu clicaar botão -> ele tem que adicionar a venda na lista de vendas cadastradas e nos demais itens
# seção Vendas Cadastradas
    # Tael com as vendas
# Seção Dashboard
    # Card/Métrica -> Faturamento Total
    # Gráfico de Barras/Coluna -> Vendas por Vendedor
    # Gráfico de Pizza -> Vendas por Produto

# pip install streamlit pandas plotly
# Para não ter problema de rodar o streamlit, você precisa rodar o comando no terminal: streamlit run codigo.py 
# Precisa abrir o "Folder" ou pasta diretamente no que estou trabalhando, daí não preciso do comando cd.
# EXISTE UM VÍDEO STREAMLIT HASHTAG ELE ENSINA COMO ALTERAR AS CORES E OUTRAS COISAS.
# streamlit run codigo.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.write("# Sistema de Vendas")
tabela_vendas = pd.read_csv("vendas.csv")  # Lê o arquivo CSV com as vendas cadastradas

# seção Cadastrar Vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data da Venda")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Fone", "Celular"])
quantidade = st.sidebar.number_input("Quantidade", min_value=1, step=1)
valor = st.sidebar.number_input("Valor", min_value=0.0, step=0.01)
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# logica de cadastro
if botao_cadastrar:
    if valor <= 0 or quantidade <= 0 or vendedor == "" or produto == "":
        st.error("Todos os campos devem ser preenchidos corretamente.")
    else:
        nova_venda = [data, vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas) # 119 linhas, exemplo
        tabela_vendas.loc[ultima_linha] = nova_venda  # Adiciona a nova venda na tabela
        tabela_vendas.to_csv("vendas.csv", index=False)  # Salva a tabela atualizada no arquivo CSV
        st.success("Venda cadastrada com sucesso!")

# seção de visualização de vendas cadastradas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

# Exemplo de como você poderia implementar a pesquisa de vendas por ID (opcional)   
    # id_venda = st.number_input("ID da Venda", min_value=1, step=1)
    # botao_pesquisar = st.button("Pesquisar Venda")

# seção Dashboard
st.write("## Dashboard")

# Card/Métrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento:,.2f}")


            # criar o gráfico
            # depois exibe

# Gráfico de Barras/Coluna -> Vendas por Vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", title="Vendas por Vendedor", color="produto")
st.plotly_chart(grafico1)

#  Gráfico de Pizza -> Vendas por Produto
grafico2 = px.pie(tabela_vendas, values="valor", names="produto", title="Vendas por Produto", hole=0.5)
st.plotly_chart(grafico2)

