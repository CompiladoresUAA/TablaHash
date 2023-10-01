import random
#Constante 
SHIFT = 4
SIZE = 100

class Nodo:
    def __init__(self, clave) -> None:
        self.cve = clave
        self.sig = None

class TabHash:
    def __init__(self, tamanio) -> None:
        self.tam = tamanio
        self.tabla = [None] * tamanio
    
    def functionHash(self,key)->int:
        temp = 0
        i = 0
        lon = len(key) - 1 
        while i < lon :
            temp = ((temp * pow(2,SHIFT) + ord(key[i])) % SIZE)  
            i+=1

        return temp

    def getTable(self):
        return self.tabla
    
    def insert(self, clave):
        indice = self.functionHash(clave)
        
        if self.tabla[indice] == None:
            #Inserta el primer nodo en ese indice de la tabla
            self.tabla[indice] = Nodo(clave)

        else:
            #Solución de la colisión Encadenamiento 
            nodoAct = self.tabla[indice]
            
            while nodoAct.sig != None:
                nodoAct = nodoAct.sig
            
            nodoAct.sig = Nodo(clave)

    def buscar(self, clave):
        indice = self.functionHash(clave)
        node = self.tabla[indice]
        if(node == None):
            print("No se encontro la clave "+clave)
            return False
        else:
            while node != None:
                if(clave == node.cve):
                    print("Se encontro la clave "+clave)
                    return True
                node = node.sig
            print("No se encontro la clave "+clave)
            return False   

def aleat(a,b):
    return random.randint(a,b)

def num():
    return str(aleat(0,9))
    
def ch():
    if(aleat(0,1)==0):
        return chr(aleat(65,90))
    else:
        return chr(aleat(97,122))


def alfaNum():
    temp=""
    i=0
    while(i!=6):
        if(aleat(1,2)==1):
            temp+=ch()
        else:
            temp+=num()
        
        i+=1
        
    return temp

def checkString(key)->bool:
    for c in key:
        tran = ord(c)
        if((tran>=65 and tran<=90) or 
        (tran >= 97 and tran <= 122) or 
        (tran == 209 or tran == 241) or
        (tran >=48 and tran <= 57)):
            pass
        else:
            print("caracter Incorrecto --> "+c)
            return False
    
    return True