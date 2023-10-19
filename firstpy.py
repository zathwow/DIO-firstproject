import requests

# IDs dos usuários a serem consultados
user_ids = [1, 2, 3]

# URL base da API da Santander Dev Week 2023
base_url = "https://sdw-2023-prd.up.railway.app/users/"

# Dicionário para armazenar as informações dos clientes
clientes = {}

for user_id in user_ids:
    # Fazer uma solicitação GET para obter os dados do cliente
    response = requests.get(f"{base_url}{user_id}")
    if response.status_code == 200:
        # Converter a resposta JSON em um dicionário
        cliente_data = response.json()
        clientes[user_id] = cliente_data

# Exemplo de clientes obtidos
print(clientes)

import openai

# Chave de API do ChatGPT (substitua pela sua chave)
openai.api_key = "sua_chave_de_api"

# Dicionário para armazenar as mensagens personalizadas
mensagens_personalizadas = {}

# Gerar mensagens personalizadas para cada cliente
for user_id, cliente_data in clientes.items():
    nome = cliente_data.get("nome", "Cliente")
    mensagem = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Olá {nome}, a importância dos investimentos é fundamental para o seu futuro financeiro.",
        max_tokens=50
    )
    mensagem_personalizada = mensagem.choices[0].text
    mensagens_personalizadas[user_id] = mensagem_personalizada

# Exemplo de mensagens personalizadas
print(mensagens_personalizadas)

import requests

# URL base da API da Santander Dev Week 2023
base_url = "https://sdw-2023-prd.up.railway.app/users/"

# Dicionário com mensagens personalizadas para cada usuário
mensagens_personalizadas = {
    1: "Mensagem personalizada para o usuário 1.",
    2: "Mensagem personalizada para o usuário 2.",
    3: "Mensagem personalizada para o usuário 3."
}

# Enviar as mensagens de marketing de volta para a API da Santander Dev Week 2023
for user_id, mensagem in mensagens_personalizadas.items():
    url = f"{base_url}{user_id}"
    data = {
        "news": mensagem
    }
    response = requests.put(url, json=data)

    if response.status_code == 200:
        print(f"Mensagem enviada com sucesso para o usuário {user_id}")
    else:
        print(f"Falha ao enviar mensagem para o usuário {user_id}: {response.status_code}")