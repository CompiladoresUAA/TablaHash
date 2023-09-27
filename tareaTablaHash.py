import random

#Diccionario de letras a un par de numeros
letrasDic ={
    'a' : '01',
    'b' : '02',
    'c' : '03',
    'd' : '04',
    'f' : '05',
    'g' : '06',
    'h' : '07',
    'i' : '08',
    'j' : '09',
    'k' : '10',
    'l' : '11',
    'm' : '12',
    'n' : '13',
    'ñ' : '14',
    'o' : '15',
    'p' : '16',
    'q' : '17',
    'r' : '18',
    's' : '19',
    't' : '20',
    'u' : '21',
    'v' : '22',
    'w' : '23',
    'x' : '24',
    'y' : '25',
    'z' : '26',
    'A' : '27',
    'B' : '28',
    'C' : '29',
    'D' : '30',
    'E' : '31',
    'F' : '32',
    'G' : '33',
    'H' : '34',
    'I' : '35',
    'J' : '36',
    'K' : '37',
    'L' : '38',
    'M' : '39',
    'N' : '40',
    'Ñ' : '41',
    'O' : '42',
    'P' : '43',
    'Q' : '44',
    'R' : '45',
    'S' : '46',
    'T' : '47',
    'U' : '48',
    'V' : '49',
    'W' : '50',
    'X' : '51',
    'Y' : '52',
    'Z' : '53'
}

class Nodo:
    def __init__(self, clave, valor) -> None:
        self.cve = clave
        self.val = valor
        self.sig = None

class TabHash:
    def __init__(self, tamanio) -> None:
        self.tam = tamanio
        self.tabla = [None] * tamanio
    
    def functionHash(self, clave):
        
        return 0

    def insert(self, clave, valor):
        indice = self.functionHash(clave)
        if self.tabla[indice] == None:
            self.tabla[indice] = Nodo(clave, valor)
        
        else:
            #Solución de la colisión Encadenamiento 
            nodoAct = self.tabla[indice]
            while nodoAct.sig != None:
                nodoAct = nodoAct.sig
            
            nodoAct.sig = Nodo(clave, valor)

    def buscar(self, clave):

        pass


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
cad = alfaNum()
print(cad)
lon = len(cad)
print(letrasDic[cad[lon-1]])