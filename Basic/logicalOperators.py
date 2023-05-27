# operadores lógicos (and, or,not) = usados para verificar se dois ou mais argumentos condicionais são verdadeiros

temp = int(input("What is the temperature outside?: "))
if temp >= 0 and temp <= 30: # as duas necessitam ser verdadeiras
    print("The temperature is great today!")
    print("Let's play outside.")
else:
    print("I think it's better if we stay inside today")

if temp < 0 or temp > 30:  # não há necessidade das duas serem verdadeiras
    print("where're we going them?")

#not   trocar entre verdadeiras por falsas
