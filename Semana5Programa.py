import random

# Lista de números
lista_numeros = [2, 9, 13, 22, 45]

# Lista de diccionarios con datos de participantes
participantes = [
    {
        "nombre": "Elena",
        "edad": 32,
        "ciudad": "Macas"
    },
    {
        "nombre": "Santiago",
        "edad": 36,
        "ciudad": "Lago Agrio"
    },
    {
        "nombre": "Maria",
        "edad": 46,
        "ciudad": "Quito"
    },
    {
        "nombre": "Cristina",
        "edad": 32,
        "ciudad": "Guayaquil"
    },
    {
        "nombre": "Juan",
        "edad": 22,
        "ciudad": "Ambato"
    }
]

suma_numeros = sum(lista_numeros)
maximo_numero = max(lista_numeros)

participante_ganador = random.choice(participantes)
nombre_ganador = participante_ganador["nombre"]
edad_ganador = participante_ganador["edad"]
ciudad_ganador = participante_ganador["ciudad"]

print("Lista de números:", lista_numeros)
print("Suma de los números:", suma_numeros)
print("Número máximo:", maximo_numero)
print("\n--- Sorteo ---")
print("El participante ganador es:")
print("Nombre:", nombre_ganador)
print("Edad:", edad_ganador)
print("Ciudad:", ciudad_ganador)
