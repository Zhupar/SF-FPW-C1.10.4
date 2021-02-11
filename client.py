class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_balance(self):
        return self.balance if isinstance(self.balance, int) else 0

    def __str__(self):
        return f"Клиент '{self.name}'. Баланс: {self.get_balance()} руб"


# client1 = Client('Жупар', 123)
# print(client1)