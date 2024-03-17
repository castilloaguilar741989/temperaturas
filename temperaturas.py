# Definir la matriz 3D con datos de temperaturas para seis ciudades
temperaturas = [
    [  # Quito
        [[28, 30, 29, 27, 26], [29, 31, 28, 27, 26], [30, 28, 27, 26, 25]],  # Semanas 1, 2, 3
    ],
    [  # Ibarra
        [[25, 26, 27, 26, 24], [26, 28, 25, 24, 23], [27, 25, 24, 23, 22]],  # Semanas 1, 2, 3
    ],
    [  # Loja
        [[32, 34, 33, 31, 30], [33, 35, 31, 30, 29], [34, 32, 30, 29, 28]],  # Semanas 1, 2, 3
    ],
    [  # Riobamba
        [[29, 31, 30, 28, 27], [30, 32, 28, 27, 26], [31, 29, 27, 26, 25]],  # Semanas 1, 2, 3
    ],
    [  # Tena
        [[27, 29, 28, 26, 25], [28, 30, 26, 25, 24], [29, 27, 25, 24, 23]],  # Semanas 1, 2, 3
    ],
    [  # Coca
        [[30, 32, 31, 29, 28], [31, 33, 29, 28, 27], [32, 30, 28, 27, 26]],  # Semanas 1, 2, 3
    ],
]

# Calcular el promedio de temperaturas por ciudad y semana
for ciudad_index, ciudad_temperaturas in enumerate(temperaturas):
    print(f"Promedio de temperaturas para {['Quito', 'Ibarra', 'Loja', 'Riobamba', 'Tena', 'Coca'][ciudad_index]}:")
    for semana_index, semana_temperaturas in enumerate(ciudad_temperaturas[0]):
        promedio_semana = sum(semana_temperaturas) / len(semana_temperaturas)
        print(f"Semana {semana_index + 1}: {promedio_semana:.2f} °C")
    print()
