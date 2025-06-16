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
    st.write("1° Selecione uma checkbox referente ao treinamento escolhido, eles estão separados em Multiplica e Lidera OPS")
    st.write("2° Após escolher os cursos (Recomendado se ater aos meses serem os mesmos), clique em gerar planiha")
    st.write("3° No processo é pego todas as informações dos cursos escolhidos e assim você pode fazer o download da planilha gerada ao apertar o botão")

# Add CSS styles for the containers (opcional)
st.subheader("Selecione os cursos abaixo:")

credentials = pygsheets.authorize(service_file=os.path.join(os.getcwd(), "cred.json"))

meuArquivoGsheets = "https://docs.google.com/spreadsheets/d/1SqfXhTywdBPIpA1D5hfL1uY2PxyKvV1EUUyjtvFBJxc/edit?usp=sharing"
arquivo = credentials.open_by_url(meuArquivoGsheets)
aba = arquivo.worksheet_by_title("Matriz Multiplica OPS")
data = aba.get_all_values()
df = pd.DataFrame(data)
df = df.iloc[5:, 0:]  # Ajuste para pular as 5 primeiras linhas 

#LIDERA OPS
aba_lidera = arquivo.worksheet_by_title("Matriz Lidera OPS")
data_lidera = aba_lidera.get_all_values()
df_lidera = pd.DataFrame(data_lidera)  
df_lidera = df_lidera.iloc[5:, 0:] # Ajuste para pular as 5 primeiras linhas

#---------------------------------------------------------------------------------------------------------------

# Container para as operações multiplica
with st.container(border = True):
    st.title("Multiplica OPS - 2025:")

    # Definindo as colunas para os bimestres
    trimestre1, trimestre2 = st.columns(2)

    with trimestre1:
        st.subheader("FEVEREIRO")
        optionM1 = st.checkbox(label="03/02/2025 - Boas práticas operacionais (Gaiolas RCON, gaylords e acondicionamento de pacotes) - (Todos os XD's)")
        optionM2 = st.checkbox(label="03/02/2025 - Como evitar Miss Sorting	(Todas as Operações)")
        optionM3 = st.checkbox(label="17/02/2025 - Recebimento das devoluções dos entregadores (Agência e PA)")
        optionM4 = st.checkbox(label="17/02/2025 - Recebimento por inferência (Todos os XD's)")
        st.subheader("MARÇO")
        optionM5 = st.checkbox(label="05/03/2025 - Troca de etiquetas (Todas as Operações)")
        optionM6 = st.checkbox(label="18/03/2025 - Como fazer o fechamento de unitizadores (Todas as Operações)")
        optionM7 = st.checkbox(label="31/03/2025 - Identificação de FIFO (Todos os XD's)")
        st.subheader("ABRIL")
        optionM8 = st.checkbox(label="02/04/2025 - Troca de Custódia (Agência e PA)")
        optionM9 = st.checkbox(label="14/04/2025 - Separação de descartes e insumos (Todos os XD's)")
        optionM10 = st.checkbox(label="14/04/2025 - Recusa de pacotes (Agência e PA)")
        optionM11 = st.checkbox(label="22/04/2025 - Tipos de Avaria (Todas as Operações)")
        st.subheader("MAIO")
        optionM12 = st.checkbox(label="05/05/2025 - MULTPLICA OPS - Check-In e Check-Out (XD CAJ)")
        optionM13 = st.checkbox(label="12/05/2025 - Bipagem nos chutes do Sorter Linear (XD CAJ)")
        optionM14 = st.checkbox(label="19/05/2025 - Acomodação de pacotes em gaiolas e gaylords (Todas as Operações)")

    # Lista para armazenar as chaves selecionadas no container multiplica
    selected_keys_multiplica = []
    selected_keys_multiplica_ad = []

    if optionM1:
        selected_keys_multiplica_ad.append(14)
        selected_keys_multiplica.append(15)
    if optionM2:
        selected_keys_multiplica_ad.append(16)
        selected_keys_multiplica.append(17)
    if optionM3:
        selected_keys_multiplica_ad.append(18)
        selected_keys_multiplica.append(19)
    if optionM4:
        selected_keys_multiplica_ad.append(20)
        selected_keys_multiplica.append(21)
    if optionM5:
        selected_keys_multiplica_ad.append(22)
        selected_keys_multiplica.append(23)
    if optionM6:
        selected_keys_multiplica_ad.append(24)
        selected_keys_multiplica.append(25)
    if optionM7:
        selected_keys_multiplica_ad.append(26)
        selected_keys_multiplica.append(27)
    if optionM8:
        selected_keys_multiplica_ad.append(28)
        selected_keys_multiplica.append(29)
    if optionM9:
        selected_keys_multiplica_ad.append(30)
        selected_keys_multiplica.append(31)
    if optionM10:
        selected_keys_multiplica_ad.append(32)
        selected_keys_multiplica.append(33)
    if optionM11:
        selected_keys_multiplica_ad.append(34)
        selected_keys_multiplica.append(35)
    if optionM12:
        selected_keys_multiplica_ad.append(36)
        selected_keys_multiplica.append(37)
    if optionM13:
        selected_keys_multiplica_ad.append(38)
        selected_keys_multiplica.append(39)
    if optionM14:
        selected_keys_multiplica_ad.append(40)
        selected_keys_multiplica.append(41)


