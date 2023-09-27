class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
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
            self.tabla[indice] = Nodo(clave, valor)
        else:
            # Si hay colisión, agregamos el elemento a la lista enlazada
            actual = self.tabla[indice]
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(clave, valor)

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        actual = self.tabla[indice]
        while actual:
            if actual.clave == clave:
                return actual.valor
            actual = actual.siguiente
        return None

TablaHash("4Sa8gD",10)