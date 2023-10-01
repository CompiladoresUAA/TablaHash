import random
#Constante 
SHIFT = 4
SIZE = 100
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
            i= int(tempo)
        else:
            tem = tempo[0]+tempo[lon-1]
            i = int(tem)
        
        return i
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
                #print("clave en while -> "+nodoAct.cve+"  |  Nodo --> "+str(nodoAct.sig))
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


    def hash(self,key)->int:
        temp = 0
        i = 0
        lon = len(key) - 1 
        while i < lon :
            temp = ((temp * pow(2,SHIFT) + ord(key[i])) % SIZE)  
            i+=1

        return temp   

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

#cad = alfaNum()
#print("Cadena ---> "+cad)
''' cad="A"
for n in cad:
    print(ord(n))
    if(ord(n)==65):
        print("Si es la letra a porque dio 65")

obj = TabHash(5)
print("Indice --> "+str(obj.functionHash("8iEe")))'''
'''obj = TabHash(100)
obj.insert("5a8Db")
obj.insert("4j0Wk")
obj.insert("gP51N")
print("----------------------------------------")
obj.buscar("hola4")
print("----------------------------------------")
obj.buscar("5a8Db")
print("----------------------------------------")
obj.buscar("0ie34")
print("----------------------------------------")
obj.buscar("gP51N")
print("----------------------------------------")
#lon = len(cad)
#c=cad[lon-1]
#print()
#n = letrasDic[c]
#print(n)'''
###################
'''
cad = "875m"
r = 0
for c in cad:
    temp = 0
    if ord(c)>=48 and ord(c)<=57:
        temp = ((temp * pow(2,8))+int(c)) % 10
    else:
        temp = ((temp * pow(2,8))+ord(c)) % 10
    print("caracter --> "+c)
    print("temp --> "+str(temp))
'''
'''obj = TabHash(100)
obj.insert("5a8Db")
obj.insert("4j0Wk")
obj.insert("gP51N")
obj.insert("5a8313Db")
obj.insert("4j0efERWk")
obj.insert("gP56547REWD1N")
obj.insert("5a8313PPb")
obj.insert("4j0ef5489k")
obj.insert("gP5RUEWD1N")
obj.insert("5aPb")
obj.insert("49k")
obj.insert("gPN")
print("##################################################\n")
print("----------------------------------------")
obj.buscar("hola4")
print("----------------------------------------")
obj.buscar("5a8Db")
print("----------------------------------------")
obj.buscar("0ie34")
print("----------------------------------------")
obj.buscar("gP51N")
print("#############################\n########################\n#################")
i = obj.functionHash("5a8Db")
n = obj.tabla[i]
if n == None:
    print("No hy nada en el indice --> "+str(i))
else:
    print("Hay algo en ese posicion de la tabla")
    while n != None:
        print(n.cve)
        n=n.sig
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
while j < obj.tam:
    node = obj.tabla[j]
    while node != None:
        print(node.cve)
        node = node.sig
    print("_______________")
    j+=1
print("indice --> "+str(obj.hash("hola Mundo")))
'''