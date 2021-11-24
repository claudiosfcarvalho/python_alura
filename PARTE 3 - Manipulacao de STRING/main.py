from extrator_url import ExtratorURL

url = 'https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real  \t\n'
print(f'URL: >>{url}<<')

extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(f'quantidade: {valor_quantidade}')