# tuple = coleção ordenada e não modificada.
# usada para agrupar um grupo de dados.

student = ("Vieira",23,"male")

print(student.count("Vieira"))
print(student.index("male"))

for x in student:
    print (x)


if "Vieira" in student:
    print("Vieira está aqui")