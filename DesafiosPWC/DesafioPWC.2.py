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

# Testando com os exemplos fornecidos

print(separar_endereco("Miritiba 339"))
print(separar_endereco("Babaçu 500"))
print(separar_endereco("Cambuí 804B"))
print(separar_endereco("Rio Branco 23"))
print(separar_endereco("Quirino dos Santos 23 b"))
print(separar_endereco("Calle Sagasta, 26"))
print(separar_endereco("4, Rue de la République"))
print(separar_endereco("100 Broadway Av"))
print(separar_endereco("Calle Sagasta, 26"))
print(separar_endereco("Calle 44 No 1991"))


# Já no segundo caso, como há 2 itens com mais de um espaço, o código anterior não funciona mais.
# Para este caso criei duas strings, uma para o nome e outra para o número.

# A Função irá  usar um laço de repetição para ler cada caractere,
# separando o nome da rua até encontrar algum digito, o qual o mesmo irá indicar o número da rua.

# Contruindo strings diferentes e retornando-as como lista.
