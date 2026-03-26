from typing import Dict
import json

lista = ["sapato", 39, 10.38, True]

produto_1: dict = {
    "nome": "Sapato",
    "quantidade": 39,
    "preco": 10.38,
    "disponibilidade": True
}
produto_2: dict = {
    "nome": "televisao",
    "quantidade": 10,
    "preco": 70.38,
    "disponibilidade": False
}

carrinho: list = []

carrinho.append(produto_1)
carrinho.append(produto_2)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)