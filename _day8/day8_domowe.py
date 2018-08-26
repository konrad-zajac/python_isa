# Stwórz fabrykę samochodów (klasę), której będzie można podać liczbę samochodów, markę,
# pojemność silnika i jego moc. Kolor samochodu ma być dobierany losowo z pośród podanych
# - czerwony
# - niebieski
# - czarny
# - pomarańczowy
# Muszę mieć możliwość stworzenia kilku rodzajów samochodów za jednym uruchomieniem fabryki
# Przykład użcia fabryki:
#
# >>> factory = Factory()
# >>> cars = factory.start_production({count: 12, producer: 'mercedes', 2001.0, 200},
# >>>                                 {count: 5, producer: 'tata', 1200.5, 80})
#
# `start_production` ma zwracać listę list samochodów (dla podanego przykładu lista
# na pierwszym miescu będzie posiadała listę 12tu samochodów producenta mercedes
# a na drugim 5 samochodów producenta tata
import random, pprint
colors = ['red','blue','black','orange']

class Factory:
  def __init__(self, car_num:int, car_co:str, eng_vol:int, eng_pow:int):
    self.car_num=car_num   
    self.car_co=car_co   
    self.eng_vol=eng_vol
    self.eng_pow=eng_pow
    self.color=colors[random.randint(0, 3)]
  def start_production(car_num:int, car_company:str, eng_vol:int, eng_pow:int):
    cars_list = ('color: ' + colors[random.randint(0, 3)] + ' count:' +str(car_num) + ', car compny ' + car_company +', '+ str(eng_vol) +', ' + str(eng_pow)) 
    return cars_list

c=Factory(12,'mercedes',2001.0,200)
c2=Factory(5,'tata',1200.5,80)
cars = Factory.start_production(12,'mercedes', 2001, 200)
print(cars)
cars = Factory.start_production(5,'tata',1200.5,80)
print(cars)
