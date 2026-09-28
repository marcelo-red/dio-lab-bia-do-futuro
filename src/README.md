# Passo a Passo de execução

## Setup do ollama
```bash

# 1. Instalar ollama (ollama.com)
# 2. Baixar um modelo leve
"llama3.2:latest"

# 3. Testar se funciona
ollama run llama3.2:latest "olá!"

```
## Código completo
```bash
Todo código-fonte está no arquivo  `app.py`.

```
## Como Rodar
```bash
# 1. Instalar dependências
pip instal streamlit pandas requests

# 2. Garantir que o Ollama está rodando
ollama serve

# 3. Rodar o app
cd "C:\Projetos da Dio\Bia\src"

python -m streamlit run app.py --server.port 8666
```
## Evidências de execução

<img width="1920" height="1080" alt="Bia 1" src="https://github.com/user-attachments/assets/5cbd1087-e33a-44da-8679-5a5fe32d4077" />


<img width="1920" height="1080" alt="Bia 4" src="https://github.com/user-attachments/assets/582b3dbd-6399-4e28-8c82-197d3c8d181d" />

```
