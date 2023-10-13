class Watch():
    pass

    def __str__(self) -> str:
        return 'Klasa Zegarek z funkcji STR'

watchOne = Watch()
print(watchOne)
print('----')
# Dziedziczenie 
class Phone ():
    def phoneGeneral(self):
        return 'Telefony mobilne'

class Samsung (Phone):
    def __init__(self, system):
        self.system = system
    def samsung(self):
        return ('To jest Samsung')
    
class Iphone (Samsung):
    def __init__(self, system, kind='15 PRO'):
        super().__init__(system)
        self.kind = kind
    def iphone (self):
        return 'To jest Iphone'



#Instancje
phoneOne = Phone()
phoneTwo = Samsung('Android')
phoneThree = Iphone('IOS', )

# Printujemy Metody
print(phoneOne.phoneGeneral())
print('----')
print(phoneTwo.phoneGeneral())
print(phoneTwo.samsung())
print(phoneTwo.system)
print('----')
print(phoneThree.phoneGeneral())
print(phoneThree.iphone())
print(phoneThree.system)
print(phoneThree.kind)
print('----')

# Dwie klasy dziedziczące po Container
class Container(): 
    pass

class PlasticContainer(Container):
    pass

class MetalContainer(Container):
    pass

# issubclass - Czy klasy dziedziczą po drugiej klasie:
class Watch():
    pass

class Garmin(Watch):
    pass

class Coffee():
    pass

testResult = issubclass(Garmin, Watch)
testResultTwo = issubclass(Coffee, Watch)
print(testResult)
print(testResultTwo)
print('----')

# MRO -  lista klas w kolejności MRO dla klasy TwoCrisp - check która metoda zostanie wywołana
class Crisp():
    def crisp (self):
        return 'To są cipsy'

class Lays (Crisp):
    pass

class Pringles (Crisp):
    pass

class TwoCrisp (Lays, Pringles):
    pass

print(TwoCrisp.mro())
print('----')

# Metoda specjalna: __repr__ 
class Car():
    def __init__ (self, category=None):
        self.category  = category if category else 'Pojazd lądowy'
    
    def __repr__(self):
        return f"{self.__class__.__name__}: category={self.category}"

class Land(Car):
    pass

class Air (Car):
    def __init__(self, category=None):
        self.category = category if category else 'Pojazd powietrzny'

carOne = Car()
carTwo = Land()
carThree = Air()
print(carOne.category)
print(carTwo.category)

instances = [carOne, carTwo, carThree]

for car in instances:
    print(car)
print('----')

# wyświetlenie nazwy klasy oraz wartość atrybutu:
class Walk():
    def __init__(self, walks):
        self.walks = walks
    def display_info(self):
        return f"Klasa: {self.__class__.__name__} => {self.walks}"

walk = Walk('Spacer z Husky')
print (walk.display_info())
print('----')

# __dict__ - wyświetlenie wszystkich atrybutów metod
class Vehicle ():
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

class CarTwoVehicle (Vehicle):
    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower

vehicle = Vehicle('Tesla', 'Czerwony', 2020)
carTwoVehicle = CarTwoVehicle ('Tesla', 'Czerwony', 2020, 300)
print(vehicle.__dict__)
print(carTwoVehicle.__dict__)
print('----')

# super ()
class EnergyDrink():
    def __init__(self, brand):
        self.brand = brand
    def energy (self):
        return 'Uwielbiam energy Drinki'
    
class Tiger (EnergyDrink):
    def __init__(self, brand, quantity):
        super().__init__(brand)
        self.quantity = quantity

energyOne = EnergyDrink('Red bull')
energyTwo = Tiger('Tiger', 2)

print(f"Energy Drink: {energyOne.brand}. {energyOne.energy()}")
print(f"Energy Drink: {energyTwo.brand}. Dzisiaj kupiłem: {energyTwo.quantity} szt.")

# kolejny przykład super ()
class CoffeDrink():
    def __init__(self, brand, opinion):
        self.brand = brand
        self.opinion = opinion
    def display_attrs(self):
        return f"Brand => {self.brand}\nOpinion => {self.opinion}"


class TeaDrink(CoffeDrink):
    def __init__(self, brand, opinion, taste):
        super().__init__(brand, opinion)
        self.taste = taste

coffeDrink = CoffeDrink('Costa', 'Pyszna')
coffeTea = TeaDrink('Lipton', 'całkiem dobra', 'Ok')

print(coffeDrink.display_attrs())
print(coffeTea.display_attrs())
print('----')

# self.__dict__.items()

class Pool ():
    def __init__(self, size, localization):
        self.size = size
        self.localization = localization

    def display(self):
        print(f"Calling from class: {self.__class__.__name__}")
        for attr, value in self.__dict__.items():   
            print (f"{attr} => {value}")
        
poolFirst = Pool('25m', 'Bielany')
poolFirst.display()
print('----')

class PoolOpen (Pool):
    def __init__(self, size, localization, open):
        super().__init__(size, localization)
        self.open = open

poolSecond = PoolOpen('50m', 'Moczydło', '9:00')
poolSecond.display()
print('----')

# Pusta klasa oraz check issubclass()
class Container():
    pass
class TemperatureControlledContainer (Container):
    pass
class RefrigeratedContainer (TemperatureControlledContainer):
    pass

print(issubclass(TemperatureControlledContainer, Container))
print(issubclass(RefrigeratedContainer, TemperatureControlledContainer))
print(issubclass(RefrigeratedContainer, Container))
print('----')

# getattr() - wyciągnięcie danych
class ContainerTemp:
    cat = 'general'

class Temp(ContainerTemp):
    temp_range = (-25.0, 5.0)

temp_range_value = getattr(Temp, 'temp_range')
print(temp_range_value)

# Dziedziczenie wielokrotne 