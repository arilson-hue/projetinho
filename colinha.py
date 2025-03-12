import json

dados = {'nome': 'Ana', 'idade': 28}

with open('dados.json', 'w') as f:
    json.dump(dados, f)