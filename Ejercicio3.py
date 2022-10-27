def Alumno():
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return "El alumno {} ha sacado un {}"

Daniel_Lopez = Alumno("Daniel Lopez", 10)
Juan_Perez = Alumno("Juan Perez", 7)

alumnos = [Daniel_Lopez, Juan_Perez ]

print(Juan_Perez )
print(Daniel_Lopez)

def nota(alumno):
    for i in alumno:
        if i.nota