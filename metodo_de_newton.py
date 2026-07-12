# All rights reserved © 2026 Asheley Henrique and Evelyn Dantas


def melhor_chute(indice, radical):
    chute = 0
    
    while True and radical != 0:
        valor_proximo = chute ** indice
        
        if (chute == 0):
            valor_mais_proximo = valor_proximo
        else:
            if (valor_mais_proximo < valor_proximo <= radical):
                valor_mais_proximo = valor_proximo
            else:
                print(f"Melhor chute: {chute}")
                break
        chute += 0.1
    return chute


iteracoes = 0

# Validando entrando do índice.
while True:
    try:
        indice  = int(input("Índice (número natural maior que zero): "))
        
        if (indice > 0):
            break
        else:
            print("Por favor, insira um número maior que zero!")
    except:
        print("Por favor, insira um número inteiro para o índice!")


# Validando entrada do radical.
while True:
    try:
        radical = float(input("Radical (número real): "))
        
        if (indice % 2 == 0 and radical < 0):
            print("Com índice par, o radical não pode ser negativo!")
        else:
            break
    except:
        print("Por favor, insira um número!")


chute = melhor_chute(indice, radical)

while True:
    try:
        iteracoes += 1
        
        funcao = chute ** indice - radical
        derivada = indice * chute ** (indice - 1)
    
        novo_chute = chute - funcao / derivada
        
        if (abs(novo_chute - chute) < 0.0001):
            chute = novo_chute
            break
        else:
            chute = novo_chute
    except ZeroDivisionError:
        chute = 0
        break
    except:
        print("Erro desconhecido!")
        break

print(f"Quantidade de iterações: {iteracoes}")
print(f"O valor de saída é: {chute}")
