import streamlit as st
import pandas as pd
import webbrowser

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= 2023] #Apena jogadores com contrato válido até 2023
    df_data = df_data[df_data["Value(£)"] > 0] #Apenas jogadores com valor maior que 0
    df_data = df_data.sort_values(by="Overall", ascending=False) #Ordena por Overall
    st.session_state["data"] = df_data

st.markdown("# FIFA23 OFFICIAL DATASET! ⚽️")
st.sidebar.markdown("Desenvolvido por Nelson na aula da [ASIMOV ACADEMY](https://www.asimovacademy.com.br/)")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset")

st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações
    abrangentes sobre jogadores profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluido dados demográficos
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e
    afiliações de clubes.
    """
)

# streamlit run 1_🏠_Home.py