class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def reorganisation(self, country):
        new_population = self.population + country.population
        new_country_name = self.name + "_" + country.name
        return Country(new_country_name, new_population)

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia.reorganisation(herzegovina)

print(bosnia_herzegovina.population)
print(bosnia_herzegovina.name)


#2. Implement the previous method with a magic method

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population


    def __add__(self, country):
        new_population = self.population + country.population
        new_country_name = f'{self.name}_{country.name}'
        return Country(new_population, new_country_name)
    

bosnia = Country('Bosnia', 10_000_000)

herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina

print(bosnia_herzegovina.population)

print(bosnia_herzegovina.name)


3. #Create a Car class with the following attributes: brand, model, year, and speed. 
#The Car class should have the following methods: accelerate, brake and display_speed. The accelerate method 
# should increase the speed by 5, #
#and the brake method should decrease the speed by 5. Remember that the speed cannot be negative.

class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    
    def accelarate(self):
        self.speed += 5
    

    def brake(self):
        if self.speed >=5:
            self.speed -=5
        else:
            self.speed = 0


    def display_speed(self):
        print(f"The current speed of the {self.brand} {self.model} is {self.speed} km/h.")


my_car = Car('Lanos', 'Lanos', 1999, 15)
my_car.display_speed()

#4. (Optional) Create a Robot class with the following attributes: orientation 
#(left, right, up, down), position_x, position_y. The Robot class should have the following methods: 
#move, turn, and display_position. The move method should take a number of steps and move the robot 
#in the direction it is currently facing. The turn method should take a direction (left or right) and 
#turn the robot in that direction.The display_position method should print the current position of the robot.

class Robot:
    def __init__(self, orientation, position_x, position_y):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        if self.orientation == 'left':
            self.position_x -= steps
        if self.orientation == 'right':
            self.position_x += steps
        if self.orientation == 'up':
            self.position_y += steps
        if self.orientation == 'down':
            self.position_y -= steps
    
    def turn(self, direction):
        if self.orientation == 'left' and direction == 'left':
            self.orientation = 'down' 
        if self.orientation == 'left' and direction == 'right':
            self.orientation = 'up'
        if self.orientation == 'right' and direction == 'left':
            self.orientation = 'up'
        if self.orientation == 'right' and direction == 'right':
            self.orientation = 'down'
        if self.orientation == 'up' and direction == 'right':
            self.orientation = 'right'
        if self.orientation == 'up' and direction == 'left':
            self.orientation = 'left'
        if self.orientation == 'down' and direction == 'left':
            self.orientation = 'right'
        if self.orientation == 'down' and direction == 'right':
            self.orientation = 'left'

# option 2
#        def turn(self, direction):
#        if direction == "left":
#            orientations = ["left", "down", "right", "up"]
#        elif direction == "right":
#            orientations = ["right", "up", "left", "down"]
#        current_index = orientations.index(self.orientation)
#        self.orientation = orientations[(current_index + 1) % 4]

    def display_position(self):
        print(f'{self.position_x} : {self.position_y} and {self.orientation}')


roboto = Robot("left", 2, 3)
#roboto.display_position()
roboto.move(7)
#roboto.display_position()
roboto.turn('left')
roboto.display_position()
        

    

        






        





