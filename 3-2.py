""" 
2-Escribe un programa en la consola de python que pida al usuario su peso (en kg) y
 estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable,
  e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa
   corporal calculado redondeado con dos decimales. """

peso = input("Ingresa tu peso en KG: ")
estatura = input("Ingresa tu estatura en MT: ")
masaCorporal = round(float(peso)/float(estatura)**2,2)

print (f"Tu indice de masa corporal es {masaCorporal} ")