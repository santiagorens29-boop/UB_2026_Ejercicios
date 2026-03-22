print("Archivo de correccion de los ejercicios")

#Ejercicio 1
def calcular_area(base, altura):
    resultado = base * altura
    return resultado

#Ejercicio 2
def conectar_base_de_datos():
    # Esta función es un placeholder para el ejercicio
    pass
try:
    conectar_base_de_datos()
except ConnectionError as e:
    print(f"Error de conexión: {e}")
    # Aquí podrías registrar el error en un archivo de log