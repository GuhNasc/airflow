# POETRY ADD STREAMLIT PANDAS
import streamlit as st 
import pandas as pd
import subprocess

# Funçao para carregar arquivos csv
def load_data():
    df= pd.read_csv("logging.log")
    return df 


# Função para executar o script
def executa_script():
    subprocess.run("poetry run python pipeline/pipeline.py")


# Layout arquivo do streamlit
def main():
    st.title("Visualização de Logs e Executação dos scripts")
    

    # carregar dados do csv
    df = load_data()

    #exibe os dados na interface
    st.write("Logs de execução:", df)

    # Botão para atualizar os dados
    if st.button("Atualizar Dados"):
        df = load_data()
        st.write("Dados atualizados com sucesso")
    
    # Botão para executar o script python
    if st.button("Rodar Script"):
        executa_script()
        st.write("Script finalizado com sucesso")

if __name__ == "__main__":
    main()
