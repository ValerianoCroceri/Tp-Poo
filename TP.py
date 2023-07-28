class Veterinaria():
    def __init__(self,listado: str, usuario: str, password : int) -> None:
        self.listado = listado
        self.usuario = usuario
        self.password = password
        
    def __str__(self) -> str:
        return f'Cuenta Activa: {self.usuario}'
    
    def validarUser(self):
        while True:
            usuario = int(input("ingrese su clave de seguridad:"))
            if usuario == self.password:
                print(f'Bienvenido nuevamente {self.usuario}')
                break
            else:
                print("clave invalida. Intente nuevamente.")
                


class Animal():
    def __init__(self, tipo: str, nombre : str,) -> None:
        self.__tipo = tipo
        self.__nombre = nombre
    def __str__(self) -> str:
        return f'{self.__tipo}{self.__nombre}'

class Paciente():
    def __init__(self,tipo: str, nombre : str, raza : str, edad: int) -> None:
        super().__init__(tipo,nombre,)
        self.__edad = edad
        self.__raza = raza
        return f'{self.__raza}{self.__edad}'
    
class Veterinaria():
    def __init__(self,) -> None:
        self.__listado = ''
        self.__paciente = []
        
    
    def __str__(self) -> str:
       return f'Listado: {self.__listado} , Paciente:{self.__paciente}, Cantidad de Animales:{len(self.__paciente)}'
    
    def setVeterinaria(self, listado: str):
        self.__listado = listado
    
    def setPaciente(self,Paciente: list):
       self.__paciente.append(Paciente)

Paciente1 = Paciente("")

Veterinaria = Veterinaria()

Veterinaria.setPaciente('')