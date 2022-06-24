import csv

print("File iniziale:")
with open('preventivo.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
partenza=1
tFinale=0
    if partenza!=1:
        p=float(row[1])
        q=float(row[2])
        t=p*q
print(t)

tFinale+=t





"""""
nome = row[0]
importo = row[1]
quantita = row[2]

tr=(float(importo)*float(quantita))
print(tr)
"""""


