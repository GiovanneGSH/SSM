# Giovanne Silveira Henrique - RGM: 000000000
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
meioDePagamento = int(input("Escolha o meio de pagamento: "))
meioSelecionado = meioDePagamento
MDR = 0
valorCompra = 0
valorLiquido = valorCompra - MDR
quantidadeParcelas = 0
valorParcelado = 0

while meioSelecionado !=(0) and meioSelecionado !=(1) and meioSelecionado !=(2) and meioSelecionado !=(9):
    print("Opção Inválida")
    meioDePagamento = int(input("Escolha o meio de pagamento: "))
    meioSelecionado = meioDePagamento   

if meioSelecionado == (0):   
    valorCompra = float(input("Valor da compra: "))
    MDR = (valorCompra * 1) / 100 
    valorLiquido = valorCompra - MDR
        
    if diaDaSemana == (5):
        dataDebito = dataHoje + timedelta(days=2)
        dataDebitoFormatada = dataDebito.strftime("%d/%m/%Y")

    elif diaDaSemana != (5):
        dataDebito = dataHoje + timedelta(days=1)
        dataDebitoFormatada = dataDebito.strftime("%d/%m/%Y")        

        print(
            f'''=============================================================
        Data da compra: {dataHojeFormatada}
        Hora da compra: {horaFormatada}
        Meio de pagamento: 0 - Cartão de Débito
        Valor da Compra: R${valorCompra:.2f}
        Valor do MDR (taxa de transação): R${MDR:.2f}
        Valor líquido: {valorLiquido:.2f}
        Data de crédito: {dataDebitoFormatada}
        =============================================================
    ''')       

elif meioSelecionado == (1):
    valorCompra = float(input("Valor da compra: "))
    MDR = (valorCompra * 5) / 100
    valorLiquido = valorCompra - MDR

    if diaDaSemana == (5):
        dataDebito = dataHoje + timedelta(days=2)
        dataDebitoFormatada = dataDebito.strftime("%d/%m/%Y")

    elif diaDaSemana != (5):
        dataDebito = dataHoje + timedelta(days=1)
        dataDebitoFormatada = dataDebito.strftime("%d/%m/%Y")        

    print(
    f'''=============================================================
    Data da compra: {dataHojeFormatada}
    Hora da compra: {horaFormatada}
    Meio de pagamento: 1 - Cartão de Crédito à Vista
    Valor da Compra: R${valorCompra:.2f}
    Valor do MDR (taxa de transação): R${MDR:.2f}
    Valor líquido: {valorLiquido:.2f}
    Data de crédito: {dataDebitoFormatada}
        =============================================================
    ''')     
            
