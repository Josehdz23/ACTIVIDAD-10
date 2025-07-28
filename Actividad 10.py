def menu():
    print("\n===== MENÚ DE RETOS RECURSIVOS =====\n1. Invertir una cadena de texto\n2. Calcular la suma de los primeros N números naturales\n3. Imprimir una cuenta regresiva desde N a 1\n4. Sumar los digitos de un numero\n5. Contar cuántos digitos tiene un número\n6. Salir")

def invertir():
    cadena = input("\nIngrese una cadena de texto: ")
    invertirCadena(cadena)
    print(f"La cadena invertida es: {invertirCadena(cadena)}")

def sumaNumeros(n):
    if n <= 0:
        return 0
    else:
        return n + sumaNumeros(n-1)

def invertirCadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertirCadena(cadena[:-1])

def main():
    while True:
        menu()
        try:
            opcion = int(input("\nSeleccione una opcion: "))
            match opcion:
                case 1:
                    invertir()
                case 2:
                    print("askf")
                case 3:
                    print("askf3")
                case 4:
                    print("askf4")
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