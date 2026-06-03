class MochilaDeMissao():
    def __init__(self, agente,equip,cap_max):
        self.agente= agente
        self.equip= equip
        self.cap_max = cap_max
    def adicionar_equipamento(self):
        item= input("O que tu quer colocar na tua mochila?")
        self.equip.append(item)
    def listar_equipamentos(self):
        for equipamento in self.equip:
            print(equipamento)
    def contar_equipamentos(self):
        quantidade= len(self.equip)
        return quantidade
    def verificar_espaco(self):
        if self.contar_equipamentos() >= self.cap_max:
            return"Sua mochila está cheia!"
        else:
            return "Não está cheia!"
    def exibir_relatorio(self):
        print(f"Nome: {self.agente}")
        print(f"Total de equipamento:{self.contar_equipamentos()} ")
        print(f"Capacidade maxima: {self.cap_max}")
        print(f"A situação: {self.verificar_espaco()}")

lista = []
mochi1= MochilaDeMissao("Ana Misteriosa", [], 3)
mochi1.adicionar_equipamento()
mochi1.listar_equipamentos()
mochi1.contar_equipamentos()
mochi1.verificar_espaco()
mochi1.exibir_relatorio()
