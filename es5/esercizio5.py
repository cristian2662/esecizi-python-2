
file= open ("trascrivi.txt", "w")
a=0
while a!='$':
    a=input("inserisci quello da trascrivere nel file di testo: \n")

print(a)
file.write(a)
file.close()

