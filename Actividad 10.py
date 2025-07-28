def menu():
    print("\n===== MENÚ DE RETOS RECURSIVOS =====\n1. Invertir una cadena de texto\n2. Calcular la suma de los primeros N números naturales\n3. Imprimir una cuenta regresiva desde N a 1\n4. Sumar los digitos de un numero\n5. Contar cuántos digitos tiene un número\n6. Salir")

def invertir():
    cadena = input("\nIngrese una cadena de texto: ")
    invertirCadena(cadena)
    print(f"La cadena invertida es: {invertirCadena(cadena)}")

def invertirCadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertirCadena(cadena[:-1])

def sumarNumeros():
    while True:
        try:
            n = int(input("\nIngrese hastaa que número se va a sumar: "))
            sumaNumeros(n)
            print(f"La suma de numeros es: {sumaNumeros(n)}")
            break
        except:
            print("El numero ingresado no es valido")

def sumaNumeros(n):
    if n <= 0:
        return 0
    else:
        return n + sumaNumeros(n-1)

def cuentaRegresiva():
    while True:
        try:
            c = int(input("\nIngrese desde donde inicirá la cuenta regresiva: "))
            cuentaReg(c)
            break
        except:
            print("El numero ingresado no es valido")

def cuentaReg(c):
    if c <= 0:
        return 0
    print(c)
    cuentaReg(c - 1)

def sumaDigitos():
    while True:
        try:
            numero = int(input("\nIngrese un numero, y se sumarán sus digitos:"))
            sumarDigitos(numero)
            print(f"La suma de los digitos del numero ({numero}) es: {sumarDigitos(numero)}")
            break
        except:
            print("El numero ingresado no es valido")

def sumarDigitos(numero):
    if numero == 0:
        return 0
    else:
        return numero % 10 + sumarDigitos(numero // 10)

def contarDigitos():
    while True:
        try:
            num = int(input("Ingrese "))
        except:
            print("El numero ingresado no es valido")
def main():
    while True:
        menu()
        try:
            opcion = int(input("\nSeleccione una opcion: "))
            match opcion:
                case 1:
                    invertir()
                case 2:
                    sumarNumeros()
                case 3:
                    cuentaRegresiva()
                case 4:
                    sumaDigitos()
                case 5:
                    print("askf5")
                case 6:
                    print("SALIENDO...")
                    break
                case _:
                    print("ERROR, esa opción no existe")
        except Exception as ex:
            print(f"Ha ocurrido un error, {ex}")
main()