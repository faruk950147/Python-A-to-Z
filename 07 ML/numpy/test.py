import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)  # 0 to 2π with 100 points
y = np.sin(x)

plt.plot(x, y)
plt.show()