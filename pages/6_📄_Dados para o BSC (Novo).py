import streamlit as st
import pandas as pd
import pygsheets
import os 

st.set_page_config(page_title="Dados para o BSC", 
                   page_icon="📄", 
                   layout="wide"                   
                )

with st.sidebar:
    st.write("Passo a Passo:")
    st.write("Selecione uma checkbox referente ao mês do curso, eles estão separados em Multiplica e Lidera OPS")

# Add CSS styles for the containers (opcional)
st.subheader("Selecione os cursos abaixo:")

credentials = pygsheets.authorize(service_file=os.path.join(os.getcwd(), "cred.json"))

meuArquivoGsheets = "https://docs.google.com/spreadsheets/d/1zw56-hBt4JNdBoM5s5TOUNJazSfmmmAwbX5jZacw-Fc/edit?gid=1356081681#gid=1356081681"
arquivo = credentials.open_by_url(meuArquivoGsheets)
aba = arquivo.worksheet_by_title("Matriz Multiplica OPS")
data = aba.get_all_values()
df = pd.DataFrame(data)
df = df.iloc[5:, 0:]  # Ajuste para pular as 4 primeiras linhas 

#LIDERA OPS
aba_lidera = arquivo.worksheet_by_title("Matriz Lidera OPS")
data_lidera = aba_lidera.get_all_values()
df_lidera = pd.DataFrame(data_lidera)  
df_lidera = df_lidera.iloc[5:, 0:] # Ajuste para pular as 4 primeiras linhas

#---------------------------------------------------------------------------------------------------------------

# Container para as operações multiplica
with st.container(border = True):
    st.title("Multiplica OPS:")

    # Definindo as colunas para os bimestres
    trimestre1, trimestre2 = st.columns(2)

    with trimestre1:
        st.subheader("JULHO")
        optionM1 = st.checkbox(label="29/07/2024 - Lacres Vermelhos e suas Utilizações")
        st.subheader("AGOSTO")
        optionM2 = st.checkbox(label="05/08/2024 - Processamento com gaiolas Roll Container	")
        optionM3 = st.checkbox(label="12/08/2024 - Carregamento em Gaiolas Roll Containers	")
        optionM4 = st.checkbox(label="12/08/2024 - Gestão de Backlog (Agências + PA's)")
        optionM5 = st.checkbox(label="26/08/2024 - Consulta e transferência de coletas (Agências + PA's)")
        optionM6 = st.checkbox(label="26/08/2024 - Embalagens Inadequadas (Reversa Nacional)")
        
    # Lista para armazenar as chaves selecionadas no container multiplica
    selected_keys_multiplica = []

    if optionM1:
        selected_keys_multiplica.append(15)
    if optionM2:
        selected_keys_multiplica.append(17)
    if optionM3:
        selected_keys_multiplica.append(19)
    if optionM4:
        selected_keys_multiplica.append(21)
    if optionM5:
        selected_keys_multiplica.append(23)
    if optionM6:
        selected_keys_multiplica.append(25)

#----------------------------------------------------------------------------------------------------------

# Container para as operações lidera
with st.container(border = True):
    st.title("Lidera OPS:")

    # Definindo as colunas para os bimestres
    bimestreLidera1, bimestreLidera2, bimestreLidera3, bimestreLidera4  = st.columns(4)

    with bimestreLidera1:
        st.subheader("JULHO")
        optionL1 = st.checkbox(label="30/07/2024 - Novo Check List de Auditoria para H2")
        optionL2 = st.checkbox(label="??/??/???? - Capacitação aos Postos de Trabalho")

        # Lista para armazenar as chaves selecionadas no container lidera
        selected_keys_lidera = []

        if optionL1:
            selected_keys_lidera.append(15)
        if optionL2:
            selected_keys_lidera.append(17)

