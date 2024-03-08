"""
1.- Abstraccion, herencia, Polimorfismo, Encapsulamiento
2.- Representa un objeto de la vida real, con atrubutos y metodos. Por ejemplo un Veiculo con color y tipo de combustible
3.- Es una instancia de una clase, en donde se le asignan valores a los atributos. Por ejemplo un Auto color amarillo a gasolina
"""

from Persona import Persona
lista = []

op = 'si'
while (op == 'si'):
    lista.append(Persona())
    op = input("Desea hacer otra encuesta? (Si/No): ").lower()
    print("")

cantIng = 0
sueldoIng = 0
cantAb = 0
sueldoAb = 0
cantOtr = 0
sueldoOtr = 0
for persona in lista:
    profName = persona.profecion
    profSueldo = persona.sueldo
    if profName == "Ingeniero":
        cantIng += 1
        sueldoIng += profSueldo
    elif profName == "Abogado":
        cantAb += 1
        sueldoAb += profSueldo
    else:
        cantOtr += 1
        sueldoOtr += profSueldo

print("Datos: ")
print(f"    Porcentaje de Ingenieros: {round(cantIng*100/len(lista),1)}%")
print(f"    Promedio sueldo de Ingenieros: {round(sueldoIng/cantIng,1)}\n")
print(f"    Porcentaje de Abogados: {round(cantAb*100/len(lista),1)}%")
print(f"    Promedio sueldo de Abogados: {round(sueldoAb/cantAb,1)}\n")
print(f"    Porcentaje de Otros: {round(cantOtr*100/len(lista),1)}%")
print(f"    Promedio sueldo de Otros: {round(sueldoOtr/cantOtr,1)}\n")
print("")