import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definir los parámetros de Lorenz
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Definir el sistema de Lorenz
def lorenz(X, t):
    x, y, z = X
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Condiciones iniciales
X0 = [1.0, 1.0, 1.0]

# Tiempo
t = np.linspace(0, 40, 10000)

# Resolver las ecuaciones diferenciales
sol = odeint(lorenz, X0, t)

# Graficar el atractor de Lorenz
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = sol[:, 0]
y = sol[:, 1]
z = sol[:, 2]

ax.plot(x, y, z, lw=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Atractor de Lorenz")
plt.show()
