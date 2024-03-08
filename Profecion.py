class Profecion:
    cantidadProfecionales = 0
    def __init__(self, nombre) -> None:
        self._nombre = nombre
        self._sueldo = 0
        self._Preguntas()
        Profecion.add()
    
    def _Preguntas(self):
        self._sueldo = int(input("Ingrese su sueldo: "))
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def sueldo(self):
        return self._sueldo
    
    def add():
        Profecion.cantidadProfecionales+=1