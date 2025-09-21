# Importamos los módulos necesarios
import random
import string

# Definimos los caracteres que se usarán para generar la contraseña
# string.ascii_letters incluye letras minúsculas y mayúsculas
# string.digits incluye números del 0 al 9
# string.punctuation incluye caracteres especiales (!@#$%, etc.)
caracteres = string.ascii_letters + string.digits + string.punctuation

# Preguntamos al usuario qué longitud quiere para la contraseña
longitud_contrasena = int(input("Introduce la longitud de la contraseña deseada: "))

# Generamos la contraseña
# random.choice() elige un carácter al azar de la lista
# El bucle 'for' repite esta acción la cantidad de veces que indicó el usuario
contrasena_generada = "".join(random.choice(caracteres) for i in range(longitud_contrasena))

# Imprimimos la contraseña en la pantalla
print("Tu nueva contraseña es: ", contrasena_generada)