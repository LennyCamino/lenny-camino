from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
import pandas as pd
from datetime import datetime, timedelta

# Cargar claves del archivo .env
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
google_maps_key = os.getenv("GOOGLE_MAPS_API_KEY")
weather_key = os.getenv("WEATHER_API_KEY")
booking_key = os.getenv("BOOKING_API_KEY")

# Comprobamos que las claves existen
print("OPENAI_API_KEY:", openai_api_key[:5] + "..." if openai_api_key else "❌ No encontrada")
print("GOOGLE_MAPS_API_KEY:", google_maps_key[:5] + "..." if google_maps_key else "❌ No encontrada")
print("WEATHER_API_KEY:", weather_key[:5] + "..." if weather_key else "❌ No encontrada")
print("BOOKING_API_KEY:", booking_key[:5] + "..." if booking_key else "❌ No encontrada")

# Leer hoja de ruta desde archivo Excel
try:
    ruta_df = pd.read_excel("camino_etapas_limpio_FINAL.xlsx")
    print("\n📋 Etapas cargadas desde el Excel:")
    print(ruta_df.head())  # Muestra las primeras filas

    # Generamos las fechas desde el 5 de mayo de 2025, una por etapa
    fecha_inicio = datetime(2025, 5, 5)
    ruta_df['Fecha'] = [fecha_inicio + timedelta(days=i) for i in range(len(ruta_df))]

    # Fecha actual del sistema
    hoy = datetime.now().date()

    # Buscar la etapa del día
    etapa_hoy = ruta_df[ruta_df['Fecha'].dt.date == hoy]

    if not etapa_hoy.empty:
        etapa_actual = etapa_hoy.iloc[0]
        print(f"\n📍 Hoy es la etapa {etapa_actual['Etapa']}: {etapa_actual['Localidad']}")
        print(f"Distancia estimada: {etapa_actual['Distancia_km']} km")
        print(f"Notas: {etapa_actual['Notas']}")

    else:
        print("\n⏳ Hoy no hay etapa programada (antes de empezar o ya finalizado el Camino).")

except Exception as e:
    print("❌ Error al leer el archivo Excel:", e)

# Iniciar el modelo
chat = ChatOpenAI(api_key=openai_api_key, model="gpt-4")

# Saludo de activación
mensaje = """
Hola, soy Fernando y acabo de activar por primera vez mi agente inteligente para el Camino de Santiago.
Por favor, preséntate como un guía estoico y simpático que me acompañará durante el camino.
"""
respuesta = chat.invoke(mensaje)
print("\n👣 Respuesta del agente:\n")
print(respuesta)
