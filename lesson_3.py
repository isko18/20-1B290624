# # " Инкапсуляция "

# #Публичный
# class PublicExample:
#     def __init__(self, value):
#         self.value = value #Публичный атрибут 
        
#     def info(self):
#         return self.value # Публичный метод 
    
# public = PublicExample(42)

# # print(public.info()) #Вызов публичного метода
# # print(public.value) #Доступ к публичному атрибуту

# #Защищенный 
# class ProtectedExample:
#     def __init__(self, value):
#         self._value = value #Защищенный атрибут
        
#     def _info(self):
#         return self._value # Защищенный метод 
    
# protected = ProtectedExample(100)

# print(protected._info())
# print(protected._value)

# # class ExampleProt(ProtectedExample):
# #     def __init__(self, value):
# #         super().__init__(value)
        
# # examp = ExampleProt(120)

# # print(examp._info())
# # print(examp._value)

# #Приватный

# class PravateExample:
#     def __init__(self, value):
#         self.__value = value # Приватный атртбут
        
#     def __info(self):
#         return self.__value #Приватный метод
    
#     def access_private(self):
#         return self.__info() # Публичный метод, где мы получаем доступ к приватному атрибуту
    
# private = PravateExample(300)    
# #Прямой вызов приватного метода вызовет ошибку
# # print(private.__info())

# #Прямой вызов приватного атрибута вызовет ошибку
# # print(private.__value)

# # Доступ через Публичный метод
# # print(private.access_private())

# # Доступ к приватному атрибута через name mangling
# print(private._PravateExample__value)


# class Example(PravateExample):
#     def __init__(self, value, current):
#         super().__init__(value)
#         self._current = current # Защищенный атрибут
        
#     def public(self):
#         print(f"Привтный - {self.__info()}, Защищенный - {self._current}")
        
# example = Example(3, 4)
# # print(exemple.public())
# print(example._PravateExample__value)
import datetime

class Car:
    def __init__(self, mark, model, year, mileage):
        self.mark = mark 
        self.model = model
        self._year = year
        self.__mileage = mileage
        
    def display_info(self):
        print(f'Марка - {self.mark}, \nМодель - {self.model}')
        
    def _calculate_age(self):
        current = datetime.datetime.now().year
        return f'Возраст машины - {current - self._year}'

    def __update_mileage(self):
        print(self.__mileage)
        
    def set_mileage(self):
        return self.__update_mileage()
        
car = Car('Mazda', 'Demio', 2008, 142000)

print(car.mark)
print(car.model)
print(car._year)

# print(car.__mileage) # Доступ по атрибуту ограничен.

# car.__update_mileage(100000)  # Доступ к приватным атрибутам и методам (прямой доступ вызовет ошибку)
print(car._calculate_age())

# print(car.set_mileage())