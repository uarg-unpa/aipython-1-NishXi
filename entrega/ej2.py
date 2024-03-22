yo = int(input("ingrese su edad: "))
vos = int(input("ingrese su edad: "))
if(yo==vos):
    print("¡Tienen la misma edad!")
else:
    if(yo>vos):
        print("Yo tengo ", yo-vos, "que vos")
    else:
        print("vos tenes ", vos-yo, "que yo")    