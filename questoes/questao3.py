class RoboColetor:
    def __init__(self, nome, amostras, capacidade_maxima):
        self.nome = nome
        self.amostras = amostras
        self.capacidade_maxima = capacidade_maxima
    def adicionar_amostra(self, amostra):
        if amostra != "" and len(self.amostras) < self.capacidade_maxima:
            self.amostras.append(amostra)
    def listar_amostras(self):
        for i in range(len(self.amostras)):
            print(self.amostras[i])
    def contar_amostras(self):
        cont = 0
        for i in range(len(self.amostras)):
            cont +=1
            return cont
    def verificar_armazenamento(self):
        if len(self.amostras)<self.capacidade_maxima:
            return f"possui espaço"
        else:
            return f"ta cheio"
    def exibir_relatorio(self):
        print(f"nome:{self.nome}\nquantidade de amostras:{self.contar_amostras()} \ncapacidade:{self.capacidade_maxima}\n armazenamento: {self.verificar_armazenamento()}")
amostras =["a1","a2","a3"]
teste = RoboColetor("Ju",amostras,20)
teste.adicionar_amostra("a4")
teste.listar_amostras()
teste.contar_amostras()
teste.verificar_armazenamento()
teste.exibir_relatorio()
