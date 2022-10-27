class alumno():
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return "Se ha creado el alumno {} con nota {}".format(self.nombre, self.nota)

Daniel_Lopez = alumno("Daniel Lopez", 10)
Juan_Perez = alumno("Juan Perez", 7)
Angulo = alumno("Angulo",3)

alumnos = [Daniel_Lopez, Juan_Perez, Angulo ]

print(Juan_Perez )
print(Daniel_Lopez)
print(Angulo)

    

def nota(a):
    for i in alumnos:
        if i.nota >=5:
            print(i.nombre,"ha aprobado.")
        else:
            print(i.nombre,"ha suspendido.")
            
nota(alumnos)