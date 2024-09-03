import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Menu de Funções", 
                   page_icon="🛠️", 
                   layout="wide"                   
                )

with st.sidebar:
    st.write()
    
st.write('Gestão da Qualidade')
st.title('Menu de Funções')
#components.iframe(meuArquivoGsheets)
st.write("Utilize qualquer um dos menus ao lado para executar aquilo que deseja.")
st.write("Atente-se que, para cada página ou função que for realizar " +
         "haverá um passo a passo do que se deve fazer.")
st.write("Ao lado você poderá ver as principais automações de processos geralmente manuais, " + 
         "que tiveram por necessidade o uso de script para encurtar seus processos!")
st.write("Qualquer dúvida fale comigo: johnatas.eugenio@loggi.com")

st.title("Scripts e suas relações:")

st.subheader("Capturar por Aderência:")
st.write("**Planilha base:** [EDUCA Loggi _Matriz - Treinamentos H2](https://docs.google.com/spreadsheets/d/1zw56-hBt4JNdBoM5s5TOUNJazSfmmmAwbX5jZacw-Fc/edit?usp=sharing)")
st.write("**Propósito:** Capturar os colaboradeores com taxa inferior a 80% nos treinamentos")

st.subheader("Dados para o BSC: ")
st.write("**Planilha base:** [EDUCA Loggi _Matriz - Treinamentos H2](https://docs.google.com/spreadsheets/d/1zw56-hBt4JNdBoM5s5TOUNJazSfmmmAwbX5jZacw-Fc/edit?usp=sharing)")
st.write("**Propósito:** Fornecer os Planejados e Realizados de cada base referente aos cursos aplicados")

