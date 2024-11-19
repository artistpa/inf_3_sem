class GasStation:
    # Конструктор, принимающий один параметр - ёмкость резервуара колонки
    # Резервуар создаётся пустой
    def __init__(self, volume):
        self.v = volume
        self.nowv = 0

    # Залить в резервуар колонки n литров топлива
    # Если столько не влезает в резервуар - не заливать ничего, выбросить exception
    def fill(self, n):
        if (self.nowv + n <= self.v):
            self.nowv += n
        else:
            print("Failed to fill")
    # Заправиться, забрав при этом из резервура n литров топлива
    # Если столько нет в резервуаре - не забирать из резервуара ничего, выбросить exception
    def tank(self, n):
        if (self.nowv - n >= 0):
            self.nowv -= n
        else:
            print("Failed to tank")

    # Запросить остаток топлива в резервуаре
    def get_limit(self):
        return self.nowv