chaves_multiplica, chaves_lidera, chaves_reserva = st.columns(3)
# Exibindo as chaves selecionadas
with chaves_multiplica:
    st.write("Chaves selecionadas no container **Multiplica**:", str(selected_keys_multiplica))
with chaves_lidera:
    st.write("Chaves selecionadas no container **Lidera**:", str(selected_keys_lidera))
with chaves_reserva:
    st.write("")

#-------------------------------------------------------------------------------------------------------------------------------

uns_contados = {}
total_multiplica = {}
lider_uns_contados = {}
total_lider = {}

button_execute = st.button("Gerar Planilha")
if button_execute:
    # Iterar sobre as linhas na primeira planilha
    for i in range(len(df)):
        base = df.iloc[i, 7]  # Base na coluna H (índice 0)
        
        if df.iloc[i, 20] != "Sim":  # Coluna "AV" é o índice 40
            # Inicializar contadores para a base atual
            total_contados = 0
            uns_para_contar = 0
            
            # Iterar sobre todas as colunas
            for j in range(len(df.iloc[i])):
                value = df.iloc[i, j]
                if j in selected_keys_multiplica and (value == "0" or value == "1"):
                    total_contados += 1
                    if value == "1":
                        uns_para_contar += 1
            
            # Armazenar contagem de 1s para a base atual
            if base in uns_contados:
                uns_contados[base] += uns_para_contar
            else:
                uns_contados[base] = uns_para_contar
            
            # Se a base já foi contabilizada, adicionar ao total existente
            if base in total_multiplica:
                total_multiplica[base] += total_contados
            else:
                total_multiplica[base] = total_contados

#---------------------------------------------------------------------------------------------------------------
    
    #LIDERA OPS
    for k in range(len(df_lidera)):
        base_lidera = df_lidera.iloc[k, 7]  # Base na coluna H (índice 0)
        
        # Inicializar contadores para a base atual
        total_contados_lidera = 0
        uns_para_contar_lidera = 0
            
        # Iterar sobre todas as colunas
        for l in range(len(df_lidera.iloc[k])):
            value_lidera = df_lidera.iloc[k, l]
            if l in selected_keys_lidera and (value_lidera == "0" or value_lidera == "1"):
                total_contados_lidera += 1
                if value_lidera == "1":
                    uns_para_contar_lidera += 1
        
        # Armazenar contagem de 1s para a base atual
        if base_lidera in lider_uns_contados:
            lider_uns_contados[base_lidera] += uns_para_contar_lidera
        else:
            lider_uns_contados[base_lidera] = uns_para_contar_lidera
        
        # Se a base já foi contabilizada, adicionar ao total existente
        if base_lidera in total_lider:
            total_lider[base_lidera] += total_contados_lidera
        else:
            total_lider[base_lidera] = total_contados_lidera
    
    #Colunas de exibição
    exibir_dados = st.columns(2, vertical_alignment ="center")

    # Combinar os resultados dos dois DataFrames em um único DataFrame
    combined_results = pd.DataFrame({
        "Base": list(set(list(uns_contados.keys()) + list(lider_uns_contados.keys()))),
        "Planejado - Multiplicadores": [total_multiplica.get(base, 0) for base in list(set(list(uns_contados.keys()) + list(lider_uns_contados.keys())))],
        "Planejado - Líderes": [total_lider.get(base, 0) for base in list(set(list(uns_contados.keys()) + list(lider_uns_contados.keys())))],
        "Realizado - Multiplicadores": [uns_contados.get(base, 0) for base in list(set(list(uns_contados.keys()) + list(lider_uns_contados.keys())))],
        "Realizado - Líderes": [lider_uns_contados.get(base, 0) for base in list(set(list(uns_contados.keys()) + list(lider_uns_contados.keys())))]
    })

    # Exibir resultados no Streamlit como tabela multiplica
    
    st.subheader("Resultado da Presença aos cursos escolhidos:")
    st.dataframe(combined_results, width = 1400)
