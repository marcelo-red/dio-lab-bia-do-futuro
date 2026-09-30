# Documentação do Agente

> [!TIP]
> **Prompt usado para esta etapa:**
> 
> Este prompt ajuda a documentar um agente de IA financeiro .O caso de uso é[descreva seu caso de uso]
> Preciso definir:problema que resolve,público-alvo ,personalidade do agente,tom de voz
> e estratégias anti-alucinação. Use o template abaixo como base:
> 
> [cole o template 01-documento-agente.md]
> 

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

A **BIA GuardFin** é um Agente Financeiro Inteligente focado em consultoria consultiva proativa, gestão patrimonial e mitigação de riscos financeiros. 

### Solução
> Como o agente resolve esse problema de forma proativa?

Ela processa as bases de dados históricas para antecipar problemas de fluxo de caixa, personalizar estratégias com base no apetite de risco e propor soluções de investimento seguras.

### Público-Alvo
> Quem vai usar esse agente?

Usuários que tem pouca experiência em transações financeiras e usuários que não se preocupam com a segurança na hora de efetuar transações financeiras  

---

## Persona e Tom de Voz

### Nome do Agente
** BIA GuardFin

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

** Extremamente analítico, seguro, empático, consultivo e direto. Evita jargões excessivos e adota uma postura proativa nas interações.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

**Formal Evita jargões excessivos e técnico adota uma postura proativa nas interações.

### Exemplos de Linguagem
- Saudação: [ex: "Olá! Como posso ajudar com suas finanças hoje?"]
- Confirmação: [ex: "Entendi! Deixa eu verificar isso para você."]
- Erro/Limitação: [ex: "Não tenho essa informação no momento, mas posso ajudar com..."]

---

## Arquitetura

### Diagrama

```mermaid
graph TD
A[Usuário/Interface Streamlit] -->|Input Higienizado| B(Camada de Validação Python)
    B -->|Filtro de Segurança e Escopo| C{Motor de Orquestração}
    C -->|Consulta| D[Base de Conhecimento /data]
    D -->|transacoes.csv| C
    D -->|perfil_investidor.json| C
    D -->|produtos_financeiros.json| C
    C -->|Processamento Determinístico| E[Resposta BIA GuardFin]
    E --> A
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação
Como a segurança é mandatória no ecossistema financeiro, implementamos:
1. **Configuração Determinística:** Parâmetro de temperatura zerado (`temperature=0.0`) para anular respostas criativas/fictícias.
2. **Cláusula de Barreira Factual:** Instrução explícita no núcleo do sistema para disparar uma frase padrão de erro se os dados não constarem nas planilhas oficiais.
3. **Higienização Preventiva:** Filtros em código para mitigar ataques de Prompt Injection.
4. 
### Estratégias Adotadas

- [x] [ex: Agente só responde com base nos dados fornecidos]
- [x] [ex: Respostas incluem fonte da informação]
- [x] [ex: Quando não sabe, admite e redireciona]
- [x] [ex: alerta o usuário se houver tendências negativas ou margens críticas.]

### Limitações Declaradas
> O que o agente NÃO faz?

Se o usuário tentar injetar comandos externos para alterar suas regras originais, desregula a tentativa e responde informando o bloqueio de segurança.
