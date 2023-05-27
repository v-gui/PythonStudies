# if statement = parte do código que sera executada se a condição for verdadeira

age = int(input("How old are you?:"))

if age > 100:
    print("Man u old as hell!")
elif age == 100:
    print("A hunnit ? thats crazy bro")
elif age >= 18:
    print("You are an adult!")
elif age <= 1:
    print("Man u're a newborn get out of the computer!")
elif age < 0:
    print("Man u not even born yet, how u typing that?")
else:
    print("You are a child!")