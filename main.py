from TP import Animal, Paciente,Veterinaria

tipo =input('ingrese su tipo de mascota:')
nombre =input('ingrese su nombre:')
edad =input('ingrese su edad:')
raza =input('ingrese su raza:')

Paciente = Paciente(tipo,nombre,edad,raza)

tipo =input('ingrese su tipo de mascota:')
nombre =input('ingrese su nombre:')

Animal = Animal(tipo,nombre)

Veterinaria = Veterinaria()

Veterinaria.setVeterinaria(Veterinaria)
Veterinaria.setPaciente(Paciente)
print(Veterinaria)