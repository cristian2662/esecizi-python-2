#!/usr/bin/python
import fnmatch
import os

def intero():
    numero = int(input("Inserire un numero: "))
    if numero <= 1:
        print("Devi inserire un numero maggiore di 1")
    else:
        div, count = 2, 0
        while div <= numero / 2 and count == 0:
         if numero % div == 0:
            count += 1
            div += 1
        if count == 0:
             print("1 !")
        else:
            print("0 !")

intero()


n=input("inserisci nome file")
file= open("C:\Users\CPioli\Desktop\esercizi2\es11\ "+ str(n), "r")

for i in file:
    numero = int(input("Inserire un numero: "))
    if numero <= 1:
        print("Devi inserire un numero maggiore di 1")
    else:
        div, count = 2, 0
        while div <= numero / 2 and count == 0:
            if numero % div == 0:
                count += 1
                div += 1
        if count == 0:
            print("primo")
print("numero di interi presenti"+str(i)
              