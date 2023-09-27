from enum import Enum
class Options(Enum):
    ADD     = 1
    GENCVE  = 2
    SHOW    = 3
    SEARCH  = 4
    EXIT    = 5

def menu()->None:
    print(f"<<<\tMenu\t>>>",end='\n')
    print("1. Agregar una clave a la tabla hash.")
    print("2. Generar una clave aleatoria y agregarla a la tabla hash.")
    print("3. Mostrar el contenido de la tabla hash.")
    print("4. Buscar una clave en la tabla hash.")
    print("5. Salir.")
    print(f"Elige una opción: ",end='')
    opcion = input()
   
    try:
        opcion = int(opcion)
        options(opcion)
    except ValueError:
        print("No ingresaste un digito correctamente. error: ")
        menu()
def options(op:int)->None:
    if( Options.ADD.value == op ):
        pass
    elif ( Options.GENCVE.value == op ):
        pass
    elif ( Options.SHOW.value == op ):
        pass
    elif ( Options.SEARCH.value == op ):
        pass
    elif ( Options.EXIT.value == op ):
        print("Saliendo ...")
if __name__ == '__main__':
    menu()

