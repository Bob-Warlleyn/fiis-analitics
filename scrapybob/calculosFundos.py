def getDecimalHouses(number):
    numberCalc = 0
    multiple = 0
    if(number.__contains__('B')):
        number = number.replace('B', '')
        numberCalc = 9
        multiple = 1000
    if(number.__contains__('M')):
        number = number.replace('M', '')
        numberCalc = 6
        multiple = 1
    if(number.__contains__('K')):
        number = number.replace('K', '')
        numberCalc = 3
        multiple = 1

    number = number.replace(' ', '')
    number = number.replace(',', '.')
    parteInteira, parteDecimal = number.split(".")
    parteDecimal += "0" * (numberCalc - len(parteDecimal))
    return parteInteira + "." + parteDecimal, multiple

def calcuFundos(liqMedDia,
                ultRend,
                divYeld,
                patrimoLiq,
                vlPatrimo,
                rentMes,
                pvp,
                cotasEmitidas,
                cotistas):

    minDivYeld = 3
    maxMedDivYeld = 6

    pontuacao = 0
    print('\n')
    print("Vamos aos calculos !! ")
    print('\n')

    print(f'''
    Dividend Yield...
        Valores considerados: 
            Minimo - {minDivYeld}
            Mediano - maior que {minDivYeld} e menor que {maxMedDivYeld} 
            Alto - maior que {maxMedDivYeld}
            Valor D.Y do fundo analisado: {divYeld} 
    Portando: ''')

    divYeld = float(divYeld.replace(',', '.'))
    if divYeld < minDivYeld:
        print('Dividend Yield abaixo do espero')
        print('Retirando 1 ponto')
        pontuacao -= 1
    elif divYeld > minDivYeld and divYeld <= maxMedDivYeld:
        print('Dividend Yield equilibrado')
        print('Adicionando 2 pontos')
        pontuacao += 2
    elif divYeld > maxMedDivYeld:
        print('Dividend Yield acima do esperado')
        print('Adicionando 3 pontos')
        pontuacao += 3

    print('Pontuacao: ', pontuacao)

    print('\n')

    minPvp = 1
    medPvp = 1.09

    print(f''' 
    Pvp...
        Valores considerados: 
            Minimo - {minPvp}
            Mediano - maior igual a {minPvp} e menor que {medPvp}
            Alto - maior igual a {medPvp} 
            Valor PVP do fundo analisado: {pvp} 
    Portando: ''')

    pvp = float(pvp.replace(',', '.'))
    if pvp < minPvp:
        print('Pvp avaliando ativo abaixo do seu valor patrimonial. Pode ser uma oportunidade, fique atento !!')
        print('Adiconando 3 pontos')
        pontuacao += 3
    elif pvp >= minPvp and pvp < medPvp:
        print("Pvp alinhado com o valor patrimonial")
        print('Adicionando 2 pontos')
        pontuacao += 2
    elif pvp >= medPvp:
        print('Pvp acima do esperado')
        print("Removendo 1 ponto")
        pontuacao -= 1

    print('Pontuacao: ', pontuacao)

    print('\n')

    rentMin = 1
    rentMed = 3

    print(f'''
    Rentabilidade mes...
        Valores considerados: 
            Minimo - {rentMin}
            Mediano - maior que {rentMin} e menor igual a {rentMed} 
            Alto - maior que {rentMed}
            Valor Rentabilidade Mes do fundo analisado: {rentMes} 

    Portando: ''')

    rentMes = float(rentMes.replace(',', '.'))
    if rentMes <= 0:
        print('Rentab. no mês negativa, performace inferior recente, sinal de atenção !!')
        print('Removendo 1 ponto')
        pontuacao -= 1
    elif rentMes <= rentMin and rentMes > 0:
        print('Rentab. no mês baixa, mas não negativa, sinal de atenção !!')
        print('Nenhum ponto adicionado')
    elif rentMes > rentMin and rentMes <= rentMed:
        print("Rentab. no mês media")
        print('Adicionando 2 pontos')
        pontuacao += 2
    elif rentMes > rentMed:
        print('Rentab. no mês acima do esperado')
        print('Adicionando 3 pontos')
        pontuacao += 3

    print('Pontuacao: ', pontuacao)

    print('\n')

    liqMin = 0.1
    liqMedia = 1

    liqMedDiaCalc = float(liqMedDia.replace(',', '.').replace('M', '').replace('K', ''))
    liqMedDiaCalc = round(liqMedDiaCalc / float(cotasEmitidas), 2)

    print(f'''
    Liquedez Media Dia...
        Valores considerados: 
            Minimo - {liqMin}
            Mediano - maior que {liqMin} e menor igual a {liqMedia} 
            Alto - maior que {liqMedia}
            Valor Liquidez Media divido pelo numero total de cotas emitidas do fundo analisado: {liqMedDiaCalc}
            Valor Liquidez media diaria do fundo: {liqMedDia}
            Valor do numero total de cotas emitidas do fundo: {cotasEmitidas}  
    Portando: ''')

    if liqMedDiaCalc > liqMedia:
        print('Liquidez media diaria alta')
        print('Adicionando 3 pontos')
        pontuacao += 3
    elif liqMedDiaCalc <= liqMedia and liqMedDiaCalc >= liqMin:
        print("Liquidez media diaria com uma boa media")
        print('Adicionando 2 pontos')
        pontuacao += 2
    elif liqMedDiaCalc < liqMin:
        print('Liquidez media diaria abaixo do esperado')
        print('Removendo 1 ponto')
        pontuacao -= 1

    print('Pontuacao: ', pontuacao)
    print('\n\n')

    patriLiqFormatado, multiple = getDecimalHouses(patrimoLiq)
    valorPatrimonioCalculado = round(float(patriLiqFormatado) / float(cotasEmitidas) * multiple, 2)

    print(f'''
    Calculo do valor patrimonial...
        Valores considerados: 
            Abaixo, acima ou de acordo com o patrimonio liquido divido pelo total de cotas
        Portando: ''')
    print(f'Valor da cota: {vlPatrimo} --- Valor esperado calculado: {valorPatrimonioCalculado}')
    vlPatrimo = float(vlPatrimo.replace(',', '.'))
    if valorPatrimonioCalculado > vlPatrimo:
        print('Valor do patrimonio calculado é maior que o vendido, fundo pode estar sendo vendido a baixo do preço !')
        print('Adicionando 3 pontos')
        pontuacao += 3
    elif valorPatrimonioCalculado < vlPatrimo:
        print(
            "Valor do patrimonio calculado é menor do que esta sendo vendido, pode não ser um bom momento para compra.")
        print('Removendo 1 pontos')
        pontuacao -= 1
    elif valorPatrimonioCalculado == vlPatrimo:
        print('Valordo patrimonio calculado esta de acordo com o valor que esta sendo vendido')
        print('Adicionando 2 pontos')
        pontuacao += 2

    return pontuacao