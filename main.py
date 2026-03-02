from octagon import Octago

a = input("Вdедите длину стороны: ")
act = Octago(int(a))
print(f"Площадь и периметр равны: {act.perimetor_area()}")
print(f"Радиус и площадь описанной окружности: {act.opis_octa()}")
print(f"Радиус и площадь вписанной окружности: {act.vpis_octa()}")
act.draw()