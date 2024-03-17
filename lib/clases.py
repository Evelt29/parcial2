
class nodo():
    def __init__(self,valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        pass

    
    def getArbol(self):
        strOut = " "
        strOut += f"Nodo Padre [{self.valor}]"
        if type(self.izquierda) != type(None):
            strOut += f"  Iz[{self.valor}]->[{self.izquierda}]" 
        if self.derecha is not None:
            strOut += f"  Der[{self.valor}]->[{self.derecha}]"
        return strOut
    
    def __str__(self):
        return f"valor:{self.valor}"
    
pass