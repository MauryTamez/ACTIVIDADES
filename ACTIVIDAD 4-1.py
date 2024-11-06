import random

# Parámetros
POPULATION_SIZE = 10     # Tamaño de la población
GENE_LENGTH = 5          # Longitud del gen (bits para representar un número de 0 a 31)
MAX_GENERATIONS = 20     # Número de generaciones
MUTATION_RATE = 0.01     # Tasa de mutación

# Función de aptitud: buscamos maximizar x^2
def fitness_function(x):
    return x ** 2

# Generar un individuo aleatorio
def generate_individual():
    return ''.join(random.choice('01') for _ in range(GENE_LENGTH))

# Convertir un gen binario a un número entero
def binary_to_int(binary):
    return int(binary, 2)

# Seleccionar a los padres mediante selección por torneo
def tournament_selection(population):
    # Escogemos dos individuos al azar
    tournament = random.sample(population, 2)
    # Devolvemos el individuo con mejor aptitud
    return max(tournament, key=lambda ind: fitness_function(binary_to_int(ind)))

# Operador de cruce de un punto
def crossover(parent1, parent2):
    point = random.randint(1, GENE_LENGTH - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Operador de mutación
def mutate(individual):
    mutated = ''.join(
        bit if random.random() > MUTATION_RATE else str(1 - int(bit))
        for bit in individual
    )
    return mutated

# Inicializar la población
population = [generate_individual() for _ in range(POPULATION_SIZE)]

# Algoritmo genético principal
for generation in range(MAX_GENERATIONS):
    # Evaluamos y mostramos la mejor solución actual
    best_individual = max(population, key=lambda ind: fitness_function(binary_to_int(ind)))
    best_value = binary_to_int(best_individual)
    print(f"Generación {generation+1}: Mejor valor x = {best_value}, Aptitud = {fitness_function(best_value)}")
    
    # Nueva generación
    new_population = []
    
    while len(new_population) < POPULATION_SIZE:
        # Selección de padres
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        
        # Cruzamiento
        child1, child2 = crossover(parent1, parent2)
        
        # Mutación
        child1 = mutate(child1)
        child2 = mutate(child2)
        
        # Agregar hijos a la nueva población
        new_population.extend([child1, child2])
    
    # Reemplazamos la población antigua por la nueva
    population = new_population

# Mejor solución final
best_individual = max(population, key=lambda ind: fitness_function(binary_to_int(ind)))
best_value = binary_to_int(best_individual)
print(f"\nMejor solución encontrada: x = {best_value}, Aptitud = {fitness_function(best_value)}")
