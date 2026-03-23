#idade = 30
#altura = 1.75
#nome = "Alice"
#is_estudade = True

# Tipagem dinâmica - python entende em tempo de execução

# Tipagem estática - java e C++ você deve declarar explicitamente no momento da compilação

# Type hint - identificar as variáveis

#idade: int = 30
#altura: float = 1.75
#nome: str = "Alice"
#is_estudade: bool = True

# Tipagem forte
# não é possivel realizar operações com tipos diferentes de dados
# exemplo: realizar operações de soma e substração com tipos diferentes (int + str)

# tipando o desafio anterior

nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

#1 solicitar ao usuario que digite seu nome
while nome_valido is not True:
    try:
        nome_usuario: str = input("Digite o seu nome: ")

        if nome_usuario.isdigit():
            print("Voce digitou o nome errado")

        if len(nome_usuario) == 0:
            print("Voce nao digitou o nome")


        if nome_usuario.isspace():
            print("Voce digitou apenas espacos")
        else:
            nome_valido = True
            print("Nome Válido: ", nome_usuario)
    except ValueError as e:
        print(e)

#2 Solicitar ao usuario que digite o valor do seu salario
#  Conversão da entrada para numero de ponto flutuante
while salario_valido is not True:
    try:
        salario: float = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        
        else:
            salario_valido = True

    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")


#3 solicitar ao usuario que digite o valor do bonus
#  Converter a entrada para um numero de ponto flutuante
while bonus_valido is not True:

    try:
        bonus_recebido: float = float(input("Digite o valor do bônus recebido: "))
        if bonus_recebido < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")

#4 calcule o valor do bonus final
bonus_final: float = bonus_recebido * 1.2  # Exemplo, ajuste conforme necessário
kpi: float = (salario + bonus_final) / 1000  # Exemplo simples de KPI

#5 imprima o calculo do valor final
print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome_usuario}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")