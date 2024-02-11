def separar_endereco(endereco):
    nome_rua = ''
    numero_rua = ''
    numero = False

    for caractere in endereco:
        if caractere.isdigit() and not numero:
            numero = True
        if not numero and not caractere.isdigit() and not caractere == '' and not caractere == ', ':
            nome_rua += caractere
        elif numero:
            numero_rua += caractere

    if "No" in endereco:
        index_no = endereco.find("No")
        nome_rua = endereco[:index_no].strip()
        numero_rua = endereco[index_no:].strip()

    if ',' in endereco:
        return [nome_rua + numero_rua]
    else:
        return [nome_rua + ', ' + numero_rua]


def ajustar_endereco(endereco):
    endereco_parts = endereco.split(' ')
    if endereco_parts[0].isdigit() or (',' in endereco_parts[-1] and endereco_parts[-2].isdigit()):
        if endereco_parts[0].isdigit():
            numero_rua = endereco_parts[0]
            nome_rua = ' '.join(endereco_parts[1:])
        else:
            numero_rua = endereco_parts[-1]
            nome_rua = ' '.join(endereco_parts[:-1])
        return [nome_rua + ', ' + numero_rua]
    else:
        return [endereco]
# Testando com os exemplos fornecidos

print(separar_endereco("Miritiba 339"))
print(separar_endereco("Babaçu 500"))
print(separar_endereco("Cambuí 804B"))
print(separar_endereco("Rio Branco 23"))
print(separar_endereco("Quirino dos Santos 23 b"))
print(ajustar_endereco("4 Rue de la République"))
print(ajustar_endereco("100 Broadway Av"))
print(separar_endereco("Calle Sagasta, 26"))
print(separar_endereco("Calle 44 No 1991"))


#Para resolver os problemas quando o número vem na frente, foi criada outra função de ajustar a posição da string quando confirmar que o número vem primeiro
