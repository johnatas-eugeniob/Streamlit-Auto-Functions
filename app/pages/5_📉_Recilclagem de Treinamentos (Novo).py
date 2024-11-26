import streamlit as st
import pandas as pd
import pygsheets
import os 

st.set_page_config(page_title="Reciclagem de Treinamentos", 
                   page_icon="📉", 
                   layout="wide"                   
                )

with st.sidebar:
    st.write("Passo a Passo:")
    st.write("Selecione uma checkbox referente aos cursos voltados ao plano Multiplica OPS")

# Add CSS styles for the containers (opcional)
st.subheader("Selecione os cursos abaixo:")

credentials = pygsheets.authorize(service_file=os.path.join(os.getcwd(), "cred.json"))

meuArquivoGsheets = "https://docs.google.com/spreadsheets/d/1zw56-hBt4JNdBoM5s5TOUNJazSfmmmAwbX5jZacw-Fc/edit?gid=1356081681#gid=1356081681"
arquivo = credentials.open_by_url(meuArquivoGsheets)
aba = arquivo.worksheet_by_title("Matriz Multiplica OPS")
data = aba.get_all_values()
df = pd.DataFrame(data)
df = df.iloc[5:, 0:]  # Ajuste para pular as 4 primeiras linhas 

#---------------------------------------------------------------------------------------------------------------

# Container para as operações multiplica
with st.container(border = True):
    st.title("Multiplica OPS:")

    # Definindo as colunas para os bimestres
    trimestre1, trimestre2 = st.columns(2)

    with trimestre1:
        st.subheader("JUNHO")
        option1 = st.checkbox(label="29/07/2024 - Lacres Vermelhos e suas Utilizações.")
        option2 = st.checkbox(label="????? - Processamento com gaiolas Roll Container") 
        
    # Lista para armazenar as chaves selecionadas no container multiplica
    selected_keys_multiplica = []

    if option1:
        selected_keys_multiplica.append(14)
    if option2:
        selected_keys_multiplica.append(16)

#----------------------------------------------------------------------------------------------------------
month_option = st.selectbox(
    "Defina o mês dos cursos para reciclagem:",
    ("JUNHO", "JULHO"))

catch_grip = st.button("Gerar Planilha")
if catch_grip:
    dados_filtrados = []

    for i in range(len(df)):
        dados_por_linha = [df.iloc[i, 0], df.iloc[i, 5], df.iloc[i, 1], df.iloc[i, 7]]
        aderencia_encontrada = False
        for j in range(len(selected_keys_multiplica)):
            reciclagem_treinamentos = df.iloc[i, selected_keys_multiplica[j]]
            if reciclagem_treinamentos != "" and reciclagem_treinamentos != "#N/A":
                # Remover símbolo de porcentagem, se existir, e converter para float
                try:
                    valor = float(reciclagem_treinamentos.strip('%')) / 100 if '%' in reciclagem_treinamentos else float(reciclagem_treinamentos)
                    if valor < 0.8:
                        dados_por_linha.append(f"{valor * 100:.1f}%")
                        aderencia_encontrada = True  
                    else:
                        dados_por_linha.append("")
                except ValueError:
                    dados_por_linha.append("")  # Adicionar vazio se a conversão falhar
            else:
                dados_por_linha.append("")
        if aderencia_encontrada:
            dados_filtrados.append(dados_por_linha)
    st.dataframe(dados_filtrados)
