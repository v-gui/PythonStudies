# exception = eventos dectados durnte a execução que interrompe a fluidez do programa

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    #print(e)
    print("You can't divide by zero! Idiot! ")
except ValueError as e:
    #print(e)
    print("Enter only numbers plz")
except Exception as e:
    #print(e)
    print("Something went wrong *_*")
else:
     print(result)
finally:
    print("This will always execute") # normalmente usado para fechar *FILES