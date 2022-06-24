diz={"melanzane": 3, "zucchine": 3, "cavoli": 2, "arance": 1, "anguria": 10, "banane": 1, "insalata": 2, "pomodori": 2}
print("")
print("seleziona tra: "+"melanzane,"+" zucchine,"+" cavoli,"+" arance,"+" anguria,"+" banane,"+" insalata,"+ " pomodori")
a = input("quale articolo vuoi comprare?\n")
"""""
if(a!="melanzane"):
elif(a!="zucchine"):
 elif(a!="cavoli"):
 elif(a!="arance"): 
 elif(a!="anguria"):
    elif(a!="banane"):
  elif(a!="insalata"):
 elif(a!="pomodori"):
 print("***ERRORE, elemento non presente nel dizionario***")
"""""
v = int(diz.get(a))
#print(v)
p = int(input("quanti prodotti vuoi inserire?\n"))
tot=p*diz.get(a)
print("costo al pezzo: "+str(diz.get(a)))
print("quantità: "+str(p))
print("totale speso: "+str(tot)+ " euro")


"""""
scelta=-1
while(scelta != 0):
    print("-------------------------")
    print("MENU DI SCELTA")
    print("0. Uscita")
    print("1. scegli prodotto")
    print("2. inserisci più prodotti")
    scelta=input("Scegli: ")
    print("-------------------------")

    if(scelta == 0):
        print("***programma chiuso con successo***")
        pass

    elif (scelta == 1):
        a=print("quale articolo vuoi comprare?")
        v=diz.get(a)

    elif(scelta == 2):
        p = print("quanti prodotti vuoi inserire?")
        tot=p*diz.get(a)
        print("quantità: "+str(p))
        print("totale speso: "+str(tot))
"""""