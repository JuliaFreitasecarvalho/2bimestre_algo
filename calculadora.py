import operator
import math

def calcular_posfixa(expressao):
    pilha = []
    variaveis = {}

    tokens = expressao.split()

    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            # Se for número
            pilha.append(int(token))

        elif token.isalpha():
            # Se for variável
            if token in variaveis:
                pilha.append(variaveis[token])
            else:
                pilha.append(token)  # pode ser para atribuição depois

        elif token == '+':
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(a + b)

        elif token == '-':
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(a - b)

        elif token == '*':
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(a * b)

        elif token == '/':
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(int(a / b))  # divisão inteira

        elif token == '%':
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(a % b)

        elif token == '^':
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(int(math.pow(a, b)))

        elif token == '!':
            a = pilha.pop()
            pilha.append(-a)

        elif token == '=':
            valor = pilha.pop()
            var = pilha.pop()
            if isinstance(var, str):
                variaveis[var] = valor
                pilha.append(valor)
            else:
                raise ValueError("Atribuição inválida. Esperava uma variável.")

        else:
            raise ValueError(f"Token inválido: {token}")

    if len(pilha) != 1:
        raise ValueError("Expressão malformada.")
    
    return pilha[0]



print(calcular_posfixa("x 10 ="))       # Atribui 10 a x → resultado: 10
print(calcular_posfixa("x 2 *"))        # Usa x → resultado: 20
print(calcular_posfixa("4 !"))          # Resultado: -4
