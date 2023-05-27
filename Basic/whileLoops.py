# while loop = executar um loop enquanto a condição for verdadeira

#while 1==1:                                #loop infinito
  #  print("Help! I'm stuck in a loop!")

name = ""
while len(name) == 0:
    name = input("Enter your name: ")
print("Hello,"+name)