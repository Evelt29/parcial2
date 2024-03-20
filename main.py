from lib import *


"""
for indice, fila in data.iloc[:, 1:].iterrows():
    for nombre_columna, valor_celda in fila.items():
        if valor_celda == num:
            data.loc[indice, nombre_columna] = f"\033[31m{num}\033[30m"
            """
num = numero() 

doc = documento()
print(data.to_string(index = False))



#------------------------ARBOL SIMETRICO-----------------------------------------------
arrayNum= data.values.flatten().tolist()
nodoRaiz = nodo(arrayNum[0])


for i in range(0, len(arrayNum),1):
    agregaNodos(nodoRaiz, arrayNum[i])
printArbol(nodoRaiz)

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#---------IN ORDER ----------------
print("--------\033[43m\033[31m InOrder:\033[0m-----------")
inOrderArr = []
LVR(nodoRaiz, inOrderArr)
print("\033[35m InOrder:\033[0m", end=" ")
print(inOrderArr)

#------------PRE ORDER-------------
print("--------\033[43m \033[31mPreOrderArr \033[0m-----------")
preOrderArr = []
VLF(nodoRaiz, preOrderArr)
print("\033[35m PreOrder:\033[0m", end=" ")
print(preOrderArr)

#----------- POST ORDER-------------
print("--------\033[43m\033[31m PostOrderArr \033[0m-----------")
postOrderArr = []
LRV(nodoRaiz, postOrderArr)
print("\033[35m PostOrder:\033[0m", end=" ")
print(postOrderArr)


#----------------ÁRBOL ORDENADO-----------------------------------
print("árbol odenado")

nodoRaiz = nodo(num)
for i in range (0,len(arrayNum),1):
    nodosOrdenados(nodoRaiz,nodo(arrayNum[i-1]))
    pass
     
printArbol(nodoRaiz)
LVR(nodoRaiz, inOrderArr)
print(inOrderArr)
