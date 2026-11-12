###########################################
#### There is nothing for you to edit######
########## in this module file.############

class Car:
    def __init__(self, brand, carplate, sheltered = False):
        self.brand = brand
        self.carplate = carplate
        self.sheltered = sheltered

    def getBrand(self):
        return self.brand
    
    def getCarplate(self):
        return self.carplate
    
    def getSheltered(self):
        return self.sheltered
    
    def setSheltered(self):
        self.sheltered = True

car1 = Car('Honda', 'SMJ1234D', True)
car2 = Car('Toyota', 'SBK1200A')
car3 = Car('Seat', 'SJK9898F', True)
car4 = Car('Volvo', 'SGL2134J')
car5 = Car('Honda', 'SFR4545T', True)
car6 = Car('Honda', 'SKR2156H', True)
car7 = Car('Seat', 'SMD6629B', True)
car8 = Car('Volvo', 'SNB2121E')

#################################

def create_car(brand, carplate):
    return Car(brand, carplate)

def get_brand(car):
    return car.getBrand()

def get_carplate(car):
    return car.getCarplate()

def set_sheltered(car):
    car.setSheltered()

def get_sheltered(car):
    return car.getSheltered()

def add_car(carlist, car):
    carlist.append(car)



#### Stack ADT ####

def make_stack(seq):
    new_stack=[]
    for element in seq:
        new_stack.append(element)
    return new_stack

def make_empty_stack():
    return []
    
def clear(stack):
    return stack.clear()

def size(stack):
    return len(stack)