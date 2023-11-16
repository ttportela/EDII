class No:
    def __init__(self, valor):
        self.valor = valor
        self.arestas = []
    
    def addRelacao(self, no):
        self.arestas.append(no)
        
        
    def imprimirRelacao(self):
        print(self.valor, ":")
        for arr in self.arestas:
            print("-", arr.valor)
    
    def distancia(self, noB):
        ct = 0


# Exemplo de Grafo:   
no1 = No(1)
no2 = No(2)
no3 = No(3)
no4 = No(4)
no5 = No(5)

no1.addRelacao(no2)
no1.addRelacao(no3)
no1.addRelacao(no4)
no1.addRelacao(no5)

no2.addRelacao(no1)
no2.addRelacao(no5)
no2.addRelacao(no4)

no3.addRelacao(no1)

no4.addRelacao(no1)
no4.addRelacao(no2)
no4.addRelacao(no5)

no5.addRelacao(no1)
no5.addRelacao(no2)
no5.addRelacao(no4)