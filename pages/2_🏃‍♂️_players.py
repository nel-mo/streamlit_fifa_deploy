import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃‍♂️",
    layout="wide"
)

df_data = st.session_state["data"]

# Filtro Clube
clubes = df_data["Club"].unique() # Define lista de clubes únicos
club = st.sidebar.selectbox("Clube", clubes) # Cria o selectbox com os clubes únicos, retorno variável club

# Filtro Jogador
df_players = df_data[(df_data["Club"] == club)]
players = df_players["Name"].unique() # Define lista de jogadores únicos do clube selecionado
player = st.sidebar.selectbox("Jogador", players) # Cria o selectbox com os jogadores únicos do clube selecionado, retorno variável player

player_stats = df_data[df_data["Name"] == player].iloc[0]

#st.image(player_stats["Photo"])
st.image("https://publish.realmadrid.com/content/dam/portals/realmadrid-com/es-es/sports/football/legendary-players/cristiano-ronaldo-dos-santos-aveiro/assets/1330603286208.jpg")
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura[m]:** {player_stats['Height(cm.)']/100}")
col3.markdown(f"**Peso[kg]:** {player_stats['Weight(lbs.)']*0.45359237:.2f}")

st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1,col2,col3,col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"{player_stats['Value(£)']:,} £")
col2.metric(label="Remuneração Semanal", value=f"{player_stats['Wage(£)']:,} £")
col3.metric(label="Cláusula de rescisão", value=f"{player_stats['Release Clause(£)']:,} £")
