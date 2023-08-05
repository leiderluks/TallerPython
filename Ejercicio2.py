
desarrollosoftware = float(input("Ingrese la nota de Desarrollo de Software: "))
matematicas = float(input("Ingrese la nota de Matemáticas: "))
logicaprogramacion = float(input("Ingrese la nota de Lógica de Programación: "))

promedio = (desarrollosoftware + matematicas + logicaprogramacion) / 3

if promedio >= 3.0:
    print("Aprobado")
else:
    print("Reprobado")