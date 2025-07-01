import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi,100)
y = np.cos(3*t)

plt.plot(t,y)
plt.show()