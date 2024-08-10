"""" Объектно ориентированное программирование """

# Full_name = 'Омурзаков Нурбек'
# FullName = 'Омурзаков Нурбек'
# print(Full_name.count('f'))

# def add_function():
#     pass

class Car: #шаблон или же чертеж 
    def __init__(self, model, marka, color): #__init__ (магический метод) конструктор
        'Атрибут объекта'
        self.model = model # self (ссылка на текущий объект)
        self.marka = marka
        self.color = color
        'Атрибут класса'
        self.bak = 10
        self.is_start = False
        
    def info(self):
        print(f'Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}')
        
    def start(self):
        if self.bak > 0:
            self.is_start = True
            print(f'Машина {self.marka} - {self.model} заведена')
        else:
            print(f'Машина {self.marka} - {self.model} нет топлива')
            
    def stop(self):
        self.is_start = False
        print(f'Машина {self.marka} - {self.model} заглушено')
        
    def drive(self, city):
        if self.is_start == True:
            print(f"машинa -{self.marka} - {self.model} едет в {city}")
        else:
            print(f"Машина {self.marka} - {self.model} не заведена!")

bmw = Car('m5 f90', 'BMW', 'black')
bmw.info()
bmw.start()
# bmw.stop()
bmw.drive('Катар')

""" Создать класс (Book).Передать параметры (avtor, book_name, year). Создать метод info. Вызвать переданный аргумент """
    

 