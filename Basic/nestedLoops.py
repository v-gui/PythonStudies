#nested loops = o loop interno vai terminar todas as interações antes de terminar as interações do loop externo

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use:")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #  end= "" = >> impede que o cursor pule a linha
    print()