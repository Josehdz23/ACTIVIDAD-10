def menu():
    print("\n===== MENÚ DE RETOS RECURSIVOS =====\n1. Invertir una cadena de texto\n2. Calcular la suma de los primeros N números naturales\n3. Imprimir una cuenta regresiva desde N a 1\n4. Sumar los dígitos de un número\n5. Contar cuántos dígitos tiene un número\n6. Salir")

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
            n = int(input("\nIngrese hasta que número se va a sumar: "))
            if n > 0:
                sumaNumeros(n)
                print(f"La suma de los números es: {sumaNumeros(n)}")
                break
            else:
                print("El número ingresado no es válido, reintente")
        except:
            print("El número ingresado no es válido")

def sumaNumeros(n):
    if n <= 0:
        return 0
    else:
        return n + sumaNumeros(n-1)

def cuentaRegresiva():
    while True:
        try:
            c = int(input("\nIngrese desde donde se inicirá la cuenta regresiva: "))
            if c > 0:
                cuentaReg(c)
                break
            else:
                print("El número ingresado no es válido, reintente")
        except:
            print("El número ingresado no es válido, reintente")

def cuentaReg(c):
    if c <= 0:
        return 0
    print(c)
    cuentaReg(c - 1)

def sumaDigitos():
    while True:
        try:
            numero = int(input("\nIngrese un número, y se sumarán sus dígitos:"))
            if numero > 0:
                sumarDigitos(numero)
                print(f"La suma de los dígitos del número ({numero}) es: {sumarDigitos(numero)}")
                break
            else:
                print("El número ingresado no es válido, reintente")
        except:
            print("El número ingresado no es válido, reintente")

def sumarDigitos(numero):
    if numero == 0:
        return 0
    else:
        return numero % 10 + sumarDigitos(numero // 10)

def contarDigitos():
    while True:
        try:
            num = int(input("\nIngrese un número para contar sus dígitos: "))
            if num > 0:
                contarDig(num)
                print(f"El número ({num}) tiene {contarDig(num)} dígitos!")
                break
            else:
                print("El número ingresado no es válido, reintente")
        except:
            print("El número ingresado no es válido, reintente")

def contarDig(num):
    if num < 10:
        return 1
    else:
        return 1 + contarDig(num // 10)

def main():
    while True:
        menu()
        try:
            opcion = int(input("\nSeleccione una opción: "))
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
                    contarDigitos()
                case 6:
                    print("SALIENDO...")
                    break
                case _:
                    print("ERROR, esa opción no existe")
        except Exception as ex:
            print(f"Ha ocurrido un error, {ex}")
main()