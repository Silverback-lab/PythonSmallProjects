from numba import jit
import random
import math
import time


@jit(nopython=True)
# --> This addis in numba compiler increase speed to run code
# --> Runing with out this took 7.48 sec and with it enabled took 0.59 sec
def some_function(n):
    z = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        z += math.sqrt(x ** 2 + y ** 2)
    return z

start = time.time()
some_function(10000000)
end = time.time()

print(end-start)

# -->  https://www.youtube.com/watch?v=bZ5G-RZoE6Q&t=338s