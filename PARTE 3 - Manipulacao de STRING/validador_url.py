import re


def valida_composicao_url(url):
    print(f'Valida composição da url {url}')
    padrao = re.compile(
        "(http(s)?://)?(www.)?[a-z|0-9]*(.com)(.br)?(/)[a-z|0-9]*([?]([a-z|A-Z|0-9]*[=]?[a-z|A-Z|0-9]*[&]?)*)+")
    busca = padrao.search(url)
    print(f'retorno search url {busca}')
    if busca:
        valor = busca.group()
        print(f'regex achou: {valor}')
    else:
        print('erroooo')
