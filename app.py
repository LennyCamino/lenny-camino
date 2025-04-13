import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Lenny - Camino Portugués", layout="centered")

# 🌄 Bienvenida espiritual
st.title("🕊️ Bienvenido al Camino con Lenny")
st.markdown("""
> *“No se trata del destino, sino del viaje.”*  
>  
> Soy **Lenny**, tu guía estoico y simpático.  
> Estoy aquí para ayudarte en tu camino hacia Santiago.  
>  
> Cada día te mostraré la etapa que corresponde, junto con notas útiles, consejos, y un poco de paz interior.  
""")

# 📅 Fecha actual
hoy = datetime.now().date()
st.markdown(f"📆 **Hoy es:** `{hoy.strftime('%d de %B de %Y')}`")

# 📘 Cargar hoja de ruta
try:
    df = pd.read_excel("camino_etapas_limpio.xlsx")
    fecha_inicio = datetime(2025, 5, 5).date()
    df["Fecha"] = [fecha_inicio + timedelta(days=i) for i in range(len(df))]
    
    etapa_hoy = df[df["Fecha"] == hoy]

    if not etapa_hoy.empty:
        st.success("📍 **Etapa del día**:")
        etapa = etapa_hoy.iloc[0]
        st.markdown(f"""
        ### Etapa {etapa['Etapa']} – {etapa['Localidad']}
        - 🛣️ **Distancia estimada**: {etapa['Distancia_km']} km  
        - 📝 **Notas**:  
        {etapa['Notas']}
        """)
    else:
        st.warning("⏳ Hoy no hay etapa programada.\n\nDescansa cuerpo y alma.")

except Exception as e:
    st.error("❌ No se pudo cargar la hoja de ruta.")
    st.text(str(e))

# 🧘‍♂️ Frase estoica diaria (simulada por ahora)
frases = [
    "A quien no le basta con poco, nada le basta. — Epicuro",
    "La dificultad muestra lo que los hombres son. — Epicteto",
    "Acepta lo que no puedes cambiar, actúa sobre lo que sí. — Marco Aurelio"
]

st.markdown("---")
st.markdown(f"🧘 *Frase para reflexionar hoy:*  \n> *{frases[hoy.day % len(frases)]}*")

st.markdown("---")
st.caption("Creado con 🤍 por LennyCamino - Powered by ChatGPT & Streamlit")
