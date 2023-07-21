#Create a class Product with properties name, price, and quantity. 
#Create a child class Book that inherits from 
#Product and adds a property author and a method called read that prints information about the book.


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
class Book(Product):
    def __init__(self, name, author, price, quantity):
        super().__init__(name, price, quantity)
        self.author = author
    
    def read(self):
        print(f'Book: {self.name}, Author: {self.author}, Cost: {self.price}, Quantity: {self.quantity}')


book_info = Book('Vasya', 'Pupkin', '20 uah', 1)
book_info.read()


#2

class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

    def display_menu(self):
        print('Menu')
        for dish, prices in self.menu.items:
            price = prices['price']
            print(f"{dish}: ${price}")

class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):
        if dish_name not in self.menu:
            return "Dont have it"
        elif quantity > self.menu[dish_name]['quantity']:
            return 'Dont have so many of it'
        else:
            dish_price = self.menu[dish_name]['price']
            total_cost = dish_price*quantity
            self.menu[dish_name]['quantity'] -= quantity
            return f"Total cost: ${total_cost}"


menu =  {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5)) # 25
print(mc.order('burger', 15)) # Requested quantity not available
print(mc.order('soup', 5)) # Dish not available

