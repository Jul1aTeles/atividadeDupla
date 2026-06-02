class CapsulaDoTempo():
    def __init__(self,autor, mensagem, ano_abertura, ano_atual):
        self.autor = autor
        self.mensagem = mensagem
        self.ano_abertura = ano_abertura
        self.ano_atual = ano_atual
    def pode_abrir(self):
        if self.ano_abertura == self.ano_atual:
            return f"Cápsula já pode ser aberta."
        else:
            return f"Cápsula ainda não pode ser aberta."
    def calcular_espera(self):
        if self.ano_abertura <= self.ano_atual:
            return 0
        else:
            return self.ano_abertura - self.ano_atual
    def classificar_espera(self):
        resto = self.ano_abertura - self.ano_atual
        if resto <= 0:
            print("Já pode abrir")
        elif resto >=1 and resto<=3:
            print("Espera curta")
        else:
            print("Espera longa")
    def exibir_resumo(self):
        print(f"\n autor:{self.autor}\n mensagem:{self.mensagem}\n ano de abertura:{self.ano_abertura}\n ano atual: {self.ano_atual}")

teste = CapsulaDoTempo("Julia","Hello",2013,2015)
teste.pode_abrir()
teste.calcular_espera()
teste.classificar_espera()
teste.exibir_resumo()
