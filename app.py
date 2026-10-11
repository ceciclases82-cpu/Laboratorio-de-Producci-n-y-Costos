from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Laboratorio de Producción y Costos",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Quita márgenes de Streamlit para que el simulador ocupe toda la pantalla
st.markdown(
    """
    <style>
      .block-container {padding: 0 !important; max-width: 100% !important;}
      header[data-testid="stHeader"], footer {display: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "laboratorio.html").read_text(encoding="utf-8")
components.html(html, height=1000, scrolling=True)
