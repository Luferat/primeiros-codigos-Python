import requests

# Protótipo
def logradouro(cep):
    # cep = 22251050 # Somente para testes → Comente
    url = f'https://viacep.com.br/ws/{cep}/json/'
    data = requests.get(url)
    # print(data.status_code) # 200
    # print(data.json()) # Retorna um JSON → DICT
    return data.json() # Retorna um JSON → DICT

cep = input('\n\n\nDigite o CEP (só números):')

local = logradouro(cep)

print(f'''
    \n\n
    CEP: {local.get('cep')}
    Logradouro: {local.get('logradouro')}
    Bairro: {local.get('bairro')}
    Cidade: {local.get('localidade')}
''')