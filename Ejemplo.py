archivo = "b_small.txt" #Nombre del archivo
f = open(archivo) #Cargar archivo
lista = f.readlines()
f.close()
input1 = lista[0].split() #Toma el tipo de pizzas y el número de rebanadas 
input2 = lista[1].split() #Toma las rebanadas de y los tipos de pizzas disponibles.

# FUNCIÓN PARA PASAR LA LISTA DE CARACTERES A ENTEROS
def convertir(n):
    intn=[]
    for p in n:
        intn.append(int(p))
    return intn

def puntaje(n):
    puntos=0
    for p in n:
        puntos=puntos+p
    return puntos

input1 = convertir(input1) #Lista con valores enteros
input2 = convertir(input2) #Lista con valores enteros
input2.sort(reverse = True) #Ordeno de mayor a menor
N = input1[1] #Número de Pizzas
M = input1[0] #Número de rebanadas

print(f"Número de tipos de Pizzas posibles: {N}")
print(f"Número máximo de rebanadas: {M}")

listaI = [] #Lista del número de rebanadas
listaII = [] #De los tipos de pizzas que se seleccionan

Tipo = 0 # Cantidad de Pizzas que se seleccionan

for p in input2:
    if p < M and Tipo < M:
        M = M-p
        Tipo = Tipo+1
        listaI.append(p)
        listaII.append((len(input2)-1)-input2.index(p))
    else:
        M = M
        Tipo = Tipo

puntos = puntaje(listaI) #Puntaje obtenido
listaI.sort(reverse = False)
listaII.sort(reverse = False)

print(f"puntaje: {puntos}")
print(f"Cantidad de Pizzas: {Tipo}")
print(f"Rebanadas: {listaI}")
print(f"Tipos de Pizza: {listaII}")