from datetime import datetime, timedelta

dataHoje = datetime.today()

dataHojeFormatada = dataHoje.strftime("%d/%m/%Y")

horaFormatada = dataHoje.strftime("%H:%M")

diaDaSemana = dataHoje.weekday()

class Recibo:

    def __init__(self, datacompra,horacompra, meiodepagamento, valordacompra, valordoMDR, valorliquido, datadecredito ):
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

def escolhaMeioPagamento():
    meioDePagamento = int(input("Escolha o meio de pagamento: "))
    return meioDePagamento

def mensagemInválida():
    print("Opção Inválida!")

def valorCompra():
    valorCompra = float(input("Valor da compra: "))
    valor = valorCompra
    return valor

def validaMeioPagamento():
    meioPagamento = escolhaMeioPagamento()
    opcoesPagamento = [0, 1, 2, 9]

    while meioPagamento not in opcoesPagamento:
        mensagemInválida()
        validaMeioPagamento()    
    pass   
    meioSelecionado = meioPagamento
    return(meioSelecionado)

def validaData():
     
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

def pagamento():
    meio = validaMeioPagamento()
    formaPagamento = "0 - Cartão de Débito"
    
    if meio == (0):
        valorcompra = valorCompra()
        MDR = (valorcompra * 1) / 100 
        valorLiquido = valorcompra - MDR
        data = validaData()

        recibo = Recibo(dataHojeFormatada, horaFormatada, formaPagamento, valorcompra, MDR, valorLiquido, data)

        print(recibo.imprimirrecibo())      

    elif meio == (9):
        print("Fim da operação")
    quit()

pagamento()

     





