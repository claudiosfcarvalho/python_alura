from validador_url import valida_composicao_url


def sanitiza_url(url):
    if type(url) == str:
        return url.strip()
    else:
        return ""


def valida_url(url):
    print(f'Valida URL: {url}')
    if not url:
        raise ValueError("A URL está vazia")
    valida_composicao_url(url)


class ExtratorURL:
    def __init__(self, url):
        self.url = sanitiza_url(url)
        print(f'URL Sanitizada: {self.url}')
        valida_url(self.url)

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        print(f'URL BASE: {url_base}')
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        print(f'URL PARAMETROS: {self.get_url_parametros()}')
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        #                                        busca valor & a partir do indice_valor
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
