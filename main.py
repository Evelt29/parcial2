from lib import *

import openpyxl
import pandas as pd

num = int(input("¿Cuál es tu número? : "))
doc = input("¿Cual es el nombre del archivo a procesar? : (xlsx)")
datos = pd.read_excel('datos-Eval-2.xlsx') #index_col =0,  engine ='openpyxl'
print(datos)
print("-------------------------------------------------------------------------------------------")




#------------------------ARBOL SIMETRICO-----------------------------------------------
arrayNum= datos
nodoRaiz = nodo(arrayNum[0])


for i in range(1, len(arrayNum),1):
    agregaNodos(nodoRaiz, arrayNum[i])
printArbol(nodoRaiz)

#---------IN ORDER ----------------
inOrderArr = []
LVR(nodoRaiz, inOrderArr)
print("InOrder:", end=" ")
print(inOrderArr)

#------------PRE ORDER-------------
preOrderArr = []
VLF(nodoRaiz, preOrderArr)
print("PreOrder:", end=" ")
print(preOrderArr)

#----------- POST ORDER-------------
postOrderArr = []
LRV(nodoRaiz, postOrderArr)
print("PostOrder:", end=" ")
print(postOrderArr)


#---------------------------------------------------
arrNodos = []
nodoRaiz = num
for i in range (0,len(arrNodos),1):
    if i == 0:
        nodoRaiz = nodo(arrNodos[i])
    else:
        nodosOrdenados(nodoRaiz,nodo(arrNodos[i]))
    pass
     
printArbol(nodoRaiz)
LVR(nodoRaiz, inOrderArr)
print(inOrderArr)




