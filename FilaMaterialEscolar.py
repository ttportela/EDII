class MaterialEscolar:
    def __init__(self, descricao, quantidade):
        self.descricao  = descricao
        self.quantidade = quantidade
        
        self.proximo = None
    
    def __str__(self):
        return self.descricao + ', ' + str(self.quantidade)
    
class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo   = None
        
    def listar(self):
        if self.primeiro == None:
            print("Lista vazia.")
        else:
            atual = self.primeiro
            i = 1
            while atual != None:
                print(i, " -", atual)
                atual = atual.proximo
                i += 1
                
    def adicionar(self, item):
        if self.primeiro == None:
            self.primeiro = self.ultimo = item
        else:
            self.ultimo.proximo = item
            self.ultimo = item
            
    def remover(self):
        if self.primeiro == None:
            return None
        else:
            item = self.primeiro
            self.primeiro = self.primeiro.proximo
            if self.primeiro == None:
                self.ultimo = None
            return item
    
def ler():
    x = MaterialEscolar('', '')
    x.descricao  = input("Informe a descrição: ")
    x.quantidade = int( input("Informe a quantidade desejada: ") )
    return x

## https://codeshare.io/WdngP3
print("-- Programa de Materiais --")

ls = Fila()

while True:
    print("\n---------------------------------")
    ls.listar()
    
    op = input("O que deseja? ([a]dicionar, [r]emover, [x]air)")
    if op == 'a':
        aux = ler()
        ls.adicionar(aux)
    elif op == 'r':
        aux = ls.remover()
        print(aux, "comprado(a)!")
    else:
        break