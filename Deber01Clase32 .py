Usuarios = []
Cuentas = []

def Menu():
    while True:
        print("-" * 22, "Menu", "-" * 22)
        print("1. Registrar ususario")
        print("2. Deposito")
        print("3. Retiro")
        print("4. Salir")
        print("")
        Opción = input("Escoja una opción: ")
        print("-" * 50)
        print("")
        
        if Opción == "4":
            print("Saliendo del sistema..")
            break
        elif Opción == "1":
            Registrar()
        elif Opción == "2":
            Deposito()
        elif Opción == "3":
            Retiro()
        else:
            print("Opcion no valida")

def Registrar():
    print("Ingrese el nombre del usuario")
    nombre = input("> ").lower()
    if any(nombre in name.lower() for name in Usuarios):
        print(f"El usuario {nombre} ya fue registrado con anterioridad")
        print("")
    else:
        Usuarios.append(nombre)
        saldo = float(0)
        Cuenta = {"Nombre": nombre.capitalize(), "Saldo": saldo}
        Cuentas.append(Cuenta)
        print("Usuario registrado con exito")
        print("")

def Deposito():
    print("Ingrese el nombre del usuario")
    nombre = input("> ").lower()
    cuenta = []
    for c in Cuentas:
        if c["Nombre"].lower() == nombre:
            cuenta = c
            break

    if cuenta:
        print("")
        print("¿Cuál es la cantidad que desea depositar?")
        deposito = float(input("> "))
        if deposito < 0:
            print("Error, vuelva a intentarlo")
            print("")
        else:
            cuenta['Saldo'] += deposito
            print("")
            print(f"Su depósito fue de {deposito:.2f}$")
            print(f"Su saldo ahora es de {cuenta['Saldo']:.2f}$")
            print("")
    else:
        print("")
        print("Usuario no registrado en el sistema")
        print("")

def Retiro():
    print("Ingrese el nombre del usuario")
    nombre = input("> ").lower()
    cuenta = []
    for c in Cuentas:
        if c["Nombre"].lower() == nombre:
            cuenta = c
            break

    if cuenta:
        print("")
        print("¿Cuál es la cantidad que desea retirar?")
        retiro = float(input("> "))
        if retiro < 0:
            print("Error, vuelva a intentarlo")
            print("")
        else: 
            if retiro > cuenta['Saldo']:
                print("No posees la cantidad suficiente para retirar")
                print("")
            else:
                cuenta['Saldo'] -= retiro
                print("")
                print(f"Su retiro fue de {retiro:.2f}$")
                print(f"Su saldo ahora es de {cuenta['Saldo']:.2f}$")
                print("")
    else:
        print("")
        print("Usuario no registrado en el sistema")
        print("")
Menu()