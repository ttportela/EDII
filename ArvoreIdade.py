# Revolução e Recursão:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Node:
    def __init__(self, value):
        self.value = value # Int
        self.pessoas = []
        
        self.left  = None # Node
        self.right = None # Node
    
    def add(self, value): # BFS - Busca em Largura
        new_node = Node(value)
        #print(self.value, ".add:", value)
        
        if value < self.value:
            if self.left == None:
                self.left = new_node
            else:
                self.left.add(value)
        else:
            if self.right == None:
                self.right = new_node
            else:
                self.right.add(value)
    
    def addPessoa(self, P):
        if self.value == P.idade:
            self.pessoas.append(P)
        elif self.value > P.idade:
            if self.left == None:
                self.left = Node(P.idade)
            self.left.addPessoa(P)
        else: #elif self.value < P.idade:
            if self.right == None:
                self.right = Node(P.idade)
            self.right.addPessoa(P)
    
    def imprimir(self):
        #Na ORDEM:
        # 1° Esquerda
        if self.left:
            self.left.imprimir()

        #2° O NÓ:
        print("Idade ", self.value)
        for p in self.pessoas:
            print(" - ", p.nome, "|", p.idade)

        #3° Direito:
        if self.right:
            self.right.imprimir()

# ------
root = Node(50)
print("ADD 35:")
root.add(35)
print("-------------------")
print("ADD 40:")
root.add(40)
print("-------------------")
print("ADD 37:")
root.add(37)
print("-------------------")
print("ADD 20:")
root.add(20)
print("-------------------")
print("ADD 60:")
root.add(60)
print("-------------------")

root.addPessoa( Pessoa("João", 37) )
root.addPessoa( Pessoa("José", 37) )
root.addPessoa( Pessoa("Maria", 20) )
root.addPessoa( Pessoa("Steven", 60) )
root.addPessoa( Pessoa("Enzo", 10) )

print("------------------- -------------------")
root.imprimir()