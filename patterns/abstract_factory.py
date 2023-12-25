# Абстрактні класи продуктів
class AbstractProductA:
    def method_a(self):
        pass

class AbstractProductB:
    def method_b(self):
        pass

# Конкретні класи продуктів, які наслідують абстрактні класи
class ConcreteProductA1(AbstractProductA):
    def method_a(self):
        return "Product A1"

class ConcreteProductA2(AbstractProductA):
    def method_a(self):
        return "Product A2"

class ConcreteProductB1(AbstractProductB):
    def method_b(self):
        return "Product B1"

class ConcreteProductB2(AbstractProductB):
    def method_b(self):
        return "Product B2"

# Абстрактна фабрика
class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass

# Конкретні фабрики, які наслідують абстрактну фабрику
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

# Приклад використання:
factory1 = ConcreteFactory1()
product_a1 = factory1.create_product_a()
product_b1 = factory1.create_product_b()

print(product_a1.method_a())  # Виведе: Product A1
print(product_b1.method_b())  # Виведе: Product B1

factory2 = ConcreteFactory2()
product_a2 = factory2.create_product_a()
product_b2 = factory2.create_product_b()

print(product_a2.method_a())  # Виведе: Product A2
print(product_b2.method_b())  # Виведе: Product B2
 