#----------------------------------------------------------------------------------------------------------

# Container para as operações lidera
with st.container(border = True):
    st.title("Lidera OPS - 2025:")

    # Definindo as colunas para os bimestres
    bimestreLidera1, bimestreLidera2, bimestreLidera3, bimestreLidera4  = st.columns(4)

    with bimestreLidera1:
        st.subheader("FEVEREIRO") 
        optionL1 = st.checkbox(label="04/02/2025 - Check list de auditoria H1 2025 (Todas as operações)", key="optionL1") 
        optionL2 = st.checkbox(label="11/02/2025 - Nova Métrica Inventário (Todas as Operações)", key="optionL2") 
        st.subheader("MARÇO") 
        optionL3 = st.checkbox(label="18/03/2025 - Acompanhamento da Dash de Treinamentos (Todas as Operações)", key="optionL3") 
        st.subheader("ABRIL") 
        optionL4 = st.checkbox(label="14/04/2025 - Como montar um bom plano de ação (Todas as Operações)", key="optionL4") 
        st.subheader("MAIO") 
        optionL5 = st.checkbox(label="05/05/2025 - LIDERA OPS - Check-In e Check-Out (XD CAJ)", key="optionL5") 
        optionL6 = st.checkbox(label="19/05/2025 - 5 's para Liderança (Todas as Operações)", key="optionL6") 


    # Lista para armazenar as chaves selecionadas no container lidera
    selected_keys_lidera = []
    selected_keys_lidera_ad = []

    if optionL1:
        selected_keys_lidera_ad.append(14)
        selected_keys_lidera.append(15)
    if optionL2:
        selected_keys_lidera_ad.append(16)
        selected_keys_lidera.append(17)
    if optionL3:
        selected_keys_lidera_ad.append(18)
        selected_keys_lidera.append(19)
    if optionL4:
        selected_keys_lidera_ad.append(20)
        selected_keys_lidera.append(21)
    if optionL5:
        selected_keys_lidera_ad.append(22)
        selected_keys_lidera.append(23)
    if optionL6:
        selected_keys_lidera_ad.append(24)
        selected_keys_lidera.append(25)

chaves_multiplica, chaves_lidera, chaves_reserva = st.columns(3)
# Exibindo as chaves selecionadas
with chaves_multiplica:
    st.write("Chaves selecionadas no container **Multiplica**:", str(selected_keys_multiplica))
with chaves_lidera:
    st.write("Chaves selecionadas no container **Lidera**:", str(selected_keys_lidera))
with chaves_reserva:
    st.write("")

filter_xd, filter_ag, filter_rv = st.columns(3)
with filter_xd:
    xd_filter = st.checkbox(label="Filtrar somente XD's?")
with filter_ag:
    ag_filter = st.checkbox(label="FIltrar somente agencias?")
