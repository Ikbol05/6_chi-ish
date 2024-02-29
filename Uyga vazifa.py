#
# # 1 masala
#
# class Car:
#     def __init__(self, model: str, color: str, speed: int, price: int):
#         self.__model = model
#         self.__color = color
#         self.__speed = speed
#         self.__price = price
#
#     def get_model(self):
#         return self.__model
#
#     def set_model(self, model2):
#         self.__model = model2
#
#     def del_model(self):
#         del self.__model
#
#     model = property(get_model, set_model, del_model)
#
#     def get_color(self):
#         return self.__color
#
#     def set_color(self, color2):
#         self.__color = color2
#
#     def del_color(self):
#         del self.__color
#
#     color = property(get_color, set_color, del_color)
#
#     def get_speed(self):
#         return self.__speed
#
#     def set_speed(self, speed2):
#         self.__speed = speed2
#
#     def del_speed(self):
#         del self.__speed
#
#     speed = property(get_speed, set_speed, del_speed)
#
#     def get_price(self):
#         return self.__speed
#
#     def set_price(self, prise2):
#         self.__price = prise2
#
#     def del_price(self):
#         del self.__price
#
#     price = property(get_price, set_price, del_price)
#
#
#
# my_car = Car("Malibu", "Qizil", 200, 2500)
#
# print(my_car.model)
# print(my_car.color)
# print(my_car.speed)
# print(my_car.price)
#
#
# my_car.model = "Spark"
# my_car.color = "Ko'k"
# my_car.speed = 90
# my_car.price = 103
#
#
# print(my_car.model)
# print(my_car.color)
# print(my_car.speed)
# print(my_car.price)

#------------------------------------------------------------------------------------------------------

# 2 chi masala

# class Figure:
#
#     def triangle(a, b, c):
#         return a + b + c
#
#     def triangle_area(a, b, c):
#         s = (a + b + c) / 2
#         return (s * (s - a) * (s - b) * (s - c)) ** 0.5
#
#     def rectangle_perimetr(a, b):
#         return 2 * (a + b)
#
#     def recangle_area(a, b):
#         return a * b
#
#
# user = Figure
# print(user.triangle(2, 4, 1))
# print(user.triangle_area(2, 4, 1))
# print(user.rectangle_perimetr(2, 4))
# print(user.recangle_area(2, 4))

#------------------------------------------------------------------------------------------------------

# 3 chi masala

# class Animal:
#
#     model = "Chevrolet"
#     name = "Captiva"
#     speed = 220
#     price = 150000

# print(Animal.__dict__)
# setattr(Animal, "color", "red")
# print(Animal.__dict__)
#------------------------------------------------------------------------------------------------------

# print(getattr(Animal, "model"))
# print(getattr(Animal, "tur", False))
#------------------------------------------------------------------------------------------------------

# print(hasattr(Animal, "price"))
# if not hasattr(Animal, "speed"):
#     Animal.speed = 200
# print(Animal.speed)
#------------------------------------------------------------------------------------------------------

# print(Animal.model)
# del Animal.model
# print(Animal.model)
















































































































