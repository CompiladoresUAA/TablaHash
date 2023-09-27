class Nodo:
    def __init__(self, valor):
        #self.clave = clave
        self.valor = valor
        self.siguiente = None

class TablaHash:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [None] * tamano

    def funcion_hash(self, clave):
        return hash(clave) % self.tamano

    def insertar(self, clave, valor):
        indice = self.funcion_hash(clave)
        if self.tabla[indice] is None:
            #self.tabla[indice] = Nodo(clave, valor)
            self.tabla[indice] = Nodo(valor)
        else:
            # Si hay colisión, agregamos el elemento a la lista enlazada
            actual = self.tabla[indice]
            while actual.siguiente:
                actual = actual.siguiente
            #actual.siguiente = Nodo(clave, valor)
            actual.siguiente = Nodo(valor)

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        actual = self.tabla[indice]
        while actual:
            if actual.clave == clave:
                return actual.valor
            actual = actual.siguiente
        return None
tab = TablaHash(10)
tab.insertar("8A9r6m")
print(tab.buscar("8A9r6m"))