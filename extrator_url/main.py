#url = ""
url = "     "

url = url.strip()

if url == "":
    raise ValueError('a url esta vazia')

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]

url_paramentro = url[indice_interrogacao+1:]
print(url_paramentro)

parametro_busca = 'quantidade'
indice_paramentro = url_paramentro.find(parametro_busca)
indice_valor = indice_paramentro + len(parametro_busca) + 1
indice_final = url_paramentro.find('&',indice_valor)
if indice_final == -1:
    valor = url_paramentro[indice_valor:]
else:
    valor = url_paramentro[indice_valor:indice_final]
print(valor)