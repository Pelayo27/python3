import math
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
print(f" Valores para el punto A({val1[0]},{val1[1]}) ")
b = input(f"{GREEN}Ingrese el Punto B(x2,y2): {RESET}")
val2 =b.split(',')
print(f" Valores para el punto  B({val2[0]},{val2[1]}) ")

operation=((int(val2[0])-int(val1[0]))**2 + (int(val2[1])-int(val1[1]))**2)
d= math.sqrt(operation)
print(f"{RED} Dista de  A hacia la B {round(d,2)}{RESET} ")