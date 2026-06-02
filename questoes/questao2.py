class PortalDimensional:
    def __init__(self, nome, destino, energia_necessaria, energia_disponivel):
        self.nome = nome
        self.destino = destino
        self.energia_necessaria = energia_necessaria
        self.energia_disponivel = energia_disponivel
    def pode_abrir(self):
        if self.energia_disponivel >= self.energia_necessaria:
            return True
        else:
            return False
    def calcular_falta_energia(self):
        if self.pode_abrir():
            return 0
        else:
            falta = self.energia_necessaria - self.energia_disponivel
            return falta
    def classificar_estabilidade(self):
        falta = self.calcular_falta_energia()
        if falta == 0:
            return "portal estável"
        elif falta <= 20: 
            return "portal quase estável"
            return "portal instável"
    def exibir_resumo(self):
        situacao = self.classificar_estabilidade()
        print("--- RESUMO DO PORTAL DIMENSIONAL ---")
        print(f"Nome do Portal: {self.nome}")
        print(f"Destino: {self.destino}")
        print(f"Energia Disponível: {self.energia_disponivel}")
        print(f"Energia Necessária: {self.energia_necessaria}")
        print(f"Situação do Portal: {situacao}")
#_________________________MAIN______________________________
porta1 = PortalDimensional("Dafny", "Aurora Boreal", 50, 40)
porta1.exibir_resumo()
porta2 = PortalDimensional("Luna", "Jupiter", 100, 85)
porta2.exibir_resumo()
porta3 = PortalDimensional("Ana Banana", "Japão", 150, 50)
porta3.exibir_resumo()
        