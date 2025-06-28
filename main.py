# main.py

import contador

def solicitar_numero():
   
    while True:
        try:
            numero = int(input("Ingresa un número: "))
            if numero >= 0:
                return numero
            else:
                print("El número debe ser positivo.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")

def main():
    numero = solicitar_numero()
    print("\nIniciando cuenta regresiva...\n")
    contador.cuenta_regresiva(numero)

if _name_ == "_main_":
    main()