import math 
x1 = int(input("Ingrese x1: "))
print(f" Punto inicial ({x1},y1)")
y1= int(input("Ingrese y1: "))

print(f" Punto A ({x1},{y1})")
    # Punto B
x2 = int(input("Ingrese x2: "))
print(f" Punto inicial ({x2},y1)")
y2= int(input("Ingrese y2: "))
print(f" Punto B ({x1},{y1})")
print(f"Puntos cardinales A ({x1},{y1}) B ({x2},{y2})")
operation= ((x2-x1)**2 + (y2-y1)**2)
d= math.sqrt(operation)
print(f" Dista de  A hacia la B {round(d,2)}")