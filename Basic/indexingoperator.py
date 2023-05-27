#index operator[] = da acesso a uma sequencia de elementos (str,list,tuples)

name = "guilherme vieira!"

#if(name[0].islower()):
  #  name = name.capitalize()

first_name = name[:9].upper()
last_name = name[10:].capitalize()
last_character = name[-1]

print(first_name + " " + last_name)
print(last_character)