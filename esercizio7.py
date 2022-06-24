from array import array
import random

lista=[12,23,34,45,56,67,78,89,91,82,73,64,55,110]
i=0
for i in lista:
    print(i)

max=lista[0]
for i in lista:
    if i>max:
        max=i
print("numero massimo: "+str(max))

min=lista[0]
for i in lista:
    if i<min:
        min=i
print("numero minimo: "+str(min))
