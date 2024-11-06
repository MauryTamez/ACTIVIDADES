import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir las variables difusas: calidad de la comida, nivel de servicio y propina
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir las funciones de pertenencia para la calidad
calidad['pobre'] = fuzz.trimf(calidad.universe, [0, 0, 5])
calidad['aceptable'] = fuzz.trimf(calidad.universe, [0, 5, 10])
calidad['excelente'] = fuzz.trimf(calidad.universe, [5, 10, 10])

# Definir las funciones de pertenencia para el servicio
servicio['malo'] = fuzz.trimf(servicio.universe, [0, 0, 5])
servicio['bueno'] = fuzz.trimf(servicio.universe, [0, 5, 10])
servicio['excelente'] = fuzz.trimf(servicio.universe, [5, 10, 10])

# Definir las funciones de pertenencia para la propina
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Definir las reglas del sistema difuso
rule1 = ctrl.Rule(servicio['excelente'] & calidad['excelente'], propina['alta'])
rule2 = ctrl.Rule(servicio['bueno'] & calidad['aceptable'], propina['media'])
rule3 = ctrl.Rule(servicio['malo'] | calidad['pobre'], propina['baja'])

# Crear el sistema de control difuso y simularlo
sistema_propina_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
sistema_propina = ctrl.ControlSystemSimulation(sistema_propina_ctrl)

# Definir los valores de entrada
sistema_propina.input['calidad'] = 6.5  # Por ejemplo, calidad 6.5 sobre 10
sistema_propina.input['servicio'] = 9.0  # Servicio 9 sobre 10

# Calcular el resultado
sistema_propina.compute()

# Mostrar el resultado de la propina sugerida
print(f"Propina sugerida: {sistema_propina.output['propina']:.2f}")
