# Base de Conhecimento

> [!TIP] 
> **Prompt usado para esta etapa:**
> 
> Preciso organizar a base de conhecimento do meu agente financeiro.
> Tenho estes arquivos de dados:[liste os arquivos].
> Me ajude a:
> (1)entender o que cada arquivo contém,
> (2)decidir como usar cada um,
> (3)criar um exemplo de contexto formatado para incluir no prompt.
>



## Dados Utilizados

| Arquivo | Formato | Para que serve na BIA |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV |Manter a continuidade consultiva, sabendo quais problemas anteriores o cliente relatou. |
| `perfil_investidor.json` | JSON | Travar as recomendações da IA dentro das classes autorizadas (Conservador, Moderado ou Arrojado). |
| `produtos_financeiros.json` | JSON | Catálogo oficial dos produtos disponíveis. O agente cocria soluções usando apenas essa lista para evitar ofertas inexistentes ou fraudulentas.|
| `transacoes.csv` | CSV | Analisar comportamentos de gastos anteriores do usuário para identificar padrões de consumo exorbitantes e disparar avisos preventivos. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

```text

Não houve expansão de arquivos externos para garantir a conformidade e integridade do escopo do desafio. No entanto, o código da aplicação (src/app.py) foi adaptado com uma função de tratamento de exceções (try-except). Caso os arquivos físicos locais sofram alguma corrupção de caminho ou ausência no momento da execução, o sistema gera de forma resiliente dados sintéticos equivalentes diretamente na memória RAM, garantindo que o agente financeiro permaneça operacional sob qualquer circunstância de infraestrutura.

...
```

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

```text

Os dados estruturados (.csv e .json) localizados na pasta /data são importados de maneira assíncrona no início da inicialização da interface através do método @st.cache_data da biblioteca Pandas e do módulo nativo JSON do Python. Essa estratégia otimiza o desempenho do sistema, lendo os dados apenas uma vez e mantendo-os em cache na sessão do usuário, evitando requisições repetitivas de leitura em disco.

...
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar ,podemos simplesmente "injetar" os dados em nosso prompt , garantindo que o nosso agente tenha o melhor contexto possível. Lembrando que, em soluções mais robustas, o ideal é que essas informações sejam carregadas dinamicamente para que possamos ganhar flexibilidade. 

```text

Para o escopo deste protótipo, as variáveis críticas extraídas dos dados locais (como o nome do cliente e a classificação exata contida no perfil_investidor.json) são injetadas dinamicamente como variáveis de ambiente dentro do prompt de sistema (System Prompt).Além disso, o fluxo do chat consulta o estado dos dados em tempo real para estruturar as respostas consultivas. Isso permite que a IA personalize as sugestões de forma reativa à entrada do usuário, garantindo uma ancoragem factual estrita que impede qualquer tipo de alucinação do modelo.

...
```

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

## Exemplo de Contexto Montado

Abaixo está o exemplo real de como a aplicação filtra, higieniza e estrutura os dados brutos obtidos das tabelas locais para gerar o contexto consolidado que guia as respostas da IA:

```text
============================================================
CONTEXTO OPERACIONAL DO AGENTE (BIA GUARDFIN)
============================================================
POLÍTICA DE PRIVACIDADE: Dados sensíveis (senhas/CPF) ocultados.

DADOS CADASTRAIS DO CLIENTE:
- Nome do Usuário: Carlos Silva
- Perfil de Risco: Moderado
- Alvo Estratégico: Preservação de capital e crescimento a médio prazo.
- Tolerância a Volatilidade: Média

HISTÓRICO RECENTE DE TRANSAÇÕES (Mapeado via transacoes.csv):
- 2026-09-10 | Valor: R$ -120.50 | Categoria: Alimentação    | Descrição: Restaurante Almoço
- 2026-09-12 | Valor: R$ -45.90  | Categoria: Transporte    | Descrição: Corrida de Aplicativo
- 2026-09-15 | Valor: R$ +5500.00| Categoria: Salário       | Descrição: Recebimento Mensal Empresa
- 2026-09-20 | Valor: R$ -850.00 | Categoria: Lazer         | Descrição: Compra de Eletrônico
- 2026-09-24 | Valor: R$ -119.90 | Categoria: Assinaturas   | Descrição: Serviço de Streaming de Vídeo

DIRETRIZ DE AÇÃO PROATIVA (ANTECIPAÇÃO DE RISCO):
- Status de Caixa: Positivo (R$ 4.363,70 acumulado no período).
- Próxima Melhor Decisão Mapeada: Sugerir exclusivamente produtos de Renda Fixa pós-fixados ou Multimercados de baixo risco, em estrita aderência ao perfil "Moderado" e vedar ativos altamente voláteis.
============================================================

...
```
