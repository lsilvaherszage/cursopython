from abc import ABC, abstractmethod
class Personal(ABC):

    @abstractmethod
    def __init__(self, nombre, apellido, fechaNac):
        self.nombre=nombre
        self.apellido=apellido
        self.fechaNac=fechaNac

    def __str__(self):
        return "{}, {} - Fecha Nacimiento: {} - {}".format(self.apellido, self.nombre, self.fechaNac, self.categoria())
    
    @abstractmethod
    def categoria(self):
        pass

    
class Administrativo(Personal):
    def __init__(self, nombre, apellido, fechaNac): #Puedo sacar el __init__ como el __str__, dado que es igual a lo que realiza la superclase?
        return super().__init__(nombre, apellido, fechaNac)

    def categoria(self):
        return "Administrativo"

class Directivo(Personal):
    def __init__(self, nombre, apellido, fechaNac):
        super().__init__(nombre, apellido, fechaNac)
        self.aCargo=[]

    def agregarPersonal(self, persona):
        self.aCargo.append(persona)

    def eliminarPersonal(self, persona):
        self.aCargo.remove(persona)

    def listarPersonal(self):
        print("Personal a cargo")
        print("Total: {}".format(len(self.aCargo)))
        for per in self.aCargo:
            print(per)

    def categoria(self):
        return "Directivo"

class Docente(Personal):
    def __init__(self, nombre, apellido, fechaNac, curso, directivo):
        super().__init__(nombre, apellido, fechaNac)
        self.curso=curso 
        self.directivo=directivo
        self.directivo.agregarPersonal(self)
        self.estudiantes=[]

    def agregarEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def eliminarEstudiante(self, estudiante):
        self.estudiantes.remove(estudiante)

    def listarEstudiantes(self):
        print("Estudiantes en su clase")
        for est in self.estudiantes:
            print(est)

    def categoria(self):
        return "Docente"

    def __str__(self):
        return super().__str__()+" - Bajo la dirección de {}".format(self.directivo.apellido)

# Probablemente sería mejor tener la clase Curso con un docente y una lista de estudiantes.

class Estudiante(Personal):
    def __init__(self, nombre, apellido, fechaNac, docente):
        super().__init__(nombre, apellido, fechaNac)
        self.docente=docente
        self.docente.agregarEstudiante(self)

    def categoria(self):
        return "Estudiante"

    def __str__(self):
        return super().__str__()+" - Su docente es {}".format(self.docente)
