#adolecente 13 a 17
edad = int(input("ingrese edad"))
while edad < 0 or edad > 120:
    edad = int(input("reingrese edad"))

if edad <= 13 and edad >= 17:
    print("es adolecente") 

#negacion
if not(edad <= 13 and edad >= 17):
    print("no es adolecente") 

#negacion de manera individual
if not(edad <= 13) or not (edad >= 17):
    print("no es adolecente") 
    #leyes de De morgan