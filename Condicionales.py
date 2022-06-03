#Declaramos un variable
calificacion = input("Introduce la calificacion de AZ-900: ")

calificacion = int(calificacion)

#Preguntamos si la calificacion es menor a 700
if calificacion < 700:
    print("Vessss, por no estudiar burrrooooooo") #Si es menor a 700, muestro esto
elif calificacion > 1000:
    print("Mientes!!, No puedes sacar mas de 1000")
else : # Si no se cumple el if anterior pasa a esta linea
    print("Felicidades, pasa por tu certificado") #Se ejecuta si ninungo de los if se cumple
    
#Verificador de mayor de edad    
edad = input("Introduce tu edad: ")
edad= int(edad)

if edad >= 18 and edad<= 100 :
    print("Bienvenido al mamitas")
elif edad  > 100 :
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar ")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else: 
    print("No puedes llevarte esos cigarros")

    #EN PYTHON NO HAY SWITCH CASE
