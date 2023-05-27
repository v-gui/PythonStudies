#   scope = a região que a variavel é reconhecida
#   a variavel só está disponivel dentro da regiao que foi criada
#   Uma versão Global e Local podem ser criadas.

name = "Vieirinha"  #Global disponivel dentro de todas as funções

def display_name():
    name = "Guilherme"  #local só disponivel dentro dessa função
    print(name)

display_name()
print(name)