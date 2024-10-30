# Importing necessary libraries
import random
import math
import matplotlib.pyplot as plt

from samila import GenerativeImage, Projection

def f1(x, y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result
def f2(x, y):
    result = random.uniform(-1,0) * y**3 - math.cos(x**2) + 2*x
    return result
DEFAULT_SEED = 122892
g = GenerativeImage(f1, f2)
g.generate(seed=DEFAULT_SEED)
g.plot(projection=Projection.POLAR, size=(9,8))
g.save_image(file_adr="myart1.png", depth=5)