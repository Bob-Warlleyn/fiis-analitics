import requests
from scrapybob import calculosFundos
def getResponse(fundo):
    url = "https://www.fundsexplorer.com.br/funds/" + fundo
    method = "GET"

    response = requests.request(method, url)
    return response.text

def getReal(response, startIndex):
    contador = 1
    while True:
        valor = response[startIndex + contador]
        try:
            real = int(valor)
            return startIndex + contador
        except:
            contador += 1

def getType(response, startIndex):
    for i in range(1, 12):
        valor = response[startIndex + i]
        if(valor == 'M' or valor == 'K' or valor == 'B'):
            return startIndex + i
    return ''

def getEndValue(response, startIndex):
    for i in range(1, 20):
        valor = response[startIndex + i]
        if(valor == ' ' or valor == '\t' or valor == '\b' or valor == '<'):
            return startIndex + i - 1

def getByValue(response, title):
    index = response.index(title)
    indexValor = getReal(response, index)
    indexEndValor = getType(response, indexValor)

    if(indexEndValor == ''):
        indexEndValor = getEndValue(response, indexValor)

    return response[indexValor: indexEndValor + 1]

def formatBilhion(number):
    posicaoPontoDois = number.find(".", number.find(".") + 1)

    if(posicaoPontoDois == -1):
        return number
    numberWithoutPoint = number[:posicaoPontoDois] + number[posicaoPontoDois + 1:]

    return numberWithoutPoint

def getPoints(fundo):
    response = getResponse(fundo)

    liqMedDia = getByValue(response, 'Liquidez Média Diária')
    ultRend = getByValue(response, 'Último Rendimento')
    divYeld = getByValue(response, 'Dividend Yield')
    patrimoLiq = getByValue(response, 'Patrimônio Líquido')
    vlPatrimo = getByValue(response, 'Valor Patrimonial')
    rentMes = getByValue(response, 'Rentab. no mês')
    pvp = getByValue(response, 'P/VP')
    cotasEmitidas = formatBilhion(getByValue(response, 'Cotas emitidas'))
    cotistas = getByValue(response, 'Número de cotistas')

    print(f'''
Fundo em analise: {fundo.upper()}, Numero de cotistas: {cotistas}, Cotas emitidas: {cotasEmitidas}
Liquidez Media: {liqMedDia}, Ultimo Rendimento: {ultRend}, Div. yeld: {divYeld}
Patrimonio Liquido: {patrimoLiq}, Valor Patrimonial: {vlPatrimo}, Rent. Mes: {rentMes}, Pvp: {pvp}''')

    pontuacao = calculosFundos.calcuFundos(liqMedDia,
                ultRend,
                divYeld,
                patrimoLiq,
                vlPatrimo,
                rentMes,
                pvp,
                cotasEmitidas,
                cotistas)

    print('\n')
    print(f'Pontuacao Final do fundo {fundo.upper()}: ', pontuacao)
    print('\n')

    if (pontuacao == 16):
        print('Esse fundo é incrivel e atende todas as espectativas desejadas')
    elif (pontuacao > 10 and pontuacao < 16):
        print('Esse fundo atende bons criterios de avalição')
    elif (pontuacao == 10):
        print('Esse fundo atende a media em todos os parametros calculados.')
    elif (pontuacao >= 6 and pontuacao < 10):
        print('Esse fundo atende bem alguns pontos calculados mas deixa a desejar em outros. Necessita de ateçao especial')
    elif (pontuacao < 6):
        print('Fundo não recomendado para compra')

# fundo = input('Digite o nome do fundo: ')
# while True:
#     fundo = fundo.lower()
#     try:
#         getPoints(fundo)
#     except:
#         print('\n')
#         print('Fundo nao encontrado')
#
#     print('\n')
#     fundo = input('Bora pro proximo fundo: ')
#     if(fundo == 'EXIT' or fundo == 'exit'):
#         break


