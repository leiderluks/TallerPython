'''Comparar 4 números solicitados al usuario, escribir condiciones que permita
mostrar que un número fue escrito 2 veces, que todos son iguales o por el contrario
todos son diferentes'''

numero1 =int (input ("escribe un número entero "))
numero2 =int (input ("escribe un número entero "))
numero3 =int (input ("escribe un número entero "))
numero4 =int (input ("escribe un número entero "))

if numero1 == numero2  and numero2== numero3 and numero3 == numero4:
    print(f"todos los numeros son igules")
elif numero1==numero2 and numero3==numero4:
    print(f"el primer y segundo numero estan repetidos y son {numero1} y el tercer y cuarto tambien estan repetidos y el numero es {numero3} ")
elif numero1==numero2 :
    print(f"el primer y segundo numero estan repetidos y son {numero1}  ")
elif numero3==numero4:
     print(f"el tercer y cuarto numero estan repetidos y son {numero3}  ")
elif numero1==numero4:
 print(f"el primer y cuarto numero estan repetidos y son {numero1} ")
elif numero1==numero3:
 print(f"el primer y el tercero numero estan repetidos y son {numero1} ")

elif numero2==numero3:
     print(f"el segundo y tercero numero estan repetidos y son {numero2} ")
elif numero2==numero4:
     print(f"el segundo y el cuarto numero estan repetidos y son {numero2} ")
else:
    print("todos los nuemeros son diferentes y son {numero1}, {numero2}, {numero3}, {numero4} ")