
file = open("testo.txt")
y = file.read()

def reverse_string(y):
    if len(y) == 0:
        return y
    else:
        return reverse_string(y[1:]) + y[0]
    
print("-------------------------")
print("il file originale e': \n", end="")
print(y)
print("-------------------------")

print("il file al contrario e': \n", end="")
print(reverse_string(y))