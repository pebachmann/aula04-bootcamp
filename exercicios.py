# crie um dicionario para armazenar informações de um livro,
# incluindo titulo, autor e ano de publicação. Imprima cadainformação

from typing import Dict

livro: dict[str, any] = {
    "Titulo": "Game of Thrones",
    "Autor": "Estagiario",
    "Ano": 2005
}

lista_de_elementos: list = livro.items()

for elemento in lista_de_elementos:
    print(elemento)