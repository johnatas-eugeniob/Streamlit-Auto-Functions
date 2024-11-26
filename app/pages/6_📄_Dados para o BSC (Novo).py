import streamlit as st
import pandas as pd
import pygsheets
import os
import ssl
import certifi

ssl._create_default_https_context = ssl._create_unverified_context



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
        st.subheader("SETEMBRO")
        optionM7 = st.checkbox(label="09/09/2024 - Devolução de insumos (Todas as Operações)")
        optionM8 = st.checkbox(label="23/09/2024 - Devolução e Expedição de Roll Container (Todas as Operações)")
        optionM9 = st.checkbox(label="23/09/2024 - Tratativa de Pacotes em Loop (Reversa Nacional)")
        st.subheader("OUTUBRO")
        optionM10 = st.checkbox(label="07/10/2024 - Não Conformidades (Todas as Operações)")
        optionM11 = st.checkbox(label="21/10/2024 - Reportar danos dos Equipamentos (Todas as Operações)")
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
    if optionM7:
        selected_keys_multiplica.append(27)
    if optionM8:
        selected_keys_multiplica.append(29)
    if optionM9:
        selected_keys_multiplica.append(31)
    if optionM10:
        selected_keys_multiplica.append(33)
    if optionM11:
        selected_keys_multiplica.append(35)


#----------------------------------------------------------------------------------------------------------

# Container para as operações lidera
with st.container(border = True):
    st.title("Lidera OPS:")

    # Definindo as colunas para os bimestres
    bimestreLidera1, bimestreLidera2, bimestreLidera3, bimestreLidera4  = st.columns(4)

    with bimestreLidera1:
        st.subheader("JULHO") 
        optionL1 = st.checkbox(label="30/07/2024 - Novo Check List de Auditoria para H2", key="optionL1") 
        st.subheader("SETEMBRO") 
        optionL2 = st.checkbox(label="09/09/2024 - Devolução e Expedição de Roll Container (Todas as Operações)", key="optionL2") 
        optionL3 = st.checkbox(label="23/09/2024 - 5s para Liderança (Todas as Operações)", key="optionL3") 
        st.subheader("OUTUBRO") 
        optionL4 = st.checkbox(label="07/10/2024 - Plano de Ação (Todas as Operações)", key="optionL4") 
        optionL5 = st.checkbox(label="21/10/2024 - Reportar danos dos Equipamentos (Todas as Operações)", key="optionL5")

    # Lista para armazenar as chaves selecionadas no container lidera
    selected_keys_lidera = []

    if optionL1:
        selected_keys_lidera.append(15)
    if optionL2:
        selected_keys_lidera.append(17)
    if optionL3:
        selected_keys_lidera.append(19)
    if optionL4:
        selected_keys_lidera.append(21)
    if optionL5:
        selected_keys_lidera.append(23)

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
medias_base = {}

button_execute = st.button("Gerar Planilha")
if button_execute:
    # Dicionários para armazenar as informações coletadas
    uns_contados = {}
    total_multiplica = {}
    lider_uns_contados = {}
    total_lider = {}
    medias_base = {}
    medias_base_lidera = {}

    # Iterar sobre as linhas na primeira planilha (Multiplica OPS)
    for i in range(len(df)):
        base = df.iloc[i, 7]  # Base na coluna H (índice 7)
        media = df.iloc[i, 36]  # Média na coluna AC (índice 29)
        
        # Ignorar as bases que contêm "Posto Avançado", "PA" ou "BOX"
        if any(substring in base for substring in ["Posto Avançado", "PA", "BOX", "Box", "Posto Avan", "POSTO AVANÇADO"]):
            continue
        
        if df.iloc[i, 38] != "Sim": #pegar dados só da reversa = and df.iloc[i, 10] == "Reversa Nacional"
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
            uns_contados[base] = uns_contados.get(base, 0) + uns_para_contar
            total_multiplica[base] = total_multiplica.get(base, 0) + total_contados
            
            # Armazenar as médias
            try:
                media_value = float(media.replace('%', '').replace(',', '.'))
                medias_base.setdefault(base, []).append(media_value)
            except ValueError:
                st.warning(f"Erro ao converter valor '{media}' para float na base {base}.")

    # Iterar sobre as linhas da segunda planilha (Lidera OPS)
    for k in range(len(df_lidera)):
        base_lidera = df_lidera.iloc[k, 7]  # Base na coluna H (índice 7)
        media_lidera = df_lidera.iloc[k, 24]  # Supondo que a média está na coluna 19
        
        if any(substring in base_lidera for substring in ["Posto Avançado", "PA", "BOX", "Box", "Posto Avan", "POSTO AVANÇADO"]):
            continue
        
        total_contados_lidera = 0
        uns_para_contar_lidera = 0

        # Iterar sobre as colunas
        for l in range(len(df_lidera.iloc[k])):
            value_lidera = df_lidera.iloc[k, l]
            if l in selected_keys_lidera and (value_lidera == "0" or value_lidera == "1"):
                total_contados_lidera += 1
                if value_lidera == "1":
                    uns_para_contar_lidera += 1

        lider_uns_contados[base_lidera] = lider_uns_contados.get(base_lidera, 0) + uns_para_contar_lidera
        total_lider[base_lidera] = total_lider.get(base_lidera, 0) + total_contados_lidera
        
        try:
            media_value_lidera = float(media_lidera.replace('%', '').replace(',', '.'))
            medias_base_lidera.setdefault(base_lidera, []).append(media_value_lidera)
        except ValueError:
            st.warning(f"Erro ao converter valor '{media_lidera}' para float na base {base_lidera}.")

    # Após o processamento, calcule as médias finais
    medias_finais_base = {base: sum(medias)/len(medias) for base, medias in medias_base.items()}
    medias_finais_lidera = {base: sum(medias)/len(medias) for base, medias in medias_base_lidera.items()}

    # Exibir resultados em um único DataFrame
    combined_results = pd.DataFrame({
        "Base": list(set(uns_contados.keys()).union(set(lider_uns_contados.keys()))),
        "Planejado - Multiplicadores": [total_multiplica.get(base, 0) for base in list(set(uns_contados.keys()).union(set(lider_uns_contados.keys())))],
        "Aderência Multiplicador": [f"{medias_finais_base.get(base, 0):.2f}".replace('.', ',') for base in list(set(uns_contados.keys()).union(set(lider_uns_contados.keys())))],
        "Planejado - Líderes": [total_lider.get(base, 0) for base in list(set(uns_contados.keys()).union(set(lider_uns_contados.keys())))],
        "Aderência Líderes": [f"{medias_finais_lidera.get(base, 0):.2f}".replace('.', ',') for base in list(set(uns_contados.keys()).union(set(lider_uns_contados.keys())))],
        "Realizado - Multiplicadores": [uns_contados.get(base, 0) for base in list(set(uns_contados.keys()).union(set(lider_uns_contados.keys())))],
        "Realizado - Líderes": [lider_uns_contados.get(base, 0) for base in list(set(uns_contados.keys()).union(set(lider_uns_contados.keys())))]
    })

    st.subheader("Resultado da Presença aos cursos escolhidos:")
    st.dataframe(combined_results, width=1400)

