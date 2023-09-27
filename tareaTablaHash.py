import random

#Diccionario de letras a un par de numeros
letrasDic ={
    'a' : '01',
    'b' : '02',
    'c' : '03',
    'd' : '04',
    'e' : '05',
    'f' : '06',
    'g' : '07',
    'h' : '08',
    'i' : '09',
    'j' : '10',
    'k' : '11',
    'l' : '12',
    'm' : '13',
    'n' : '14',
    'ñ' : '15',
    'o' : '16',
    'p' : '17',
    'q' : '18',
    'r' : '19',
    's' : '20',
    't' : '21',
    'u' : '22',
    'v' : '23',
    'w' : '24',
    'x' : '25',
    'y' : '26',
    'z' : '27',
    'A' : '28',
    'B' : '29',
    'C' : '30',
    'D' : '31',
    'E' : '32',
    'F' : '33',
    'G' : '34',
    'H' : '35',
    'I' : '36',
    'J' : '37',
    'K' : '38',
    'L' : '39',
    'M' : '40',
    'N' : '41',
    'Ñ' : '42',
    'O' : '43',
    'P' : '44',
    'Q' : '45',
    'R' : '46',
    'S' : '47',
    'T' : '48',
    'U' : '49',
    'V' : '50',
    'W' : '51',
    'X' : '52',
    'Y' : '53',
    'Z' : '54'
}

class Nodo:
    def __init__(self, clave) -> None:
        self.cve = clave
        #self.val = valor
        self.sig = None

class TabHash:
    def __init__(self, tamanio) -> None:
        self.tam = tamanio
        self.tabla = [None] * tamanio
    
    def functionHash(self, clave):
        tempo = ""
        for c in clave:
            tran = ord(c)
            if((tran>=65 and tran<=90) or 
               (tran >= 97 and tran <= 122) or 
               tran == 164 or tran == 165):
                tempo+=letrasDic[c]
            else:
                tempo+=c
        
        lon = len(tempo)
        
        if(lon == 1):
            i= int(tempo) + 1
        else:
            tem = tempo[0]+tempo[lon-1]
            i = int(tem) + 1
        
        return i

    def insert(self, clave):
        indice = self.functionHash(clave)
        if self.tabla[indice] == None:
            #self.tabla[indice] = Nodo(clave, valor)
            self.tabla[indice] = Nodo(clave)

        else:
            #Solución de la colisión Encadenamiento 
            nodoAct = self.tabla[indice]
            while nodoAct.sig != None:
                nodoAct = nodoAct.sig
            
            #nodoAct.sig = Nodo(clave, valor)
            nodoAct.sig = Nodo(clave)

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
print("Cadena ---> "+cad)
cad="A"
for n in cad:
    print(ord(n))
    if(ord(n)==65):
        print("Si es la letra a porque dio 65")

obj = TabHash(5)
print("Indice --> "+str(obj.functionHash("8iEe")))
#lon = len(cad)
#c=cad[lon-1]
#print()
#n = letrasDic[c]
#print(n)