from extrator_url import ExtratorURL

url = 'https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real  \t\n'
VALOR_DOLAR = 5.50 #em real
extrator_url = ExtratorURL(url)
print(f'Tamanho URL:{len(extrator_url)}')
print(extrator_url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(type(valor_quantidade))
valor_convertido =  float(valor_quantidade) * VALOR_DOLAR
print(f'Quantidade: R${valor_quantidade} \nConversão: ${valor_convertido}')

# extrator_url2 = ExtratorURL(url)
# print(extrator_url == extrator_url2)
# print(1 == True)
# print(1 is True)
# print(1 is 1)
# print(0 == False)
