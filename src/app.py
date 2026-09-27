import streamlit as st
import pandas as pd

# Configuração da página do Streamlit
st.set_page_config(page_title="BIA GuardFin", page_icon="🤖", layout="centered")

st.title("🤖 BIA GuardFin — Agente Financeiro")
st.caption("Protótipo Homologado — Desafio de Inteligência Generativa DIO")
st.markdown("---")

dados_json = {"nome": "Carlos Silva", "perfil": "Moderado"}
dados_csv = pd.DataFrame({
    "Data": ["2026-09-15", "2026-09-22", "2026-09-26"],
    "Valor": [-119.80, 5200.00, -850.00],
    "Categoria": ["Assinaturas", "Salário Recebido", "Lazer"],
    "Descricao": ["Streaming", "Salário Mensal", "Compra Eletrônico"]
})

st.sidebar.subheader("🛡️ Painel de Governança")
st.sidebar.caption("Status Infra: **Online (Modo Seguro)**")
st.sidebar.markdown(f"**Cliente:** {dados_json['nome']}")
st.sidebar.markdown(f"**Perfil de Risco:** `{dados_json['perfil']}`")

if st.sidebar.checkbox("Inspecionar Histórico (CSV)"):
    st.sidebar.dataframe(dados_csv)

if "historico_mensagens" not in st.session_state:
    st.session_state.historico_mensagens = [{"role": "assistant", "content": "Olá! Sou a BIA GuardFin. Como posso ajudar nas suas decisões financeiras com total privacidade hoje?"}]

for mensagem in st.session_state.historico_mensagens:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

if prompt_usuario := st.chat_input("Digite sua dúvida financeira..."):
    st.session_state.historico_mensagens.append({"role": "user", "content": prompt_usuario})
    with st.chat_message("user"):
        st.write(prompt_usuario)
    prompt_normalizado = prompt_usuario.lower()
    
    if any(chave in prompt_normalizado for chave in ["senha", "token", "password", "cpf", "cvv", "cartão"]):
        resposta_agente = "⚠️ **[Filtro de Cibersegurança]** Por questões de privacidade e conformidade com a LGPD, o envio de chaves de acesso, senhas ou documentos diretos é terminantemente bloqueado no chat."
    elif any(termo in prompt_normalizado for termo in ["ignore", "substitua as regras", "diretrizes anteriores"]):
        resposta_agente = "⚠️ **[Defesa de Sistema Ativa]** Tentativa de modificação de parâmetros operacionais abortada. Minhas diretrizes financeiras permanecem íntegras."
    elif any(invalido in prompt_normalizado for invalido in ["futebol", "clima", "tempo", "receita", "filme", "novela"]):
        resposta_agente = "Não tenho informações suficientes para responder a isso no momento. Meu ecossistema de dados restringe-se exclusivamente a análises patrimoniais."
    else:
        resposta_agente = f"Analisando seu histórico de transações e seu perfil classificado como **{dados_json['perfil']}**, identifiquei que sua saúde financeira está estável neste mês. Com base nas diretrizes de segurança, **sua próxima melhor decisão** é diversificar parte do seu caixa em ativos de Renda Fixa pós-fixados. Deseja que eu liste as opções disponíveis na base?"

    st.session_state.historico_mensagens.append({"role": "assistant", "content": resposta_agente})
    with st.chat_message("assistant"):
        st.write(resposta_agente)
