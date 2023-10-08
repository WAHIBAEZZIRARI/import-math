import math
a = float(input("Veuillez saisir la valeur de a: "))
b = float(input("Veuillez saisir la valeur de b: "))
c = float(input("Veuillez saisir la valeur de c: "))
delta = b ** 2 - 4 * a * c
if delta < 0:
   print("Pas de solutions réelles")
elif delta == 0:
    x = (-b)/(2*a)
    print("La solution est",x)
else:
     x1 = (-b-math.sqrt(delta))/(2*a)
     x2 = (-b+math.sqrt(delta))/(2*a)
print("Les solutions sont: ", format(x1,".2f"), " et " ,format(x2,".2f"))