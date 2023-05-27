#       *args =  parametro que ira juntos todos os argumentos dentro de uma tuple
#        util para que a função possa aceitar uma variedade de argumentos

#def add(*stuff):
 #   sum = 0
 #   stuff = list(stuff)
 #   stuff[5] = 0
 #   for i in stuff:
 #       sum += i
#    return sum

#print(add(1,2,3,4,5,6))


#       **kwargs = parametro que vai juntar todos os parametros em um dicionario
#       util para aceitar diferentes keywords

def hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title="Mr.",first="Guilherme",middle="Vieira",last="Pereira")