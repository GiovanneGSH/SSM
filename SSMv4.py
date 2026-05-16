# Giovanne Silveira Henrique - RGM: 47808667
# Algoritmo 1 SSM - Simulador de meio de pagamento.
# =================================================

from datetime import datetime, timedelta

dataHoje = datetime.today()

dataHojeFormatada = dataHoje.strftime("%d/%m/%Y")

horaFormatada = dataHoje.strftime("%H:%M")

diaDaSemana = dataHoje.weekday()

print("UNICSUL - Simulador de Meio de Pagamento - versão 2026" ,dataHojeFormatada, sep="        ")

print(
'''    
Meios de pagamento disponíveis: 
0 - Cartão de Débito
1 - Cartão de Crédito à Vista
2 - Cartão de Crédito Parcelado 
9 - Sair
'''
)

class Recibo:

    def __init__(self, datacompra,horacompra, meiodepagamento, valordacompra, valordoMDR, valorliquido, datadecredito):
        self.datacompra = datacompra
        self.horacompra = horacompra
        self.meiodepagamento = meiodepagamento
        self.valordacompra = valordacompra
        self.valordoMDR = valordoMDR
        self.valorliquido = valorliquido
        self.datadecredito = datadecredito

    def imprimirrecibo(self):
        return f'''=============================================================
    Data da compra: {self.datacompra}
    Hora da compra: {self.horacompra}
    Meio de pagamento: {self.meiodepagamento}
    Valor da Compra: R${self.valordacompra:.2f}
    Valor do MDR (taxa de transação): R${self.valordoMDR:.2f}
    Valor líquido: {self.valorliquido:.2f}
    Data de crédito: {self.datadecredito}
        =============================================================
    '''   

class ReciboParcelado:

    def __init__(self, datacompra,horacompra, meiodepagamento, valordacompra, valordoMDR, valorliquido, datadecredito, quantidadeParcelas, valorParcelas):
        self.datacompra = datacompra
        self.horacompra = horacompra
        self.meiodepagamento = meiodepagamento
        self.valordacompra = valordacompra
        self.valordoMDR = valordoMDR
        self.valorliquido = valorliquido
        self.datadecredito = datadecredito
        self.quantidadeParcelas = quantidadeParcelas
        self.valorParcelas = valorParcelas

    def imprimirreciboparcelado(self):
        if quantidadeParcelas == (2):
            return f'''=============================================================
    Data da compra: {self.datacompra}
    Hora da compra: {self.horacompra}
    Meio de pagamento: {self.meiodepagamento}
    Valor da Compra: R${self.valordacompra:.2f}
    Valor do MDR (taxa de transação): R${self.valordoMDR:.2f}
    Valor líquido: {self.valorliquido:.2f}
    Parcela: 1/2
    Valor líquido: {self.valorParcelas:.2f}
    Data de crédito: {self.datadecredito}
    Parcela: 2/2
    Valor líquido: {self.valorParcelas:.2f}
    Data de crédito: {self.datadecredito}
        =============================================================
    '''   
        elif quantidadeParcelas == (3):
            return f'''=============================================================
    Data da compra: {self.datacompra}
    Hora da compra: {self.horacompra}
    Meio de pagamento: {self.meiodepagamento}
    Valor da Compra: R${self.valordacompra:.2f}
    Valor do MDR (taxa de transação): R${self.valordoMDR:.2f}
    Valor líquido: {self.valorliquido:.2f}
    Parcela: 1/3
    Valor líquido: {self.valorParcelas:.2f}
    Data de crédito: {self.datadecredito}
    Parcela: 2/3
    Valor líquido: {self.valorParcelas:.2f}
    Data de crédito: {self.datadecredito}
    Parcela: 3/3
    Valor líquido: {self.valorParcelas:.2f}
    Data de crédito: {self.datadecredito}
        =============================================================
    '''   


def escolhaMeioPagamento():
    meioDePagamento = int(input("Escolha o meio de pagamento: "))
    return meioDePagamento

def mensagemInvalida():
    print("Opção Inválida!")

