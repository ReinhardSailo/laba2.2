import math

radius = float(input("Введите радиус окружности: "))
point_x = float(input("Введите координату x точки A: "))
point_y = float(input("Введите координату y точки A: "))

distance = math.sqrt(point_x**2 + point_y**2)

if distance <= radius:
    print("Точка A попадает в окружность.")
else:
    print("Точка A не попадает в окружность.")
