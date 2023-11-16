#Trie
class Trie:
    def __init__(self, valor=''):
        self.valor = valor
        self.marca = False
        
        self.filhos = []
    
    def filho(self, c):
        for letra in self.filhos:
            if letra.valor == c:
                return letra
            
        letra = Trie( c )
        self.filhos.append(letra)
        return letra
    
    def add(self, palavra): # 'abajur' 
        letra = self.filho( palavra[0] ) # Encontra ou cria o filho
        
        if len(palavra) > 1:
            letra.add( palavra[1:] ) # 'bajur'
        else:
            letra.marca = True
            
    def imprime(self, palavra=''):
        palavra = palavra + self.valor
        if self.marca:
            print(palavra)
        for letra in self.filhos:
            letra.imprime(palavra)


t = Trie()
t.add('abajur')
t.add('abacate')
t.add('aba')
t.imprime()