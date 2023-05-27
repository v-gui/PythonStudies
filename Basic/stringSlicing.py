#               criar uma substring extraindo elementos de outra string
#                                   index[] ou slice ()

#                                   [start:stop:step]

#name = "Guilherme Vieira"

#first_name = name[0:9]
#last_name = name[10:]
#funky_name = name[0:16:1]  #step = literalmente pular as casas, letras (1 é o padrão)
#reversed_name = name[::-1]

#print(reversed_name)


website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)
# já que o tamanho dos sites varia muito, você utiliza o index negativo para retirar o final do site que costuma ser igual

print(website1[slice])
print(website2[slice])

