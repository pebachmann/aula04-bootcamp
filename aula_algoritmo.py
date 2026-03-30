lista_de_numeros: list = [40,50,60,70,0,-408593,1,50]

# [40,50,60,70,0,-408593,1,50]
# [50,60,,700,-408593,1,50]

def ordenar_lista_de_numeros(numeros: list) -> list:
    nova_lista_de_numeros = numeros.copy()

    for i in range(len(nova_lista_de_numeros)):
        for j in range(i+1, len(nova_lista_de_numeros)):
            if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = nova_lista_de_numeros[j], nova_lista_de_numeros[i]

    return nova_lista_de_numeros

nova_lista = ordenar_lista_de_numeros(lista_de_numeros)
print(nova_lista)

# funcoes sao desenvolvidas pelos engenheiros de dados e utilizados pelos times
# disponibilizam-se as funcoes em diretorios como 'utils.py', 'aws.py'.
# conceito DRY: Dont repeat Yourself
#   padronização e reutilização de código em time através de funções.