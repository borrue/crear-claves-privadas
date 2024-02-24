import random
import string
def generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    caracteres = ''
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena
def obtener_preferencias():
    longitud = int(input("Longitud de la contraseña: "))
    incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
    incluir_minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("¿Incluir símbolos especiales? (s/n): ").lower() == 's'
    return longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos
def main():
    print("¡Bienvenido a la aplicación de generación de contraseñas seguras!")
    longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos = obtener_preferencias()
    contrasena_generada = generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
    print("Tu contraseña generada es:", contrasena_generada)

if __name__ == "__main__":
    main()

