import random
import numpy as np
import matplotlib.pyplot as plt

# Definir la función a minimizar
def funcion_objetivo(x):
    return (x - 3) ** 2 + 2

# Simulación del ajuste automático de parámetros
def ajuste_parametros(num_iteraciones, rango_busqueda):
    mejor_x = random.uniform(*rango_busqueda)  # Seleccionar un valor inicial aleatorio
    mejor_y = funcion_objetivo(mejor_x)        # Evaluar la función objetivo en ese punto

    for i in range(num_iteraciones):
        # Generar un nuevo valor aleatorio dentro del rango
        nuevo_x = random.uniform(*rango_busqueda)
        nuevo_y = funcion_objetivo(nuevo_x)
        
        # Si el nuevo valor es mejor (menor), actualizamos
        if nuevo_y < mejor_y:
            mejor_x = nuevo_x
            mejor_y = nuevo_y
        
        print(f"Iteración {i+1}: x = {nuevo_x}, f(x) = {nuevo_y}")
    
    return mejor_x, mejor_y

# Parámetros de la simulación
num_iteraciones = 100
rango_busqueda = (-10, 10)

# Ejecutar la simulación
mejor_x, mejor_y = ajuste_parametros(num_iteraciones, rango_busqueda)

print(f"\nMejor valor encontrado: x = {mejor_x}, f(x) = {mejor_y}")

# Graficar la función y el mejor valor encontrado
x_vals = np.linspace(-10, 10, 400)
y_vals = funcion_objetivo(x_vals)

plt.plot(x_vals, y_vals, label='Función Objetivo')
plt.scatter(mejor_x, mejor_y, color='red', label=f'Mejor valor: x={mejor_x:.2f}', zorder=5)
plt.title("Simulación de Ajuste Automático de Parámetros")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
