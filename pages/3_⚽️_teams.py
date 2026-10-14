import streamlit as st
import requests
import base64

@st.cache_data
def load_image_64(url):
    #headers = {"User-Agent": "Mozilla/5.0"}
    headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/131.0.0.0 Safari/537.36"
    ),
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    }  
    headers["Referer"] = "https://sofifa.com/"
    data = requests.get(url, headers=headers).content
    return "data:image/png;base64," + base64.b64encode(data).decode()

def preprocess_row(url):
    if isinstance(url, str) and url.startswith("http"):
        return load_image_64(url)
    return url

st.set_page_config(
    page_title="Teams",
    page_icon="⚽️",
    layout="wide"
)

df_data = st.session_state["data"]

# Filtro Clube
clubes = df_data["Club"].unique() # Define lista de clubes únicos
club = st.sidebar.selectbox("Clube", clubes) # Cria o selectbox com os clubes únicos, retorno variável club

df_filtered = df_data[df_data["Club"] == club].set_index("Name")

df_filtered["Photo"] = df_filtered["Photo"].apply(preprocess_row)
df_filtered["Flag"] = df_filtered["Flag"].apply(preprocess_row)
df_filtered["Club Logo"] = df_filtered["Club Logo"].apply(preprocess_row)

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}") # O curioso é oque o ## deixa em titulo 2

columns = ["Age", "Photo","Flag","Overall","Value(£)","Wage(£)","Joined","Height(cm.)","Weight(lbs.)","Contract Valid Until","Release Clause(£)"]

st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall",
                     help="Overall do jogador",
                     format="%d",
                     min_value=0,
                     max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage",format="£%f",
                                                            min_value=0,max_value=df_filtered["Wage(£)"].max()),
                "Photo": st.column_config.ImageColumn("Photo", help="Foto do jogador"),
                "Flag": st.column_config.ImageColumn("Flag", help="Bandeira do país"),
                 })