# Programacion tradicional

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def main():
    temperaturas_diarias = []

    for dia in range(7):
        temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperaturas_diarias.append(temp)

    promedio_diario = calcular_promedio(temperaturas_diarias)
    print(f"\nEl promedio de temperatura diario es: {promedio_diario:.2f}°C")

    temperaturas_semanales = []

    for semana in range(4):
        temp_semanal = []
        print(f"\nSemana {semana + 1}:")
        for dia in range(7):
            temp = float(input(f"Ingrese la temperatura del día {dia + 1} de la semana {semana + 1}: "))
            temp_semanal.append(temp)
        temperaturas_semanales.append(temp_semanal)

    for semana, temps in enumerate(temperaturas_semanales):
        promedio_semanal = calcular_promedio(temps)
        print(f"\nEl promedio de temperatura de la semana {semana + 1} es: {promedio_semanal:.2f}°C")

if __name__ == "__main__":
    main()