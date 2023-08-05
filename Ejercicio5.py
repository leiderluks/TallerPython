'''#5. Realizar un programa que muestre un menú con opciones de colores primario 
(Amarillo, azul, rojo, blanco y negro), el usuario debe escoger 2 colores de los 
ofrecidos en el menú y con una secuencia de if y elif evaluar las posibles 
combinaciones generadas con los colores primarios. Si el usuario escogió 
colores que no generan otro al ser combinados debe mostrar un mensaje de 
“opciones no validas'''

print("Menú de colores primarios:")
print("1. Amarillo")
print("2. Azul")
print("3. Rojo")
print("4. Blanco")
print("5. Negro")

color1 = int(
    input("ingrese el primer color: "))
color2 = int(
    input("ingrese el segundo color: "))

if color1 == 1 and color2 == 2 or color1 == 2 and color2 == 1:
     print("Mezclando amarillo y azul obtienes verde.")
elif color1 == 1 and color2 == 3 or color1 == 3 and color2 == 1:
    print("Mezclando amarillo y rojo obtienes naranja.")
elif color1 == 1 and color2 == 4 or color1 == 4 and color2 == 1:
    print("Mezclando amarillo y blanco obtienes amarillo.")
elif color1 == 1 and color2 == 5 or color1 == 5 and color2 == 1:
    print("Mezclando amarillo y negro obtienes amarillo.")
elif color1 == 2 and color2 == 3 or color1 == 3 and color2 == 2:
    print("Mezclando azul y rojo obtienes morado.")
elif color1 == 2 and color2 == 4 or color1 == 4 and color2 == 2:
    print("Mezclando azul y blanco obtienes azul.")
elif color1 == 2 and color2 == 5 or color1 == 5 and color2 == 2:
    print("Mezclando azul y negro obtienes azul.")
elif color1 == 3 and color2 == 4 or color1 == 4 and color2 == 3:
    print("Mezclando rojo y blanco obtienes rojo.")
elif color1 == 3 and color2 == 5 or color1 == 5 and color2 == 3:
    print("Mezclando rojo y negro obtienes rojo.")
elif color1 == 4 and color2 == 5 or color1 == 5 and color2 == 4:
    print("Mezclando blanco y negro obtienes gris.")
else:
    print("Opciones no válidas.")