from client import Client


class Guest(Client):
    def __init__(self, name, city, status):
        super().__init__(name, balance=None)
        self.city = city
        self.status = status

    def __str__(self):
        return f'{self.name}, г.{self.city}, статус: "{self.status}"'


class GuestList:
    def __init__(self, *guests):
        self.list_ = []
        for guest in guests:
            self.list_.append(guest)

    def __str__(self):
        a = ""
        for i, elem in enumerate(self.list_):
            a += f"{i + 1} {elem} \n"
        return f"Список гостей: \n{a}"


g1 = Guest('Жупар', 'Астана', 'Стажер')
g2 = Guest('Максим', 'Москва', 'Наставник')
g3 = Guest('Алиса', 'Екатеринбург', 'Куратор')

l1 = GuestList(g1, g2, g3)
print(l1)
