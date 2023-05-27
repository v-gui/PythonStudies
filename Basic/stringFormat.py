# str.format() = método opcional que da aos usuários maior cotrole enquanto demonstra o output

#animal = "cow"
#item = "moon"

# print("The "+ animal+" jumped over the "+item) -- normal

#print("The {} jumped over the {}".format(animal, item))     # {} funciona como um placeholder, é atribuido em ordem.
#print("The {1} jumped over the {0}".format(animal, item))   # argumento posicional
#print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))   # argumento com chave KEY

#text = "The {} jumped over the {}"

#print(text.format(animal, item))

#----------------------------------------------------------------------------------------

#name = "Guilherme"
#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:20}. Nice to meet you".format(name))
#print("Hello, my name is {:<20}. Nice to meet you".format(name))
#print("Hello, my name is {:>20}. Nice to meet you".format(name))
#print("Hello, my name is {:^20}. Nice to meet you".format(name))

#----------------------------------------------------------------------------------------

number = 1000

print("The number pi is {:.2f}".format(number)) # numero de casas decimais
print("The number pi is {:,}".format(number))   # ,
print("The number pi is {:b}".format(number))   # binário
print("The number pi is {:o}".format(number))   # octadecimal
print("The number pi is {:x}".format(number))   # hexadecimal
print("The number pi is {:E}".format(number))   # notação cientifica
