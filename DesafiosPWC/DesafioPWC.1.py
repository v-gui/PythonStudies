def separar_endereco(endereco):
    return [endereco.replace(" ", ",")]


# Testando com os exemplos fornecidos

print(separar_endereco("Miritiba 339"))
print(separar_endereco("Babaçu 500"))
print(separar_endereco("Cambuí 804B"))

# Maneira mais simples que consegui resolver para o primeiro caso,
# Apenas trocando o "Espaço" no input por uma virgula para arrumar o output final.
# Só funciona nesses casos porque estão padronizados com apenas um espaço.
