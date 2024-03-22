password = input("ingrese su contraseña: ")
prueba = input("ingrese nuevamente su contraseña: ")
if(prueba.lower() == password.lower()):
    print("correcto")
else:
    print("incorrecto")