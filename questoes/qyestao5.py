class CofreDoDragao():
    def __init__(self,nome_dragao, tesouros):
        self.nome_dragao = nome_dragao
        self.tesouros = tesouros
    def adicionar_item(self, nome, valor):
        if nome != "" and valor > 0:
            self.tesouros.append({
                "Nome" : nome,
                "Valor" : valor
            })
    def listar_itens(self):
        for i in self.tesouros:
            print(f"{i}\n")
    def calcular_total(self):
        soma = 0
        for i in self.tesouros:
            soma =+ i["Valor"]
        return soma
    def encontrar_item_mais_valioso(self):
        maiorvalor = 0
        maisvalioso = {}
        for item in self.tesouros:
            if item["Valor"] > maiorvalor:
                maiorvalor = item["Valor"]
                maisvalioso = item
        return maisvalioso
    def classificar_colecao(self):
        if self.calcular_total()<500:
            return("Colecao pequena")
        elif self.calcular_total()>=500 and self.calcular_total <= 1500:
            return("Colecao respeitável")
        else:
            return("colecao lendária")
    def exibir_resumo(self):
        print(f"Nome:{self.nome_dragao}\nTotal acumulado:{self.calcular_total()}\nMais valioso:{self.encontrar_item_mais_valioso()}\nClassificação:{self.classificar_colecao()}")
tesouros = [{
    "Nome" : "aa",
    "Valor" : 550
}]
teste = CofreDoDragao("Ju",tesouros)
teste.adicionar_item("a",90)
teste.listar_itens()
teste.calcular_total()
teste.encontrar_item_mais_valioso()
print(teste.classificar_colecao())
teste.exibir_resumo()
    
