import time

# Recursiva 
def soma_recursiva(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + soma_recursiva(lista[1:])

# Iterativa
def soma_iterativa(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma

# Memoization 
def soma_memo(lista, memo={}):
    if len(lista) in memo:
        return memo[len(lista)]
    if len(lista) == 0:
        return 0
    memo[len(lista)] = lista[0] + soma_memo(lista[1:], memo)
    return memo[len(lista)]

# Função para medir o tempo
def medir_tempo(funcao, lista):
    start_time = time.time()
    resultado = funcao(lista)
    end_time = time.time()
    return resultado, end_time - start_time

# Testando com uma lista de exemplo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

# Comparação
resultado_recursivo, tempo_recursivo = medir_tempo(soma_recursiva, lista)
resultado_iterativo, tempo_iterativo = medir_tempo(soma_iterativa, lista)
resultado_memo, tempo_memo = medir_tempo(soma_memo, lista)

# Exibindo resultados
print(f"Recursivo: Soma = {resultado_recursivo}, Tempo: {tempo_recursivo:.8f} segundos")
print(f"Iterativo: Soma = {resultado_iterativo}, Tempo: {tempo_iterativo:.8f} segundos")
print(f"Memoization: Soma = {resultado_memo}, Tempo: {tempo_memo:.8f} segundos")