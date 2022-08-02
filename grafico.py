import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

x = np.array([10, 100, 1000])

y = np.array([42.5313201, 445.2973613, 4471.0025635])

#X_Y_Spline = make_interp_spline(x, y)

#X_ = np.linspace(x.min(), x.max(), 10000)
#Y_ = X_Y_Spline(X_)

#plt.plot(X_, Y_) 

plt.plot(x, y) 

plt.xlabel('N elementos') 
plt.ylabel('Tiempo') 
plt.title('Complejidad Cosine Similarity') 
plt.show() 