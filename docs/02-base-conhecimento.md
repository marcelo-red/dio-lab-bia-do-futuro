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

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Não houve expansão de arquivos externos para garantir a conformidade e integridade do escopo do desafio. No entanto, o código da aplicação (src/app.py) foi adaptado com uma função de tratamento de exceções (try-except). Caso os arquivos físicos locais sofram alguma corrupção de caminho ou ausência no momento da execução, o sistema gera de forma resiliente dados sintéticos equivalentes diretamente na memória RAM, garantindo que o agente financeiro permaneça operacional sob qualquer circunstância de infraestrutura.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os dados estruturados (.csv e .json) localizados na pasta /data são importados de maneira assíncrona no início da inicialização da interface através do método @st.cache_data da biblioteca Pandas e do módulo nativo JSON do Python. Essa estratégia otimiza o desempenho do sistema, lendo os dados apenas uma vez e mantendo-os em cache na sessão do usuário, evitando requisições repetitivas de leitura em disco.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para o escopo deste protótipo, as variáveis críticas extraídas dos dados locais (como o nome do cliente e a classificação exata contida no perfil_investidor.json) são injetadas dinamicamente como variáveis de ambiente dentro do prompt de sistema (System Prompt).Além disso, o fluxo do chat consulta o estado dos dados em tempo real para estruturar as respostas consultivas. Isso permite que a IA personalize as sugestões de forma reativa à entrada do usuário, garantindo uma ancoragem factual estrita que impede qualquer tipo de alucinação do modelo.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
