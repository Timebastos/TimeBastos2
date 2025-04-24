
import streamlit as st

st.set_page_config(page_title="Treinador Bastos - Iniciantes", layout="wide")
st.title("🏃 Plataforma de Prescrição - Iniciantes")

st.header("📋 Triagem Inicial do Atleta")

nome = st.text_input("Nome completo do atleta")
idade = st.number_input("Idade", min_value=10, max_value=100, step=1)
peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, step=0.1)
atividade = st.selectbox("Você pratica alguma outra atividade física?", ["Não", "Sim, 1 a 2x por semana", "Sim, 3 ou mais vezes por semana"])
corrida = st.selectbox("Você já corre ou trota atualmente?", ["Não", "Sim, mas com pausas", "Sim, de forma contínua"])
tempo_correndo = st.selectbox("Há quanto tempo você pratica corrida?", ["Nunca corri", "Menos de 3 meses", "Mais de 3 meses"])
frequencia = st.selectbox("Quantas vezes por semana você costuma correr?", ["Nenhuma", "1 a 2 vezes", "3 ou mais vezes"])
objetivo = st.text_input("Qual o seu principal objetivo com a corrida?")

# Cálculo automático do perfil e ciclos
pontos = 0
if atividade == "Sim, 3 ou mais vezes por semana":
    pontos += 2
elif atividade == "Sim, 1 a 2x por semana":
    pontos += 1

if corrida == "Sim, de forma contínua":
    pontos += 2
elif corrida == "Sim, mas com pausas":
    pontos += 1

if tempo_correndo == "Mais de 3 meses":
    pontos += 2
elif tempo_correndo == "Menos de 3 meses":
    pontos += 1

if frequencia == "3 ou mais vezes":
    pontos += 2
elif frequencia == "1 a 2 vezes":
    pontos += 1

# Classificação final
if pontos <= 2:
    perfil = "Iniciante Sedentário"
elif pontos <= 4:
    perfil = "Iniciante Ativo"
else:
    perfil = "Iniciante Avançado"

macrociclo = "Linear"
mesociclo = "Adaptação"
microciclo = "Adaptação"

if perfil == "Iniciante Avançado":
    mesociclo = "Base"
    microciclo = "Estável"

# Banco de treinos iniciais
banco = {
    "Adaptação": [
        {"tipo": "Caminhada + trote leve", "duracao": 25, "intensidade": "Leve"},
        {"tipo": "Trote leve + caminhada (intervalado)", "duracao": 30, "intensidade": "Leve"},
        {"tipo": "Mobilidade e técnica + 15min leve", "duracao": 20, "intensidade": "Leve"}
    ],
    "Estável": [
        {"tipo": "Corrida contínua leve 25min", "duracao": 25, "intensidade": "Leve"},
        {"tipo": "Intervalado curto (2x4min leve) + caminhada", "duracao": 30, "intensidade": "Moderado"},
        {"tipo": "Técnica + corrida 20min contínua", "duracao": 25, "intensidade": "Leve"}
    ]
}

volume_total = 0
semana = banco[microciclo][:]
for t in semana:
    volume_total += t['duracao']

if st.button("📤 Confirmar e Gerar Plano"):
    st.success(f"Perfil identificado: {perfil}")
    st.markdown(f"**Macrociclo sugerido:** {macrociclo}")
    st.markdown(f"**Mesociclo inicial:** {mesociclo}")
    st.markdown(f"**Microciclo da semana:** {microciclo}")
    st.markdown(f"**Objetivo:** {objetivo}")
    st.markdown(f"**Idade:** {idade} anos | Peso: {peso} kg")
    st.divider()
    st.subheader("📋 Plano de Treino da Semana")
    for i, treino in enumerate(semana):
        st.markdown(f"- Dia {i+1}: {treino['tipo']} – {treino['duracao']} min – Intensidade: {treino['intensidade']}")
    st.markdown(f"**Volume total planejado:** {volume_total} minutos")
