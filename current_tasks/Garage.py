# Базовый класс машины
class Car:
    def __init__(self, c, s, n):
        self.capacity = int(c)
        self.speed = int(s)
        self.number = n

# Грузовик
class Truck(Car):
    pass

# Автобус
class Bus(Car):
    pass

class Garage:
    def __init__(self):
        self.cars = []

    # Запарковать машину v
    def park(self, v):
        self.cars.append(v)
    # Пересчитать машины заданного типа t.
    # Вернуть количество.
    def count(self, t):
        c = 0
        for i in range(len(self.cars)):
            if isinstance(self.cars[i], t):
                c += 1
        return c

    # Получить самую быструю машину заданного типа t.
    # Вернуть экземпляр.
    def get_fastest_of_type(self, t):
        c = t(0, 0, "1")
        for i in range(len(self.cars)):
            if isinstance(self.cars[i], t) and self.cars[i].speed >= c.speed:
                c = self.cars[i]
        return c

# Создаём гараж
g = Garage()
# Паркуем машины
g.park(Car(1, 100, "abc"))
g.park(Truck(1000, 150, "zzz"))
g.park(Bus(100, 50, "QWE"))
g.park(Bus(100, 80, "ASD"))
g.park(Bus(100, 20, "ZXC"))

# Сколько всего машин? Ожидаем 5, потому что грузовик и автобус - тоже машины.
print(g.count(Car))
# Сколько всего грузовиков? Ожидаем 1.
print(g.count(Truck))
# Сколько всего автобусов? Ожидаем 3.
print(g.count(Bus))
# Получим самую быструю машину и выведем её номер. Ожидаем zzz, потому что грузовик внезапно самый быстрый.
print(g.get_fastest_of_type(Car).number)
# Получим самый быстрый грузовик и выведем его номер. Ожидаем zzz.
print(g.get_fastest_of_type(Truck).number)
# Получим самый быстрый автобус и выведем его номер. Ожидаем ASD.
print(g.get_fastest_of_type(Bus).number)