elif meioSelecionado == (2):
    valorCompra = float(input("Valor da compra: "))
    MDR = (valorCompra * 5) / 100
    valorLiquido = valorCompra - MDR
    quantidadeParcelas = int(input("Quantidade de Parcelas 2x ou 3x: "))
    
    if quantidadeParcelas <2 or quantidadeParcelas >3:
        
        while quantidadeParcelas <2 or quantidadeParcelas >3:
            print("Quantidade Inválida")
            quantidadeParcelas = int(input("Quantidade de Parcelas 2x ou 3x: "))   

    valorParcelado = round(valorLiquido / quantidadeParcelas, 2)

    provaReal = valorParcelado * quantidadeParcelas
    restoDivisao = round(valorLiquido - provaReal, 2)

    primeiraParcela = round(valorParcelado + restoDivisao, 2)       
        
    if quantidadeParcelas == (2):
            
        dataCredito = dataHoje + timedelta(days=30)
        validaDataCredito = dataCredito.weekday()
            
        if validaDataCredito == (5):
            dataCredito = dataHoje + timedelta(days=32)
            dataCreditoFormatada = dataCredito.strftime("%d/%m/%Y")
        elif validaDataCredito !=(5):
            dataCredito = dataHoje + timedelta(days=31)
            dataCreditoFormatada = dataCredito.strftime("%d/%m/%Y")

        dataSegundoCredito = dataHoje + timedelta(days=60)
        validaSegundoCredito = dataSegundoCredito.weekday()

        if validaSegundoCredito == (5):
            dataSegundoCredito = dataHoje + timedelta(days=62)
            dataSegundoCreditoFormatada = dataSegundoCredito.strftime("%d/%m/%Y")
        elif validaDataCredito !=(5):
            dataSegundoCredito = dataHoje + timedelta(days=61)
            dataSegundoCreditoFormatada = dataSegundoCredito.strftime("%d/%m/%Y")

            print(
                f'''=============================================================
            Data da compra: {dataHojeFormatada}
            Hora da compra: {horaFormatada}
            Meio de pagamento: 2 - Cartão de Crédito Parcelado
            Valor da Compra: R${valorCompra:.2f}
            Valor do MDR (taxa de transação): R${MDR:.2f}
            Valor líquido: {valorLiquido:.2f}
            Parcela: 1/2
            Valor líquido: R${primeiraParcela:.2f}
            Data de Crédito: {dataCreditoFormatada}
            Parcela: 2/2
            Valor líquido: R${valorParcelado:.2f}
            Data de Crédito: {dataSegundoCreditoFormatada}    
            =============================================================
        ''')   
                    
    elif quantidadeParcelas == (3):
            
        dataCredito = dataHoje + timedelta(days=30)
        validaDataCredito = dataCredito.weekday()
            
        if validaDataCredito == (5):
            dataCredito = dataHoje + timedelta(days=32)
            dataCreditoFormatada = dataCredito.strftime("%d/%m/%Y")
        elif validaDataCredito !=(5):
            dataCredito = dataHoje + timedelta(days=31)
            dataCreditoFormatada = dataCredito.strftime("%d/%m/%Y")

        dataSegundoCredito = dataHoje + timedelta(days=60)
        validaSegundoCredito = dataSegundoCredito.weekday()

        if validaSegundoCredito == (5):
            dataSegundoCredito = dataHoje + timedelta(days=62)
            dataSegundoCreditoFormatada = dataSegundoCredito.strftime("%d/%m/%Y")
        elif validaDataCredito !=(5):
            dataSegundoCredito = dataHoje + timedelta(days=61)
            dataSegundoCreditoFormatada = dataSegundoCredito.strftime("%d/%m/%Y")

        dataTerceiroCredito = dataHoje + timedelta(days=90)
        validaTerceiroCredito = dataTerceiroCredito.weekday()

        if validaTerceiroCredito == (5):
            dataTerceiroCredito = dataHoje + timedelta(days=92)
            dataTerceiroCreditoFormatada = dataTerceiroCredito.strftime("%d/%m/%Y")
        elif validaDataCredito !=(5):
            dataTerceiroCredito = dataHoje + timedelta(days=91)
            dataTerceiroCreditoFormatada = dataTerceiroCredito.strftime("%d/%m/%Y")

            print(
                f'''=============================================================
            Data da compra: {dataHojeFormatada}
            Hora da compra: {horaFormatada}
            Meio de pagamento: 2 - Cartão de Crédito Parcelado
            Valor da Compra: R${valorCompra:.2f}
            Valor do MDR (taxa de transação): R${MDR:.2f}
            Valor líquido: {valorLiquido:.2f}
            Parcela: 1/3
            Valor líquido: R${primeiraParcela:.2f}
            Data de Crédito: {dataCreditoFormatada}
            Parcela: 2/3
            Valor líquido: R${valorParcelado:.2f}
            Data de Crédito: {dataSegundoCreditoFormatada}   
            Parcela: 3/3
            Valor líquido: R${valorParcelado:.2f}
            Data de Crédito: {dataTerceiroCreditoFormatada}  
            =============================================================
        ''')  
             
elif meioSelecionado == (9):
    print("Fim da operação")
    quit()            


    






