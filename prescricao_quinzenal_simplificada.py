
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Treinador Bastos - Prescrição Quinzenal", layout="wide")
st.title("📆 Prescrição Quinzenal Simples")

# Prova-alvo
st.header("🏁 Prova-Alvo")
data_prova = st.date_input("Data da prova")
distancia = st.text_input("Distância da prova (ex: 7km, 21k trail, etc.)")
data_hoje = datetime.today().date()
semanas_ate_prova = (data_prova - data_hoje).days // 7
if semanas_ate_prova <= 0:
    st.warning("A data da prova deve estar no futuro.")
    st.stop()

st.success(f"Faltam **{semanas_ate_prova} semanas** até a prova de {distancia}.")

# Feedback simples
st.header("📋 Feedback da Quinzena Anterior")
volume = st.slider("Volume total realizado (min)", 0, 300, 90, step=10)
rpe = st.slider("RPE médio (0 = fácil | 10 = exaustivo)", 0, 10, 5)
sono = st.slider("Qualidade do sono", 1, 5, 3)
fadiga = st.slider("Fadiga muscular", 1, 5, 3)
humor = st.slider("Humor geral", 1, 5, 3)

ajuste = "Manter"
if volume < 80 or rpe >= 8 or (sono <= 2 and fadiga >= 4):
    ajuste = "Reduzir"
elif rpe <= 3 and volume >= 100:
    ajuste = "Aumentar"

st.subheader(f"🔁 Ajuste sugerido: **{ajuste} carga**")

# Microciclos
if ajuste == "Reduzir":
    micro1, micro2 = "Recuperação", "Estável"
elif ajuste == "Aumentar":
    micro1, micro2 = "Carga", "Choque"
else:
    micro1, micro2 = "Estável", "Carga"

# Banco simplificado
banco = {
    "Adaptação": ["20min caminhada + 10min trote leve", "3x(3min trote + 2min cam)", "Técnica + 15min leve"],
    "Estável": ["30min Z2 contínuo", "4x(4min leve/mod + 1min)", "Mobilidade + 25min leve"],
    "Carga": ["40min contínuo mod", "5x(5min forte + 2min)", "Técnica + 30min ritmo"],
    "Choque": ["45min contínuo Z3", "6x(4min forte + 1min)", "Força leve + corrida"],
    "Recuperação": ["20min leve + mobilidade", "2x(3min trote + 2min)", "30min bike ou trote leve"],
    "Polimento": ["25min progressiva", "3x(3min moderado + 1min)", "15min + 5 acelerações"]
}

# Exibir treinos
st.header("📋 Treinos da Quinzena")
for i, micro in enumerate([micro1, micro2]):
    st.subheader(f"Semana {i+1} - {micro}")
    for treino in banco[micro]:
        st.markdown(f"- {treino}")
