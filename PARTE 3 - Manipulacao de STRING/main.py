url = 'https://bytebank.com/cambio?moedaOrigem=real'

print(url)

# url_base = url[0:19]
# print(url_base)
#
# url_parametros = url[20:36]
# print(url_parametros)

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)
