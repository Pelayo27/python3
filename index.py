import math
from time import sleep
import matplotlib.pyplot as plt
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
a = input(f"{GREEN}Ingrese el Punto A(x1,y1): {RESET}")
val1 =a.split(',')
x1=float(val1[0])
y1=float(val1[1])
sleep(1)
print(f" Valores para el punto A({x1},{y1}) ")
b = input(f"{GREEN}Ingrese el Punto B(x2,y2): {RESET}")
val2 =b.split(',')
x2=float(val2[0])
y2=float(val2[1])
print(f" Valores para el punto  B({x2},{y2}) ")
sleep(2)
operation=((x2-x1)**2 + (y2-y1)**2)
d= math.sqrt(operation)
print(f"{RED} Distancia entre A({x1},{y1}) y B({x2},{y2}) es : {round(d,2)}{RESET} ")
sleep(4)
fig, ax = plt.subplots()
ax.plot([x1, x2], [y1, y2])
plt.show()