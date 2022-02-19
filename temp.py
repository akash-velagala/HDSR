import numpy as np

m = np.arrange(6).reshape(3, 1, 2)

n = np.arrange(6).reshape(3, 2, 1)

print(m+n)