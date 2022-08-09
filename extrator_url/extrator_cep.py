endereco = "Rua Benedito da Cunha Campos, 535, Jardim Nazareth, Mogi Mirim, Sp, 13806-610"

import re

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)

    