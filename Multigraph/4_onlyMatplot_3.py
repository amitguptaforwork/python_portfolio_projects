import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()
#combine above two lines in one single line using following
#fig, ax = plt.subplots()  # Create a figure containing a single axes.

ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

plt.show()


