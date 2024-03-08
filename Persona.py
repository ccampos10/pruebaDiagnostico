from Profecion import Profecion

class Persona:
    def __init__(self) -> None:
        self._nombre = '-'
        self._edad = -1
        self._sexo = '-'
        self._prof = '-'
        self._Preguntar()
    
    def _Preguntar(self):
        self._nombre = input("Ingrese su nombre: ")
        self._edad = int(input("Ingrese su edad: "))
        self._sexo = input("Ingrese su sexo (Masculino/Femenino): ")
        prof = input("Ingrese su profecion (Ingeniero/Abogado/Otro): ")
        self._prof = Profecion(prof)
    
    @property
    def profecion(self):
        return self._prof.nombre
    
    @property
    def sueldo(self):
        return self._prof.sueldo