
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Treinador Bastos - App Integrado", layout="wide")
st.sidebar.title("Menu")
pagina = st.sidebar.radio("Navegação", ["Triagem", "Prova-Alvo", "Prescrição Quinzenal", "Feedback e Histórico"])

# Banco de treinos simplificado
banco = {
    "Adaptação": ["20min caminhada + 10min trote leve", "3x(3min trote + 2min cam)", "Técnica + 15min leve"],
    "Estável": ["30min Z2 contínuo", "4x(4min leve/mod + 1min)", "Mobilidade + 25min leve"],
    "Carga": ["40min contínuo mod", "5x(5min forte + 2min)", "Técnica + 30min ritmo"],
    "Choque": ["45min contínuo Z3", "6x(4min forte + 1min)", "Força leve + corrida"],
    "Recuperação": ["20min leve + mobilidade", "2x(3min trote + 2min)", "30min bike ou trote leve"],
    "Polimento": ["25min progressiva", "3x(3min moderado + 1min)", "15min + 5 acelerações"]
}

if pagina == "Triagem":
    st.title("📋 Triagem do Atleta")
    nome = st.text_input("Nome")
    idade = st.number_input("Idade", 10, 100)
    peso = st.number_input("Peso (kg)", 30.0, 200.0)
    atividade = st.selectbox("Pratica outra atividade?", ["Não", "1-2x/semana", "3+ vezes"])
    corrida = st.selectbox("Já corre/trota?", ["Não", "Com pausas", "Contínuo"])
    tempo = st.selectbox("Tempo de prática", ["Nunca", "< 3 meses", "3-12 meses", "> 1 ano"])
    freq = st.selectbox("Frequência semanal", ["Nenhuma", "1-2x", "3+ vezes"])
    provas = st.selectbox("Participou de provas?", ["Nunca", "Por experiência", "Busca performance"])
    objetivo = st.text_input("Objetivo")

    pontos = 0
    if atividade == "3+ vezes": pontos += 1
    if corrida == "Contínuo": pontos += 1
    if tempo == "3-12 meses": pontos += 1
    if tempo == "> 1 ano": pontos += 2
    if freq == "3+ vezes": pontos += 1
    if provas == "Busca performance": pontos += 2
    elif provas == "Por experiência": pontos += 1

    if pontos <= 2: perfil = "Iniciante Sedentário"
    elif pontos <= 4: perfil = "Iniciante Ativo"
    elif pontos <= 6: perfil = "Intermediário"
    elif pontos <= 7: perfil = "Avançado"
    else: perfil = "Elite"

    st.success(f"Perfil: {perfil}")
    st.session_state.perfil = perfil

elif pagina == "Prova-Alvo":
    st.title("🎯 Planejamento pela Prova-Alvo")
    data_prova = st.date_input("Data da prova")
    distancia = st.text_input("Distância da prova")
    hoje = datetime.today().date()
    semanas = (data_prova - hoje).days // 7
    st.success(f"Faltam {semanas} semanas até {distancia}")

    if semanas <= 8: meso = ["Base", "Choque", "Competitivo"]
    elif semanas <= 12: meso = ["Adaptação", "Base", "Desenvolvimento", "Choque", "Polimento"]
    else: meso = ["Adaptação", "Base", "Desenvolvimento", "Desenvolvimento", "Choque", "Competitivo", "Polimento"]

    base = []
    div, resto = divmod(semanas, len(meso))
    for i, m in enumerate(meso):
        n = div + (1 if i < resto else 0)
        base.extend([m] * n)

    semana_atual = st.number_input("Semana atual:", 1, semanas)
    st.info(f"Mesociclo atual: {base[semana_atual - 1]}")
    st.session_state.meso = base[semana_atual - 1]

elif pagina == "Prescrição Quinzenal":
    st.title("📆 Prescrição Quinzenal")

    volume = st.slider("Volume total realizado (min)", 0, 300, 90, 10)
    rpe = st.slider("RPE médio", 0, 10, 5)
    sono = st.slider("Sono", 1, 5, 3)
    fadiga = st.slider("Fadiga", 1, 5, 3)
    humor = st.slider("Humor", 1, 5, 3)

    ajuste = "Manter"
    if volume < 80 or rpe >= 8 or (sono <= 2 and fadiga >= 4): ajuste = "Reduzir"
    elif rpe <= 3 and volume >= 100: ajuste = "Aumentar"

    st.subheader(f"Ajuste sugerido: {ajuste}")

    if ajuste == "Reduzir": micro1, micro2 = "Recuperação", "Estável"
    elif ajuste == "Aumentar": micro1, micro2 = "Carga", "Choque"
    else: micro1, micro2 = "Estável", "Carga"

    st.header("📋 Treinos")
    for i, m in enumerate([micro1, micro2]):
        st.subheader(f"Semana {i+1}: {m}")
        for treino in banco[m]:
            st.markdown(f"- {treino}")

elif pagina == "Feedback e Histórico":
    st.title("📚 Histórico (simulado)")
    if "perfil" in st.session_state:
        st.markdown(f"**Último perfil avaliado:** {st.session_state.perfil}")
    if "meso" in st.session_state:
        st.markdown(f"**Último mesociclo ativo:** {st.session_state.meso}")
    st.info("Histórico completo será integrado com persistência em breve.")
