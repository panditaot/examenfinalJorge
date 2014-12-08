#Los archivos se deben de encontrar en la misma carpeta

print("ingrese área de aspas:")
mts=int(input("área: "))
valor = float(mts*float(2.7))
print("el precio de su cantidad de mts^2 es: $"+str(round(valor),))


import re
print("Creando documento")
print("espere...")
clima = open("clima.csv","r")
generacion = open("generacion.csv","r")
resultados = open("resultadosultadosExamenFinal.csv","w")

l3 = []

for line in clima:
    lista = re.compile(r'\d*\-\d*\-\d*,\d*\,\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*\,\-?\d*')
    l2 = re.findall(lista, line)
    if l2 != []:
        l3.append(l2)

l4=[]
l5 =[]
for x in range(len(l3)):
    str(l3[x][0])
    l4 = l3[x][0].split(",")
    l5.append(l4)

lista6 =0
for x in range(len(l5)):
    lista6 = int((int(l5[x][17])/3.6))
    l5[x][17] = lista6

for x in range(len(l5)):
    if int(l5[x][17]) >= 23:
        l5[x][17] = 7452.3
    elif int(l5[x][17]) == 1:
        l5[x][17] = 0.6
    elif int(l5[x][17]) == 2:
        l5[x][17] = 4.9
    elif int(l5[x][17]) == 3:
        l5[x][17] = 16.5
    elif int(l5[x][17]) == 4:
        l5[x][17] = 39.2
    elif int(l5[x][17]) == 5:
        l5[x][17] = 76.5
    elif int(l5[x][17]) == 6:
        l5[x][17] = 132.3
    elif int(l5[x][17]) == 7:
        l5[x][17] = 210.1
    elif int(l5[x][17]) == 8:
        l5[x][17] = 313.6
    elif int(l5[x][17]) == 9:
        l5[x][17] = 446.5
    elif int(l5[x][17]) == 10:
        l5[x][17] = 612.5
    elif int(l5[x][17]) == 11:
        l5[x][17] = 815.2
    elif int(l5[x][17]) == 12:
        l5[x][17] = 1058.4
    elif int(l5[x][17]) == 13:
        l5[x][17] = 1345.7
    elif int(l5[x][17]) == 14:
        l5[x][17] = 1680.7
    elif int(l5[x][17]) == 15:
        l5[x][17] = 2067.2
    elif int(l5[x][17]) == 16:
        l5[x][17] = 2508.8
    elif int(l5[x][17]) == 17:
        l5[x][17] = 3009.2
    elif int(l5[x][17]) == 18:
        l5[x][17] = 3572.1
    elif int(l5[x][17]) == 19:
        l5[x][17] = 4201.1
    elif int(l5[x][17]) == 20:
        l5[x][17] = 4900
    elif int(l5[x][17]) == 21:
        l5[x][17] = 5672.4
    elif int(l5[x][17]) == 22:
        l5[x][17] = 6521.9
    else:
        ()

y = 0
valor = 0
for x in range(len(l5)):
    y = round((float(l5[x][17])*(0.0027)),4)
    l5[x][17] = y
    valor+= y
    

resultados.write("fecha, cantidad generada\n")
for x in range(len(l5)):
    resultados.write(str(l5[x][0])+","+str(l5[x][17])+"\n")


resultados.close()
generacion.close()
clima.close()

print("Terminado")

print("valor ahorrado durante al año: $"+str(round(valor,2)))

end = input("")
