url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"


indice_fatiamento = url.find('?')
url_base = url[0:indice_fatiamento]


url_parametros = url [indice_fatiamento +1:indice]
print(url_parametros)

parametros_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametros_busca)

print(indice_fatiamento)

