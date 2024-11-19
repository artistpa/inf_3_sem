class MoneyBox:
    def __init__(self):
        self.number = 0
        self.value = 0

    def add_coin(self, value):
        self.number += 1
        self.value += value

    def get_coins_number(self):
        return(self.number)

    def get_coins_value(self):
        return(self.value)

m = MoneyBox()
# Добавили монетку достоинством 10
m.add_coin(10)
# Добавили монетку достоинством 5
m.add_coin(5)

# Ожидаем, что монеток внутри 2 штуки
print(m.get_coins_number())
# Ожидаем, что общее достоинство всех монеток 15
print(m.get_coins_value())