# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie todo o código da aplicação para o diretório de trabalho
COPY app/ /app

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o arquivo de requisitos para instalar as dependências
#COPY requirements.txt requirements.txt

# Exponha a porta usada pelo Streamlit
EXPOSE 8501

# Comando para rodar o Streamlit quando o contêiner for iniciado
CMD ["streamlit", "run", "1_🏠_Home.py"]
