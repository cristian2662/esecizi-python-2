file = open("testo.txt")
y = file.read()

def bubblesort(y):
    swapped = False
    for n in range(len(y) - 1, 0, -1):
        for i in range(n):
            if len(y)> 1:
                swapped = True


        if not swapped:
            return

print("lista non modificata,")
print(y)
bubblesort(y)
print("-----------------")
print("lista in ordine crescente, ")
print(y)

if len(y)%2:
    print("parola a cifra pari, nessuna parola stampata")
else:
    print("ecco le parole con cifre dispari"+str(y))

