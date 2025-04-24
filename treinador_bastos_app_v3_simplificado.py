
import streamlit as st

st.set_page_config(page_title="Treinador Bastos", layout="centered")
st.title("Treinador Bastos - Semana de Treino")

st.header("📌 Ciclos Definidos")
tipo_macro = st.selectbox("Macrociclo:", ["Linear", "Ondulatório", "Blocos", "Polarizado", "Contemporâneo"])
tipo_meso = st.selectbox("Mesociclo:", ["Base", "Desenvolvimento", "Choque", "Competitivo", "Tapering"])
tipo_micro = st.selectbox("Microciclo:", ["Adaptação", "Carga", "Estável", "Choque", "Recuperação", "Polimento"])

st.divider()

st.header("🗓️ Sessões da Semana")
qtd_dias = st.slider("Dias de treino disponíveis:", 2, 7, 4)

treinos = []
for dia in range(1, qtd_dias + 1):
    sessao = st.selectbox(
        f"Sessão do Dia {dia}",
        [
            "Corrida intervalada leve",
            "Corrida contínua Z2",
            "Técnica + mobilidade",
            "Força funcional",
            "Cross training (bike leve)",
            "Longão respiratório",
            "Regenerativo leve",
            "Tempo run moderado",
            "Tiros curtos Z5",
            "Descanso ou bike leve"
        ],
        key=f"treino_{dia}"
    )
    treinos.append(sessao)

if st.button("📋 Ver Plano da Semana"):
    st.success("Plano gerado com sucesso!")
    st.subheader("📌 Treinos Selecionados")
    for i, treino in enumerate(treinos, 1):
        st.markdown(f"**Dia {i}:** {treino}")
