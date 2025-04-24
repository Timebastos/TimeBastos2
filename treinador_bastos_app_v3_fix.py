
import streamlit as st
import datetime

st.set_page_config(page_title="Treinador Bastos", layout="centered")
st.title("Treinador Bastos - Prescrição Quinzenal")

st.header("📆 Prescrição Semanal Baseada em Ciclos")

# Ciclos definidos
tipo_macro = st.selectbox("Macrociclo em andamento:", ["Linear", "Ondulatório", "Blocos", "Polarizado", "Contemporâneo"])
tipo_meso = st.selectbox("Mesociclo atual:", ["Base", "Desenvolvimento", "Choque", "Competitivo", "Tapering"])
tipo_micro = st.selectbox("Microciclo da semana:", ["Adaptação", "Carga", "Estável", "Choque", "Recuperação", "Polimento"])

st.markdown(f"🔄 **Plano quinzenal em andamento:**")
st.markdown(f"**Macrociclo:** {tipo_macro} | **Mesociclo:** {tipo_meso} | **Microciclo:** {tipo_micro}")

# Seleção de sessões da semana
st.subheader("🗓️ Semana Atual - Escolha das Sessões")
dias_disponiveis = st.slider("Quantos dias essa semana o atleta pode treinar?", 2, 7, 4)

sessoes = []
for i in range(1, dias_disponiveis + 1):
    treino = st.selectbox(f"Sessão do Dia {i}:", [
        "Corrida intervalada leve",
        "Corrida contínua Z2",
        "Técnica de corrida + mobilidade",
        "Força funcional",
        "Cross training (bike leve)",
        "Longão leve com foco em respiração",
        "Regenerativo + mobilidade",
        "Tempo run moderado",
        "Tiros curtos (Z5)",
        "Descanso / opcional bike leve"
    ], key=f"sessao_{i}")
    sessoes.append(treino)

# Controle de estados
if 'prescricao_confirmada' not in st.session_state:
    st.session_state.prescricao_confirmada = False

if st.button("✅ Confirmar Prescrição da Semana"):
    st.session_state.prescricao_confirmada = True
    st.success("Prescrição confirmada! Sessões registradas com sucesso.")

if st.session_state.prescricao_confirmada:
    if st.button("📤 Liberar Plano para o Atleta"):
        st.success("Plano liberado! O atleta já pode visualizar sua semana de treinos.")
        st.subheader("📋 Plano da Semana")
        for idx, sessao in enumerate(sessoes):
            st.markdown(f"- **Dia {idx + 1}:** {sessao}")
