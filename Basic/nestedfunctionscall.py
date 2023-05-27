#   nested functions calls = funções chamada dentro de outra função
#                            funções internas são realizadas primeiro
#                            valor retornado é utilizado como argumento para a função externa

#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))