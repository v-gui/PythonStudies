import re

def separar_endereco(endereco):
    nome_rua = ''
    numero_rua = ''

    # Expressões regulares para identificar padrões de endereço
    padrao_numero = r'\b\d+\b'  # Padrão para encontrar números
    padrao_letras = r'[a-zA-Z]+'  # Padrão para encontrar letras

    # Procurando por padrões de número e letras no endereço
    numeros = re.findall(padrao_numero, endereco)
    letras = re.findall(padrao_letras, endereco)


    nome_rua = " ".join(letras)
    if numeros:
        numero_rua = numeros[-1]

    # Função especifica no caso de haver "No", recorta tudo oque aparecer antes de No como nome_rua
    if " No" in endereco:
        index_no = endereco.find(" No")
        nome_rua = endereco[:index_no].strip()
        numero_rua = endereco[index_no:].strip()

    return [nome_rua, numero_rua]

# Testando com os exemplos fornecidos

print(separar_endereco("4, Rue de la République"))
print(separar_endereco("100 Broadway Av"))
print(separar_endereco("Calle Sagasta, 26"))
print(separar_endereco("Calle 44 No 1991"))

# Para esses casos mais especificos, o 2° código resolve a maioria dos problemas, apenas quando no caso os números vem na frente no input, não consegui resolver por lá.

#Então usei essa biblioteca RE, que padroniza diferentes tipos de endereço,
# fiz as mudanças nos dois casos onde o número vem no inicio do input, para que o número encontrado fosse colocado ao final da string


