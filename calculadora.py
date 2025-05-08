from operaciones import suma, resta, multiplicacion, division, potencia, division_entera

try:
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    operador = input("Ingrese el operador (+, -, *, /, **, //): ")

    if operador == "+":
        resultado = suma(a, b)
    elif operador == "-":
        resultado = resta(a, b)
    elif operador == "*":
        resultado = multiplicacion(a, b)
    elif operador == "/":
        resultado = division(a, b)
    elif operador == "**":
        resultado = potencia(a, b)
    elif operador == "//":
        resultado = division_entera(a, b)
    else:
        raise ValueError("Operador no válido")

    print(f"Resultado: {resultado}")

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
