
from .clases import *

import pandas as pd


def import_xlsx(filename):
    df = pd.read_excel(filename) 
    return df
data = import_xlsx("datos-Eval-2.xlsx")






def linkHijo(nodoPadre, nodoHijoIz=None, nodoHijoDer=None):
    if nodoHijoIz is not None:
        nodoPadre.izquierda = nodoHijoIz
    if nodoHijoDer is not None:
        nodoPadre.derecha = nodoHijoDer

def LVR(nodo, inOrderArr):
    if nodo is not None:
        nodoPadre = nodo
        nodoHijo = None
        LVR(nodoPadre.izquierda,inOrderArr)    
        inOrderArr.append(nodoPadre.valor)
        LVR(nodoPadre.derecha,inOrderArr) 
        
        
        return inOrderArr
    

def LRV(nodo, postOrderArr):
    if nodo is not None:
        nodoPadre = nodo
        nodoHijo = None
        LRV(nodoPadre.izquierda,postOrderArr)    
        LRV(nodoPadre.derecha,postOrderArr) 
        postOrderArr.append(nodoPadre.valor)
        
        return postOrderArr
    
def VLF(nodo, preOrderArr):
    if nodo is not None:
        nodoPadre = nodo
        nodoHijo = None
        preOrderArr.append(nodoPadre.valor)
        VLF(nodoPadre.izquierda,preOrderArr)    
        VLF(nodoPadre.derecha,preOrderArr) 
        
        
        return preOrderArr
 

 #_______________________NODOS ORDENADOS_______________________
    
def nodosOrdenados(nodoPadre, newNodo):
    if newNodo.valor < nodoPadre.valor: #izquierda
        if nodoPadre.izquierda is None:  
            nodoPadre.izquierda = newNodo
        else:
            nodosOrdenados(nodoPadre.izquierda, newNodo)
                    
    if newNodo.valor > nodoPadre.valor: #izquierda
        if nodoPadre.derecha is None:  
            nodoPadre.derecha = newNodo
        else:
            nodosOrdenados(nodoPadre.derecha, newNodo)
            
def printArbol(nodo):
    if nodo is not None:
        nodoPadre = nodo
        print(nodoPadre.getArbol())
        printArbol(nodoPadre.izquierda)
        printArbol(nodoPadre.derecha)
    return 0   



def agregaNodos(currentNodo, nuevoNum):
    cola=[]
    cola.append(currentNodo)
    
    
    while cola:
        currentNodo= cola.pop(0)
        
        if currentNodo.izquierda is None:
            currentNodo.izquierda = nodo( nuevoNum )
            return 0
            
        if currentNodo.derecha is None:
            currentNodo.derecha = nodo ( nuevoNum )
            return 0
            
        cola.append(currentNodo.izquierda)
        cola.append(currentNodo.derecha) 
    return 0  