def valorCompra():
    valorCompra = float(input("Valor da compra: "))
    valor = valorCompra
    return valor

def quantidadeParcelas():
    quantidadeParcelas = int(input("Quantidade de Parcelas 2x ou 3x: "))
    return quantidadeParcelas

def printquantidadeparcelas(quantidadeparcelas):
    
    for i in range(1, quantidadeparcelas +1):
        print(f"Parcela: {i}/{quantidadeparcelas}")

def validaMeioPagamento():
    meioPagamento = escolhaMeioPagamento()
    opcoesPagamento = [0, 1, 2, 9]

    while meioPagamento not in opcoesPagamento:
        mensagemInvalida()
        validaMeioPagamento()    
    pass   
    meioSelecionado = meioPagamento
    return(meioSelecionado)

def MDR (valorcompra, opcaoPagamento):
    MDR = (valorcompra * opcaoPagamento) / 100
    return(MDR)

def validaData(opcaoPagamento):
    
    if opcaoPagamento == (1):
        
        if diaDaSemana == (5):
            dataDebito = dataHoje + timedelta(days=2)
            dataDebitoFormatada = dataDebito.strftime("%d/%m/%Y")
            return(dataDebitoFormatada)
        elif diaDaSemana != (5):
            dataDebito = dataHoje + timedelta(days=1)
            if dataDebito.weekday() == (5):
                dataDebito = dataDebito + timedelta(days=2)
            dataDebitoFormatada = dataDebito.strftime("%d/%m/%Y")
            return(dataDebitoFormatada)
    
    elif opcaoPagamento == (5):
     
        if diaDaSemana == (5):
            dataDebito = dataHoje + timedelta(days=32)
            dataDebitoFormatada = dataDebito.strftime("%d/%m/%Y")
            return(dataDebitoFormatada)
        elif diaDaSemana != (5):
            dataDebito = dataHoje + timedelta(days=31)
            if dataDebito.weekday() == (5):
                dataDebito = dataDebito + timedelta(days=32)
            dataDebitoFormatada = dataDebito.strftime("%d/%m/%Y")
            return(dataDebitoFormatada)

def pagamento():
    meio = validaMeioPagamento()
    
    if meio == (0):
        formaPagamento = "0 - Cartão de Débito"
        opcaoPagamento = 1
        valorcompra = valorCompra()
        taxa = MDR(valorcompra, opcaoPagamento)
        valorLiquido = valorcompra - taxa
        data = validaData(opcaoPagamento)

        recibo = Recibo(dataHojeFormatada, horaFormatada, formaPagamento, valorcompra, taxa, valorLiquido, data)

        print(recibo.imprimirrecibo())
    
    elif meio == (1):
        formaPagamento = "1 - Cartão de Crédito à Vista"
        opcaoPagamento = 5
        valorcompra = valorCompra()
        taxa = MDR(valorcompra, opcaoPagamento)
        valorLiquido = valorcompra - taxa
        data = validaData(opcaoPagamento)
        
        recibo = Recibo(dataHojeFormatada, horaFormatada, formaPagamento, valorcompra, taxa, valorLiquido, data)

        print(recibo.imprimirrecibo())
        
    elif meio == (2):
        formaPagamento = "2 - Cartão de Crédito Parcelado"
        opcaoPagamento = 5
        valorcompra = valorCompra()
        quantidadeparcelas = quantidadeParcelas()
        
        while quantidadeparcelas <2 or quantidadeparcelas >3:
            mensagemInvalida()
            quantidadeparcelas = quantidadeParcelas()
        taxa = MDR(valorcompra, opcaoPagamento)
        valorLiquido = valorcompra - taxa
                
        valorParcelas = round(valorLiquido / quantidadeparcelas, 2)
        
        data = validaData(opcaoPagamento)
        
        recibo = ReciboParcelado(dataHojeFormatada, horaFormatada, formaPagamento, valorcompra, taxa, valorLiquido, data, quantidadeparcelas, valorParcelas)

        print(recibo.imprimirreciboparcelado())

    elif meio == (9):
        print("Fim da operação")
    quit()

pagamento()