import numpy as np
import pandas as pd
x = np.arange(0, 5, 0.1)
y = np.sin(x)

print(y)

a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)

b = a.reshape(2,3)
print(b.shape)

df = pd.DataFrame(b);
print(df)