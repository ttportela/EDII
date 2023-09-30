# Estrutura para a DATA:
class Data:
    def __init__(self, D, M, A, h, m):
        self.dia = D
        self.mes = M
        self.ano = A
        self.hora = h
        self.minuto = m

    def __str__(self):
        return "{:02d}/{:02d}/{:02d} {:02d}:{:02d}".format(\
            self.dia, self.mes, self.ano, self.hora, self.minuto)

    def diasNoMes(self):
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.mes in [4, 6, 9, 11]:
            return 30
        elif self.mes in [2]:
            return 28
    
    def somaDias(self, k):
        # Soma 1° os anos:
        anos = k // 365
        self.ano += anos
        # diminui a quantidade de dias que ja somei nos anos
        k -= anos * 365

        # Agora incrementar mes a mes:
        while (k > 0):
            x = self.diasNoMes() - self.dia
            # Faltam x dias para o fim do mes
            if k <= x:
                self.dia += k # Aqui acaba a soma
                break
            else: # se tem mais dias que restam no mês:
                self.dia = 1 # Vamos para o dia 1 do mes seguinte
                self.mes += 1
                # Atualiza o k:
                k = k - (x + 1)
                # Se o mes for 12, não existe mes 13 então:
                if self.mes == 13:
                    self.mes = 1
                    self.ano += 1 # soma um ano
    def compara(self, data):
        # Este método compara duas datas para saber qual vem antes na ordem:
        # A hora vou comparar em minutos:
        smin = self.hora*60 + self.minuto
        dmin = data.hora*60 + data.minuto
        # Faço uma comparação do maior ao menor
        if self.ano < data.ano:
            return -1 # menos um para self menor
        elif self.ano == data.ano and self.mes < data.mes:
            return -1
        elif self.ano == data.ano and self.mes == data.mes \
            and self.dia < data.dia: 
            return -1
        elif self.ano == data.ano and self.mes == data.mes \
            and self.dia == data.dia and smin < dmin:
            return -1
        elif self.ano == data.ano and self.mes == data.mes \
            and self.dia == data.dia and smin == dmin:
            return 0 # São iguais
        else:
            return 1 # A data self é maior

# Estrutura para os elementos da Lista
class No:
    def __init__(self, data):
        self.data = data
        self.prox = None

# Estrutura da Fila
class Fila: 
    def __init__(self):
        self.ini = None
    
    def add(self, data):
        novo = No(data)
        if self.ini == None:
            self.ini = novo
        else:
            # 1. pode ser que seja menor que a data inicial:
            if novo.data.compara(self.ini.data) < 0:
                novo.prox = self.ini
                self.ini = novo
            else:
            # 2. vamos achar a posicao que a data encaixa
                pt = self.ini # ponteiro da lista
                while True:
                    if pt.prox == None or pt.prox.data.compara(novo.data) > 0:
                        # Se chegou no fim da fila, ou o próximo é maior:
                        novo.prox = pt.prox
                        pt.prox = novo
                        break
                    else:
                        pt = pt.prox

    def imprimir(self):
        pt = self.ini
        while pt != None:
            print(pt.data)
            pt = pt.prox

# ---
print("1 - Testando a soma de dias (e impressão)")
d = Data(29, 9, 2023, 0, 0)
print(d, d.diasNoMes(), d.diasNoMes() - d.dia)
d.somaDias(1)
print(d)
d.somaDias(50)
print(d)
d.somaDias(600)
print(d)

print("2 - Testando a fila de datas:")
filaDeDatas = Fila()

filaDeDatas.add( Data(29, 9, 2023, 10, 0) )
filaDeDatas.add( Data(29, 9, 2023, 9, 10) )
filaDeDatas.add( Data(3, 9, 2023, 23, 0) )
filaDeDatas.add( Data(30, 9, 2023, 10, 0) )
filaDeDatas.add( Data(10, 10, 2023, 0, 30) )
filaDeDatas.add( Data(1, 1, 2023, 9, 30) )
filaDeDatas.add( Data(10, 9, 2024, 4, 10) )
filaDeDatas.add( Data(10, 9, 2020, 7, 0) )

filaDeDatas.imprimir()