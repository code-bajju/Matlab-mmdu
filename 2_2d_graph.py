import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4])
y = x*2
# First plot with X and Y
plt.plot(x, y)
x1 = [2, 3, 5, 7]
y1 = [1, 5, 8, 4]
# Second plot with x1 and y1 data
plt.plot(x1, y1, '-.')
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('multiple plots')
plt.show()