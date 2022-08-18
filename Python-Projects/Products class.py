from random import randint


class IdManager:
    def __init__(self):
        self.next_value = 0

    def get_next_id(self):
        result = self.next_value
        self.next_value += 1
        return result


def get_random_date():
    year = 2022
    month = randint(1, 12)
    day = randint(1, 28)
    return "{}/{}/{}".format(year, month, day)


class Product:
    def __init__(self, id, name, exp_date, price):
        self.id = id
        self.name = name
        self.exp_date = exp_date
        self.price = price

    def print(self):
        print("id: {} {} expires at {} and costs {}".format(
            self.id, self.name, self.exp_date, self.price))

    def has_expired(self):
        # calcuate if it has expired and if so return true else false
        # todo
        pass


class Donut(Product):
    def __init__(self, id):
        super().__init__(id, "Donut", get_random_date(), 20)


class Chicken(Product):
    def __init__(self, id):
        super().__init__(id, "Chicken", get_random_date(), 100)


class Chips(Product):
    def __init__(self, id):
        super().__init__(id, "Chips", get_random_date(), 10)


class Store:
    # name property setter
    def set_name(self, name):
        self._name = name

    # name property getter
    def get_name(self):
        return self._name

    # next_id property getter
    # also known as a readonly property because there is no setter
    def get_next_id(self):
        return self.id_manager.get_next_id()

    def __init__(self):
        self._name = None

        # keep track of the instances of products in my store
        self.items = []

        # create an attribute that is a instance of IdManager so that I can use my own personal IdManager
        self.id_manager = IdManager()

        # populate me with donuts
        self.add_donuts(10)

        # populate me with chickens
        self.add_chicken(10)

        # populate me with chips
        self.add_chips(10)

    def add_donuts(self, count):
        for i in range(0, count):
            self.items.append(Donut(self.get_next_id()))

    def add_chicken(self, count):
        for i in range(0, count):
            self.items.append(Chicken(self.get_next_id()))

    def add_chips(self, count):
        for i in range(0, count):
            self.items.append(Chips(self.get_next_id()))

    def print(self):
        for item in self.items:
            item.print()

    # remove from my items all the products that has expired (I threw it away or gave it to Jester)
    def remove_expired_products(self):
        # todo
        pass


# find me all the items that are older than today and print them
def print_expired_items(store):
    # todo
    pass


# how much does expired items cost my company
def calculate_expired_cost(store):
    # todo
    pass


store = Store()
print_expired_items(store)
calculate_expired_cost(store)

store.remove_expired_products()
