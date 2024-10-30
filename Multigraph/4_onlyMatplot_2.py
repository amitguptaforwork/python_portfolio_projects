import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#A simple example
# Matplotlib graphs your data on Figures (e.g., windows, Jupyter widgets, etc.), each of which can contain one or more 
# Axes, an area where points can be specified in terms of x-y coordinates (or theta-r in a polar plot, x-y-z in a 3D plot, etc.).
# The simplest way of creating a Figure with an Axes is using pyplot.subplots. We can then use Axes.plot to draw some data on the Axes:

#https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# matplotlib.pyplot is a collection of functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: 
#e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.

#In matplotlib.pyplot various states are preserved across function calls, so that it keeps track of things like the 
#current figure and plotting area, and the plotting functions are directed to the current axes 

# Generating visualizations with pyplot is very quick:

# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()

# You may be wondering why the x-axis ranges from 0-3 and the y-axis from 1-4. If you provide a single list or array to plot,
#  matplotlib assumes it is a sequence of y values, and automatically generates the x values for you. Since python ranges start with 0, 
#  the default x vector has the same length as y but starts with 0; therefore, the x data are [0, 1, 2, 3].

# plot is a versatile function, and will take an arbitrary number of arguments. For example, to plot x versus y, you can write:
#plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

# Formatting the style of your plot
# For every x, y pair of arguments, there is an optional third argument which is the format string that indicates the color and line type of the plot. The letters and symbols of the format string are from MATLAB, and you concatenate a color string with a line style string. The default format string is 'b-', which is a solid blue line. For example, to plot the above with red circles, you would issue

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'g^--')

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.


plt.show()