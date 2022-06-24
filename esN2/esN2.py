#prova numeri
file1 = open("esN2_int.txt")
y = file1.read()
print("-------------------------")
print(y)
print("-------------------------")

#prova stringhe
file = open("esN2_string.txt")
x = file.read()
print("-------------------------")
print(x)
print("-------------------------")

if len(x)>5:
    with open("Long.txt", "w") as text_file:
        text_file.write("STRINGHE SOPRA I 5 CARATTERI: %s\n" % x)

if len(x)<5:
    with open("Short.txt", "w") as text_file:
        text_file.write("STRINGHE SOTTO I 5 CARATTERI: %s\n" % x)
