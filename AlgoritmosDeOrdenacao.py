def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Últimos i elementos já estão na posição correta
        for j in range(0, n-i-1):
            # Percorre a lista do início ao penúltimo elemento não ordenado
            if arr[j] > arr[j+1]:
                # Se o elemento atual for maior que o próximo, troca-os
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento atual a ser inserido na parte ordenada
        j = i - 1  # Índice do último elemento na parte ordenada
        
        # Move os elementos maiores que 'key' uma posição à frente
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        # Insere 'key' na posição correta na parte ordenada
        arr[j+1] = key
    return arr

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Encontra o índice do elemento mínimo na parte não ordenada
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Troca o elemento mínimo com o primeiro elemento da parte não ordenada
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Seleciona o elemento pivô
    esquerda = [x for x in arr if x < pivot]  # Elementos menores que o pivô
    meio = [x for x in arr if x == pivot]  # Elementos iguais ao pivô
    direita = [x for x in arr if x > pivot]  # Elementos maiores que o pivô
    
    return quick_sort(esquerda) +  meio + quick_sort(direita)  # Recursivamente ordena as partes

def merge_sort(arr):
    if len(arr) == 1:
        # Quando o array já foi dividido até restar apenas um elemento
        return arr
    else: 
        meio = len(arr) // 2
        # Ordena a primeira metade do arranjo.
        esquerda = merge_sort(arr[:meio])
        # Ordena a segunda metade do arranjo.
        direita  = merge_sort(arr[meio:])
        # Combina as duas metades ordenadas anteriormente.
        return merge(esquerda, direita)

def merge(esquerda, direita):
    # Cria um array com o tamanho somado das duas sublistas
    aux = [0] * (len(esquerda) + len(direita))
    
    for k in range(len(aux)):
        # Mescla as duas metades ordenadas em ordem crescente
        if len(esquerda) > 0 and len(direita) > 0:
            if esquerda[0] < direita[0]:
                aux[k] = esquerda.pop(0)
            else:
                aux[k] = direita.pop(0)
        # Adiciona os elementos restantes da metade esquerda (se houver)
        elif len(esquerda) > 0:
            aux[k] = esquerda.pop(0)
        # Adiciona os elementos restantes da metade direita (se houver)
        elif len(direita) > 0:
            aux[k] = direita.pop(0)
    return aux    

# TESTANDO:
N = 10000
# Array aleatório de N elementos
import random
import time
random.seed(1)
arr = [random.randint(0, 101) for _ in range(N)]
    
# Testando a ordenação:
print("Lista original...................:", arr[:10])
start = time.time()
print("Lista ordenada por bubble_sort...:", bubble_sort(arr.copy())[:10])
print("Tempo:", (time.time() - start) * 1000)
start = time.time()
print("Lista ordenada por insertion_sort:", insertion_sort(arr.copy())[:10])
print("Tempo:", (time.time() - start) * 1000)
start = time.time()
print("Lista ordenada por selection_sort:", selection_sort(arr.copy())[:10])
print("Tempo:", (time.time() - start) * 1000)
start = time.time()
print("Lista ordenada por merge_sort....:", merge_sort(arr.copy())[:10])
print("Tempo:", (time.time() - start) * 1000)
start = time.time()
print("Lista ordenada por quick_sort....:", quick_sort(arr.copy())[:10])
print("Tempo:", (time.time() - start) * 1000)