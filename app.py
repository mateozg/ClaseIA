import pandas as pd
import streamlit as st


st.set_page_config(page_title="NBA Dashboard", page_icon="🏀", layout="wide")

st.title("NBA Dashboard Basico")
st.caption("Dashboard simple con datos simulados de ejemplo.")

teams = pd.DataFrame(
    {
        "Equipo": ["Lakers", "Celtics", "Warriors", "Bulls", "Heat"],
        "Victorias": [48, 52, 44, 39, 45],
        "Derrotas": [34, 30, 38, 43, 37],
        "Puntos por partido": [112.4, 115.1, 113.0, 108.2, 110.7],
    }
)

col1, col2, col3 = st.columns(3)
col1.metric("Equipos", len(teams))
col2.metric("Mejor equipo", teams.loc[teams["Victorias"].idxmax(), "Equipo"])
col3.metric("Promedio PPG", f'{teams["Puntos por partido"].mean():.1f}')

st.subheader("Tabla de equipos")
st.dataframe(teams, use_container_width=True, hide_index=True)

st.subheader("Victorias por equipo")
st.bar_chart(teams.set_index("Equipo")["Victorias"])

st.subheader("Detalle rapido")
team = st.selectbox("Selecciona un equipo", teams["Equipo"].tolist())
selected = teams[teams["Equipo"] == team].iloc[0]

detail_col1, detail_col2, detail_col3 = st.columns(3)
detail_col1.metric("Victorias", int(selected["Victorias"]))
detail_col2.metric("Derrotas", int(selected["Derrotas"]))
detail_col3.metric("Puntos por partido", f'{selected["Puntos por partido"]:.1f}')

st.write("Hecho para subir a GitHub y correr con `streamlit run app.py`.")