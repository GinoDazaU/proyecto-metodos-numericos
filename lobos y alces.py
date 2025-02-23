import matplotlib.pyplot as plt

# Datos desde el año 2000 hasta 2019
anios = list(range(2000, 2020))
lobos = [29, 19, 17, 19, 29, 30, 30, 21, 23, 24, 19, 16, 9, 8, 9, 3, 2, 2, 2, 14]
alces = [850, 900, 1000, 900, 750, 540, 385, 450, 650, 530, 510, 515, 750, 975, 1050, 1250, 1300, 1600, 1500, 2060]

import matplotlib.ticker as ticker

# Crear la figura
plt.figure(figsize=(12, 6))

# Graficar poblaciones de lobos y alces
plt.plot(anios, lobos, marker='o', linestyle='-', label='Lobos', color='red')
plt.plot(anios, alces, marker='s', linestyle='-', label='Alces', color='blue')

# Configurar etiquetas de los ejes
plt.xlabel('Año')
plt.ylabel('Población')
plt.title('Evolución de Poblaciones de Lobos y Alces (2000-2019)')
plt.legend()
plt.grid(True)

# Asegurar que los años aparezcan como enteros en el eje X
plt.xticks(anios, rotation=45)  # Rotar ligeramente para mayor claridad
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# Mostrar la gráfica
plt.show()
