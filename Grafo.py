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
    
    def __str__(self):
        return self.valor
    
    def BFS(self): # Busca em Largura - BFS
        visitados = set()
        
        fila_proc = list()
        fila_proc.append(self)
        
        while len(fila_proc) > 0:
            no = fila_proc.pop(0)
            visitados.add(no)
            
            for e in no.arestas:
                if e not in visitados:
                    fila_proc.append(e)
                visitados.add(e)
        
        return visitados
    
# -------- Criação do GRAFO ----------    
no1 = No(1)
no2 = No(2)
no3 = No(3)
no4 = No(4)
no5 = No(5)

no1.addRelacao(no2)
no1.addRelacao(no3)
no1.addRelacao(no4)
#no1.addRelacao(no5)

no2.addRelacao(no1)
no2.addRelacao(no5)
no2.addRelacao(no4)

no3.addRelacao(no1)

no4.addRelacao(no1)
no4.addRelacao(no2)
no4.addRelacao(no5)

#no5.addRelacao(no1)
no5.addRelacao(no2)
no5.addRelacao(no4)

# ----------- Teste: ----------
visitados = no3.BFS()

for e in visitados:
    print(e.valor)