
import streamlit as st
import datetime

st.set_page_config(page_title="Treinador Bastos - Avaliação", layout="wide")
st.title("🏃 Treinador Bastos - Avaliação e Prescrição")

if 'historico_planilhas' not in st.session_state:
    st.session_state.historico_planilhas = []

st.header("📋 Avaliação e Parâmetros do Atleta")

tipo_macro = st.selectbox("Macrociclo:", ["Linear", "Ondulatório", "Blocos", "Polarizado", "Contemporâneo"])
tipo_meso = st.selectbox("Mesociclo:", ["Base", "Desenvolvimento", "Choque", "Competitivo", "Tapering"])
tipo_micro = st.selectbox("Microciclo:", ["Adaptação", "Carga", "Estável", "Choque", "Recuperação", "Polimento"])
nivel_atleta = st.selectbox("Nível do atleta:", ["Iniciante", "Intermediário", "Avançado", "Elite"])

vam = st.number_input("VAM estimada (km/h):", min_value=8.0, max_value=25.0, step=0.1)
vo2 = st.number_input("VO₂máx estimado (ml/kg/min):", min_value=30.0, max_value=90.0, step=0.1)
fcmax = st.number_input("Frequência Cardíaca Máxima estimada (bpm):", min_value=140, max_value=220)
base_ritmo = st.selectbox("Base preferida para ritmo:", ["VAM", "VO₂máx", "Frequência Cardíaca"])

st.header("⚙️ Geração Automática da Semana")

data_inicio = st.date_input("Data de início da semana de treino")
dias_disponiveis = st.slider("Dias de treino disponíveis:", 2, 7, 4)

volume_anterior = st.session_state.historico_planilhas[-1]['volume'] if st.session_state.historico_planilhas else 60
progresso = {"Iniciante": 1.10, "Intermediário": 1.15, "Avançado": 1.18, "Elite": 1.20}
volume_alvo = round(volume_anterior * progresso[nivel_atleta])
st.markdown(f"🎯 Volume alvo: **{volume_alvo} min**")

banco = [
    {"tipo": "Regenerativo", "intensidade": "Leve", "duracao": 30},
    {"tipo": "Corrida contínua Z2", "intensidade": "Leve", "duracao": 40},
    {"tipo": "Técnica + mobilidade", "intensidade": "Leve", "duracao": 20},
    {"tipo": "Tempo run", "intensidade": "Moderado", "duracao": 30},
    {"tipo": "Intervalado curto", "intensidade": "Forte", "duracao": 25},
    {"tipo": "Intervalado longo", "intensidade": "Forte", "duracao": 35},
    {"tipo": "Cross training (bike leve)", "intensidade": "Leve", "duracao": 40},
    {"tipo": "Força funcional", "intensidade": "Moderado", "duracao": 30},
    {"tipo": "Longão", "intensidade": "Moderado", "duracao": 60}
]

sugestoes, total = [], 0
for i in range(dias_disponiveis):
    for t in banco:
        if total + t['duracao'] <= volume_alvo:
            sugestoes.append(t)
            total += t['duracao']
            break

st.subheader("📋 Treinos sugeridos")
treinos_formatados = []
for i, t in enumerate(sugestoes):
    if base_ritmo == "VAM":
        ritmo = round(60 / (vam * (0.6 if t['intensidade'] == 'Leve' else 0.75 if t['intensidade'] == 'Moderado' else 0.9)), 2)
    elif base_ritmo == "VO₂máx":
        ritmo = round(3000 / (vo2 * (0.6 if t['intensidade'] == 'Leve' else 0.75 if t['intensidade'] == 'Moderado' else 0.9)), 2)
    else:
        faixa = (int(fcmax * (0.6 if t['intensidade'] == 'Leve' else 0.75)), int(fcmax * (0.7 if t['intensidade'] == 'Leve' else 0.85)))
        ritmo = f"{faixa[0]}–{faixa[1]} bpm"
    treinos_formatados.append({"tipo": t["tipo"], "duracao": t["duracao"], "intensidade": t["intensidade"], "ritmo": ritmo})
    st.markdown(f"- **Dia {i+1}:** {t['tipo']} – {t['duracao']} min – {t['intensidade']} – Ritmo: {ritmo}")

if st.button("✅ Confirmar Plano"):
    plano = {
        "data_inicio": str(data_inicio),
        "macrociclo": tipo_macro,
        "mesociclo": tipo_meso,
        "microciclo": tipo_micro,
        "nivel": nivel_atleta,
        "vam": vam,
        "vo2": vo2,
        "fcmax": fcmax,
        "base_ritmo": base_ritmo,
        "volume": total,
        "treinos": treinos_formatados
    }
    st.session_state.historico_planilhas.append(plano)
    st.success("Plano salvo com sucesso!")
