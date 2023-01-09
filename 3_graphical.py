import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,15,45)
y = x ** 4
z = x ** 6
plt.plot(x,z,color='BLUE')
plt.plot(x, y,"*")
plt.xlabel('x-values')
plt.ylabel("y-values")
plt.title('line plot')
plt.grid(True)
plt.show()
