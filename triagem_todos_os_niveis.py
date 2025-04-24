
import streamlit as st

st.set_page_config(page_title="Treinador Bastos - Prescrição Completa", layout="wide")
st.title("🏃 Plataforma de Prescrição - Todos os Níveis")

st.header("📋 Triagem Inicial do Atleta")

nome = st.text_input("Nome completo do atleta")
idade = st.number_input("Idade", min_value=10, max_value=100, step=1)
peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, step=0.1)
atividade = st.selectbox("Você pratica alguma outra atividade física?", ["Não", "Sim, 1 a 2x por semana", "Sim, 3 ou mais vezes por semana"])
corrida = st.selectbox("Você já corre ou trota atualmente?", ["Não", "Sim, mas com pausas", "Sim, de forma contínua"])
tempo_correndo = st.selectbox("Há quanto tempo você pratica corrida?", ["Nunca corri", "Menos de 3 meses", "3 a 12 meses", "Mais de 1 ano"])
frequencia = st.selectbox("Quantas vezes por semana você costuma correr?", ["Nenhuma", "1 a 2 vezes", "3 ou mais vezes"])
provas = st.selectbox("Você já participou de provas?", ["Nunca", "Já participei por experiência", "Sim, busco melhorar meu tempo"])
objetivo = st.text_input("Qual o seu principal objetivo com a corrida?")

# Cálculo automático do perfil
pontos = 0
if atividade == "Sim, 3 ou mais vezes por semana": pontos += 1
if corrida == "Sim, de forma contínua": pontos += 1
if tempo_correndo == "3 a 12 meses": pontos += 1
if tempo_correndo == "Mais de 1 ano": pontos += 2
if frequencia == "3 ou mais vezes": pontos += 1
if provas == "Sim, busco melhorar meu tempo": pontos += 2
elif provas == "Já participei por experiência": pontos += 1

# Determinar perfil
if pontos <= 2:
    perfil = "Iniciante Sedentário"
elif pontos <= 4:
    perfil = "Iniciante Ativo"
elif pontos <= 6:
    perfil = "Intermediário"
elif pontos <= 7:
    perfil = "Avançado"
else:
    perfil = "Elite"

# Seleção automática de ciclos
if perfil.startswith("Iniciante"):
    macrociclo = "Linear"
    mesociclo = "Adaptação" if "Sedentário" in perfil else "Base"
    microciclo = "Adaptação" if "Sedentário" in perfil else "Estável"
elif perfil == "Intermediário":
    macrociclo = "Ondulatório"
    mesociclo = "Base"
    microciclo = "Carga"
elif perfil == "Avançado":
    macrociclo = "Blocos"
    mesociclo = "Desenvolvimento"
    microciclo = "Carga"
elif perfil == "Elite":
    macrociclo = "Contemporâneo"
    mesociclo = "Choque"
    microciclo = "Polimento"

# Banco de treinos por microciclo
banco = {
    "Adaptação": [
        {"tipo": "Caminhada + trote leve", "duracao": 25, "intensidade": "Leve"},
        {"tipo": "Trote leve + caminhada (intervalado)", "duracao": 30, "intensidade": "Leve"},
        {"tipo": "Mobilidade e técnica + 15min leve", "duracao": 20, "intensidade": "Leve"}
    ],
    "Estável": [
        {"tipo": "Corrida contínua leve 25min", "duracao": 25, "intensidade": "Leve"},
        {"tipo": "Intervalado leve (2x4min) + caminhada", "duracao": 30, "intensidade": "Moderado"},
        {"tipo": "Técnica + corrida 20min contínua", "duracao": 25, "intensidade": "Leve"}
    ],
    "Carga": [
        {"tipo": "Corrida contínua 35min ritmo confortável", "duracao": 35, "intensidade": "Moderado"},
        {"tipo": "Intervalado progressivo 3x6min + pausa leve", "duracao": 40, "intensidade": "Forte"},
        {"tipo": "Técnica + tiros curtos + leve", "duracao": 30, "intensidade": "Moderado"}
    ],
    "Polimento": [
        {"tipo": "Rodagem curta com acelerações", "duracao": 20, "intensidade": "Moderado"},
        {"tipo": "Mobilidade + 15min leve com foco em postura", "duracao": 15, "intensidade": "Leve"},
        {"tipo": "Rodagem progressiva 20min", "duracao": 20, "intensidade": "Moderado"}
    ]
}

volume_total = 0
semana = banco.get(microciclo, [])
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
