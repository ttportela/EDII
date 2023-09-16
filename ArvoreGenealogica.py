class Pessoa:
    def __init__(self, nome):
        self.nome = nome

        self.pai = None
        self.mae = None

    def add(self, parente):
        fila = [self]

        while fila:
            e = fila.pop(0)

            if e.pai == None:
                e.pai = parente
                return
            if e.mae == None:
                e.mae = parente
                return
            
            fila.append(e.pai)
            fila.append(e.mae)

    
    def preOrdem(self):
        print(self.nome)
        if self.pai:
            self.pai.preOrdem()
        if self.mae:
            self.mae.preOrdem()
    def ordem(self):
        if self.pai:
            self.pai.ordem()
        print(self.nome)
        if self.mae:
            self.mae.ordem()
    def posOrdem(self):
        if self.pai:
            self.pai.posOrdem()
        if self.mae:
            self.mae.posOrdem()
        print(self.nome)



# ------------------------------------------------------------
def main():
    jon = Pessoa("Jon Snow")

    jon.add(Pessoa("Rhaegar Targaryen"))
    jon.add(Pessoa("Lyanna Stark"))

    jon.add(Pessoa("Aerys Targaryen"))
    jon.add(Pessoa("Rhaella Targaryen"))

    jon.add(Pessoa("Richard Stark"))
    jon.add(Pessoa("Lyarra Stark"))

 #   jon_pai = Pessoa("Rhaegar Targaryen")
 #   jon_mae = Pessoa("Lyanna Stark")
 #   jon.pai = jon_pai
 #   jon.mae = jon_mae

#    jon_pai_pai = Pessoa("Aerys Targaryen")
#    jon_pai_mae = Pessoa("Rhaella Targaryen")
#    jon_pai.pai = jon_pai_pai
#    jon_pai.mae = jon_pai_mae

#    jon_mae_pai = Pessoa("Richard Stark")
#    jon_mae_mae = Pessoa("Lyarra Stark")
#    jon_mae.pai = jon_mae_pai
#    jon_mae.mae = jon_mae_mae

    jon.preOrdem()
    print("------------")
    jon.ordem()
    print("------------")
    jon.posOrdem()

main()