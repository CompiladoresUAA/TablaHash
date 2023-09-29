import random
#Constante 
SHIFT : 4
SIZE : 10
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
            #self.tabla[indice] = Nodo(clave, valor)
            #print("Primer valor en el indice -> "+str(indice))
            self.tabla[indice] = Nodo(clave)

        else:
            #Solución de la colisión Encadenamiento 
            nodoAct = self.tabla[indice]
            #print("Valores en i= "+str(indice))
            #if(nodoAct.sig == None):
                #print("Segundo Nodo")
            while nodoAct.sig != None:
                #print("clave en while -> "+nodoAct.cve+"  |  Nodo --> "+str(nodoAct.sig))
                nodoAct = nodoAct.sig
            
            #nodoAct.sig = Nodo(clave, valor)
            nodoAct.sig = Nodo(clave)

    def buscar(self, clave):
        indice = self.functionHash(clave)
        #print("Indice --> "+str(indice))
        node = self.tabla[indice]
        if(node == None):
            print("No se encontro la clave "+clave)
        else:
            while node.sig == None:
                if(clave == node.cve):
                    print("Se encontro la clave "+clave)
                    return
                node = node.sig
            print("No se encontro la clave "+clave)


    def hash(self,key)->int:
        temp = 0
        i = 0
        while key[i] != None:
            #temp = ((temp * pow(2,SHIFT)))  
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
obj = TabHash(100)
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