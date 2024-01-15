import numpy as np
a = np.arange(4).reshape((2,2))
a1 = np.arange(4).reshape((1,4))
print(np.max(a,a1))