with filter_rv:
    rv_filter = st.checkbox(label="Filtrar reversa? (valido para treinamentos somente de reversa)")
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
        modelo = str(df.iloc[i, 11]).strip().upper() # Modelo

        # Caso xd_filter esteja ativo, mantém apenas os que possuem "XD"
        if xd_filter and modelo != "XD":
            continue

        # Caso ag_filter esteja ativo,  excluí apenas os que possuem "XD"
        if ag_filter and modelo == "XD":
            continue      
        
        if rv_filter:
            # Trata vinculo e validação de ausente e  reversa ## and df.iloc[i, 11] == "Reversa Nacional" ## ----------- filtro de logger: df.iloc[i, 6] == "Logger" and 
            if df.iloc[i, 44] != "Sim":
                total_contados = 0
                uns_para_contar = 0
                
                # Iterar sobre todas as colunas
                for j in range(len(df.iloc[i])):
                    value = df.iloc[i, j]
                    if j in selected_keys_multiplica and (value == "0" or value == "1"):
                        total_contados += 1
                        if value == "1":
                            uns_para_contar += 1

                # Iterar sobre todas as colunas para selected_keys_multiplica_ad (capturar médias)
                for j in selected_keys_multiplica_ad:
                    try:
                        value = df.iloc[i, j]
                        
                        # Verificar se a célula está "vazia" (string vazia ou espaços)
                        if pd.isnull(value) or (isinstance(value, str) and value.strip() == ""): #garante que mesmo com a célula com fórmula a mesma será ignorada
                            continue
                        
                        # Tratar valores como strings antes de aplicar replace
                        if isinstance(value, str):
                            value = value.replace('%', '').replace(',', '.')
                        
                        # Converter para float
                        media_value = float(value)
                        medias_base.setdefault(base, []).append(media_value)
                    except ValueError:
                        st.warning(f"Erro ao converter valor '{df.iloc[i, j]}' para float na base {base} - M L{i}, L{j}")
                
                # Armazenar contagem de 1s para a base atual
                uns_contados[base] = uns_contados.get(base, 0) + uns_para_contar
                total_multiplica[base] = total_multiplica.get(base, 0) + total_contados
                
        else:
            #else para quando o botão não for pressionado --------------- filtro de logger df.iloc[i, 6] == "Logger" and 
            if df.iloc[i, 44] != "Sim":
                total_contados = 0
                uns_para_contar = 0
                
                # Iterar sobre todas as colunas
                for j in range(len(df.iloc[i])):
                    value = df.iloc[i, j]
                    if j in selected_keys_multiplica and (value == "0" or value == "1"):
                        total_contados += 1
                        if value == "1":
                            uns_para_contar += 1
                
                # Iterar sobre todas as colunas para selected_keys_multiplica_ad (capturar médias)
                for j in selected_keys_multiplica_ad:
                    try:
                        value = df.iloc[i, j]
                        
                        # Verificar se a célula está "vazia" (string vazia ou espaços)
                        if pd.isnull(value) or (isinstance(value, str) and value.strip() == ""): #garante que mesmo com a célula com fórmula a mesma será ignorada
                            continue
                        
                        # Tratar valores como strings antes de aplicar replace
                        if isinstance(value, str):
                            value = value.replace('%', '').replace(',', '.')
                        
                        # Converter para float
                        media_value = float(value)
                        medias_base.setdefault(base, []).append(media_value)
                    except ValueError:
                        st.warning(f"Erro ao converter valor '{df.iloc[i, j]}' para float na base {base} - M L{i}, L{j}")

                # Armazenar contagem de 1s para a base atual
                uns_contados[base] = uns_contados.get(base, 0) + uns_para_contar
                total_multiplica[base] = total_multiplica.get(base, 0) + total_contados

    # Iterar sobre as linhas da segunda planilha (Lidera OPS)
    for k in range(len(df_lidera)):
        base_lidera = df_lidera.iloc[k, 7]  # Base na coluna H (índice 7)
        modelo_lidera = df_lidera.iloc[k, 11] # Modelo

        # Caso xd_filter esteja ativo, mantém apenas os que possuem "XD"
        if xd_filter and modelo_lidera != "XD":
            continue

        # Caso ag_filter esteja ativo, exclui todos que possuam "XD"
        if ag_filter and modelo_lidera == "XD":
            continue 

        if rv_filter and modelo_lidera == "Reversa Nacional":
            total_contados_lidera = 0
            uns_para_contar_lidera = 0

            # Iterar sobre as colunas relevantes (selected_keys_lidera)
            for l in selected_keys_lidera:
                value_lidera = df_lidera.iloc[k, l]
                if value_lidera in ["0", "1"]:  # Contar apenas valores "0" e "1"
                    total_contados_lidera += 1
                    if value_lidera == "1":
                        uns_para_contar_lidera += 1

            # Capturar médias com selected_keys_lidera_ad
            for l in selected_keys_lidera_ad:
                try:
                    value_lidera = df_lidera.iloc[k, l]
                    if pd.isnull(value_lidera) or (isinstance(value_lidera, str) and value_lidera.strip() == ""):
                        continue

                    if isinstance(value_lidera, str):
                        value_lidera = value_lidera.replace('%', '').replace(',', '.')

                    media_value = float(value_lidera)
                    medias_base_lidera.setdefault(base_lidera, []).append(media_value)
                except ValueError:
                    st.warning(f"Erro ao converter valor '{value_lidera}' para float na base {base_lidera} - Ldr L{k}, C{l}")

            # Atualizar os dicionários de contagem
            lider_uns_contados[base_lidera] = lider_uns_contados.get(base_lidera, 0) + uns_para_contar_lidera
            total_lider[base_lidera] = total_lider.get(base_lidera, 0) + total_contados_lidera


        else: 
            total_contados_lidera = 0
            uns_para_contar_lidera = 0

            # Iterar sobre as colunas relevantes (selected_keys_lidera)
            for l in selected_keys_lidera:
                value_lidera = df_lidera.iloc[k, l]
                if value_lidera in ["0", "1"]:  # Contar apenas valores "0" e "1"
                    total_contados_lidera += 1
                    if value_lidera == "1":
                        uns_para_contar_lidera += 1

            # Capturar médias com selected_keys_lidera_ad
            for l in selected_keys_lidera_ad:
                try:
                    value_lidera = df_lidera.iloc[k, l]
                    if pd.isnull(value_lidera) or (isinstance(value_lidera, str) and value_lidera.strip() == ""):
                        continue

                    if isinstance(value_lidera, str):
                        value_lidera = value_lidera.replace('%', '').replace(',', '.')

                    media_value = float(value_lidera)
                    medias_base_lidera.setdefault(base_lidera, []).append(media_value)
                except ValueError:
                    st.warning(f"Erro ao converter valor '{value_lidera}' para float na base {base_lidera} - Ldr L{k}, C{l}")

            # Atualizar os dicionários de contagem
            lider_uns_contados[base_lidera] = lider_uns_contados.get(base_lidera, 0) + uns_para_contar_lidera
            total_lider[base_lidera] = total_lider.get(base_lidera, 0) + total_contados_lidera

    # Após o processamento, calcule as médias finais
    medias_finais_base = {base: sum(medias)/len(medias) for base, medias in medias_base.items()}
    medias_finais_lidera = {base: sum(medias) / len(medias) for base, medias in medias_base_lidera.items() if len(medias) > 0}

    # Exibir resultados em um único DataFrame
    combined_results = pd.DataFrame({
        "Base": list(set(uns_contados.keys()).union(set(lider_uns_contados.keys()))),
        "Planejado - Multiplicadores": [total_multiplica.get(base, 0) for base in list(set(uns_contados.keys()).union(set(lider_uns_contados.keys())))],
        "Realizado - Multiplicadores": [uns_contados.get(base, 0) for base in list(set(uns_contados.keys()).union(set(lider_uns_contados.keys())))],
        "Aderência Multiplicador": [f"0,{medias_finais_base.get(base, 0):.2f}".replace('.', '') for base in list(set(uns_contados.keys()).union(set(lider_uns_contados.keys())))],
        "Planejado - Líderes": [total_lider.get(base, 0) for base in list(set(uns_contados.keys()).union(set(lider_uns_contados.keys())))],
        "Realizado - Líderes": [lider_uns_contados.get(base, 0) for base in list(set(uns_contados.keys()).union(set(lider_uns_contados.keys())))],
        "Aderência Líderes": [f"0,{medias_finais_lidera.get(base, 0):.2f}".replace('.', '') for base in list(set(uns_contados.keys()).union(set(lider_uns_contados.keys())))]
    })

    st.subheader("Resultado da Presença aos cursos escolhidos:")
    st.dataframe(combined_results, width=1400)

