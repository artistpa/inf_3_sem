class SpacePort:
    # Создание космодрома, в котором size штук доков.
    # Доки нумеруются от 0 до size-1.
    # В момент создания все доки свободны.
    # Попытка создать космодром с неположительным числом доков должна приводить к исключению.
    def __init__(self, n):
        if n > 0:
            self.size = n
            self.k = [0] * n
        else:
            raise ValueError()

    # Запросить посадку в док с номером dock_number.
    # Если такого номера дока нет - выбросить exception.
    # Если док есть, но занят - вернуть false (запрет посадки).
    # Если док есть и свободен - вернуть true (разрешение посадки) и док становится занят.
    def request_landing(self, dock_number):
        if dock_number >= 0 and dock_number <= self.size - 1:
            if self.k[dock_number] == 0:
                self.k[dock_number] = 1
                return True
            return False
        else:
            raise IndexError()



    # Запросить взлёт из дока с номером dock_number.
    # Если такого номера дока нет - выбросить exception.
    # Если док есть, но там пусто - выбросить exception.
    # Если док есть и в нём кто-то стоит - вернуть true (разрешение взлёта) и док становится свободен.
    def request_takeoff(self, dock_number):
        if dock_number >= 0 and dock_number <= self.size - 1:
            if (self.k[dock_number] == 1):
                self.k[dock_number] = 0
                return True
            else:
                return "Ooops"
        else:
            raise Exception()

s = SpacePort(5)
print(s.request_landing(0))
print(s.request_landing(4))
try:
    print(s.request_landing(5))
except:
    print("Ooops")

print(s.request_takeoff(0))
print(s.request_takeoff(4))
try:
    print(s.request_takeoff(5))
except:
    print("Ooops")



