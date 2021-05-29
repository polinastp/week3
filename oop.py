class Product:
    def __init__(self, name, price, stock = 0, discount = 10, max_discount = 20):
        self.name = name
        if len(self.name) < 2:
            raise ValueError('Название товара должно быть 2 симвала или больше')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def discounted(self):
        return self.price - self.price * self.discount / 100
    
    def sell(self, item_count = 1):
        if item_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        self.stock -= item_count
    
    def get_color(self):
        raise NotImplementedError

    def __repr__(self):
        return f'<Product name: {self.name}, price: {self.price}, stock: {self.stock}>'

product1 = Product('Product', 100, stock = 10)
print(product1)
product1.sell(5)
print(product1)

class Phone(Product):
    def __init__(self, name, price, color, stock = 0, discount = 0, max_discount = 20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
    
    def get_color(self):
        return f'Phone color: {self.color}'

    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'

my_phone = Phone('Iphone', -1000, 'Black')
print(my_phone)
print(my_phone.color)

class Sofa(Product):
    def __init__(self, name, price, color, fabric, stock = 0, discount = 0, max_discount = 20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
        self.fabric = fabric
    
    def get_color(self):
        return f'Sofa color: {self.color}'

    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'

my_phone = Phone('Iphone', -1000, 'Black')
print(my_phone)
print(my_phone.color)
print(my_phone.get_color())

sofa1 = Sofa('Small sofa', 3000, 'Pink', 'Leather')
print(sofa1.get_color())
# print(sofa1)
# print(sofa1.color)
# print(sofa1.fabric)

