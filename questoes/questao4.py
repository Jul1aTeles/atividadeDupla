class MochilaDeMissao():
    def __init__(self, agente,equip,cap_max):
        self.agente= agente
        self.equip= equip
        self.cap_max = cap_max
    def adicionar_equipamento(self, equip):
        item= input("O que tu quer colocar na tua mochila?")
        self.equip.append(item)
    def listar_equipamentos(self):
        for item in self.equip:
            print(item)


lista = []
mocg(, lista)