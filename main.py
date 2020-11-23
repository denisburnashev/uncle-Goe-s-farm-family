class Animal():
  def __init__(self, name, speach, weight, product):
    self.name = name
    self.speach = speach
    self.weight = weight
    self.product = product

  def eat(self, food):
    print(f'{self.speach}!!!')
    self.weight = self.weight + food * 0.3

class Goose(Animal):
  def __init__(self, name, speach, weight, product):
    super().__init__(name, speach, weight, product)

  def collecting_eggs(self, producing):
    ammount = producing * 2
    print(f'{self.speach}')
    print(f'вы успешно собрали {int(ammount)} яиц')

class Cow(Animal):
  def __init__(self, name, speach, weight, product, ammount):
    self.ammount = ammount
    super().__init__(name, speach, weight, product)

  def milk_a_cow(self, producing):
    ammount = producing * 13
    self.weight -= ammount
    print(f'{self.speach}')
    print(f'Вы получили {ammount} {self.ammount}s но корова потеряла в весе, тепереь ее вес составляет {self.weight}')

class Sheep(Animal):
  def __init__(self, name, speach, weight, product, condition):
    self.condition = condition
    super().__init__(name, speach, weight, product)

  def shear_a_sheep(self, producing):
    if self.condition == 'woolen':
      self.condition = 'unwoolen'
      print(f'{self.speach}')
      print(f'Вы получили {self.product}')
    elif self.condition == 'unwoolen':
      print('Вы не можете пока подстричь эту овцу')

class Chiken(Animal):
  def __init__(self, name, speach, weight, product):
    super().__init__(name, speach, weight, product)

  def collecting_eggs(self, producing):
    ammount = producing * 20
    print(f'{self.speach}')
    print(f'вы успешно собрали {int(ammount)} яиц')

class Goat(Animal):
  def __init__(self, name, speach, weight, product, ammount):
    self.ammount = ammount
    super().__init__(name, speach, weight, product)

  def milk_a_goat(self, producing):
    ammount = producing * 4
    self.weight -= ammount
    print(f'{self.speach}')
    print(f'Вы получили {ammount} {self.ammount}s но коза потеряла в весе, тепереь ее вес составляет {self.weight}')

class Duck(Animal):
  def __init__(self, name, speach, weight, product):
    super().__init__(name, speach, weight, product)

  def collecting_eggs(self, producing):
    ammount = producing * 2
    print(f'{self.speach}')
    print(f'вы успешно собрали {int(ammount)} яиц')

first = Goose('Серый', 'Honk', 2.23, 'egg')
second = Goose('Белый', 'Honk', 2.87, 'egg')
third = Cow('Манька', 'Moo', 494.67, 'milk', 'liter')
forth = Sheep('Барашек', 'Baa', 87.71, 'wool', 'woolen')
fifth = Sheep('Кудрявый', 'Baa', 113.29, 'wool', 'woolen')
sixth = Chiken('Ко-Ко', 'Cluck', 3.56, 'egg')
seventh = Chiken('Кукареку', 'Cluck', 3.74, 'egg')
eighth = Goat('Рога', 'Baa', 121.11, 'milk', 'liter')
ninth = Goat('Копыта', 'Baa', 127.21, 'milk', 'liter')
tenth = Duck('Кряква', 'Quack', 138.21, 'egg')

animals = []
both_weight = []

animals.append(first)
animals.append(second)
animals.append(third)
animals.append(forth)
animals.append(fifth)
animals.append(sixth)
animals.append(seventh)
animals.append(eighth)
animals.append(ninth)
animals.append(tenth)


def main():
  while True:
    user_input = input('С кем вы хотите взаимодействовать: Гуси, Корова, Овцы, Курицы, Козы , Утка или \n'
                       'введите w для того чтобы узнать общий вес животных \n'
                       'введите t для того чтобы узнать кто из животных весит больше всего: \n'
                       'введите e для того чтобы дать всем животным однаковое кол-во корма: \n')
    if user_input == 'Гуси':
      user_input = input('C каким гусем вы хотите взаимодействовать: Серый или Белый \n')
      if user_input == 'Серый':
        user_input = input('Что вы хотите сделать: накормить или собрать яйца \n')
        if user_input == 'накормить':
          first.eat(float(input('Сколько вы хотите дать корма: ')))
          print(f'Серый гусь набрал в весе и теперь весит: {first.weight}')
        elif user_input == 'собрать яйца':
          first.collecting_eggs(float(input('Сколько часов вы хотите собирать яйца: ')))
      elif user_input == 'Белый':
        user_input = input('Что вы хотите сделать: накормить или собрать яйца \n')
        if user_input == 'накормить':
          second.eat(float(input('Сколько вы хотите дать корма: ')))
          print(f'Серый гусь набрал в весе и теперь весит: {second.weight}')
        elif user_input == 'собрать яйца':
          second.collecting_eggs(float(input('Сколько часов вы хотите собирать яйца: ')))
    elif user_input == 'Корова':
      user_input = input('Что вы хотите сделать: накормить или доить: \n')
      if user_input == 'накормить':
        third.eat(float(input('Сколько вы хотите дать корма: ')))
        print(f'Корова Манька набрала в весе и теперь весит: {third.weight}')
      elif user_input == 'доить':
        third.milk_a_cow(float(input('Сколько часов вы хотите доить корову: ')))
    elif user_input == 'Овцы':
      user_input = input('С какой овцой вы хотите взаимодействовать: Барашек или Кудрявый')
      if user_input == 'Барашек':
          user_input = input('Что вы хотите сделать: накормить или подстричь \n')
          if user_input == 'накормить':
            forth.eat(float(input('Сколько вы хотите дать корма: ')))
            print(f'Барашек набрал в весе и теперь весит: {forth.weight}')
          elif user_input == 'подстричь':
            forth.shear_a_sheep('подстричь')
      if user_input == 'Кудрявый':
          user_input = input('Что вы хотите сделать: накормить или подстричь \n')
          if user_input == 'накормить':
            forth.eat(float(input('Сколько вы хотите дать корма: ')))
            print(f'Барашек набрал в весе и теперь весит: {fifth.weight}')
          elif user_input == 'подстричь':
            fifth.shear_a_sheep('подстричь')
    elif user_input == 'Курицы':
      user_input = input('C каким курицей вы хотите взаимодействовать: Ко-Ко или Кукареку \n')
      if user_input == 'Ко-Ко':
        user_input = input('Что вы хотите сделать: накормить или собрать яйца \n')
        if user_input == 'накормить':
          sixth.eat(float(input('Сколько вы хотите дать корма: ')))
          print(f'Ко-ко набрала в весе и теперь весит: {sixth.weight}')
        elif user_input == 'собрать яйца':
          sixth.collecting_eggs(float(input('Сколько часов вы хотите собирать яйца: ')))
      if user_input == 'Кукареку':
        user_input = input('Что вы хотите сделать: накормить или собрать яйца \n')
        if user_input == 'накормить':
          seventh.eat(float(input('Сколько вы хотите дать корма: ')))
          print(f'Ко-ко набрала в весе и теперь весит: {seventh.weight}')
        elif user_input == 'собрать яйца':
          seventh.collecting_eggs(float(input('Сколько часов вы хотите собирать яйца: ')))
    elif user_input == 'Козы':
      user_input = input('C каким гусем вы хотите взаимодействовать: Рога или Копыта \n')
      if user_input == 'Рога':
        user_input = input('Что вы хотите сделать: накормить или доить \n')
        if user_input == 'накормить':
          eighth.eat(float(input('Сколько вы хотите дать корма: ')))
          print(f'Рога набрала в весе и теперь весит: {eighth.weight}')
        elif user_input == 'доить':
          eighth.milk_a_goat(float(input('Сколько часов вы доить козу: ')))
      elif user_input == 'Копыта':
        user_input = input('Что вы хотите сделать: накормить или доить \n')
        if user_input == 'накормить':
          ninth.eat(float(input('Сколько вы хотите дать корма: ')))
          print(f'Копыта набрал в весе и теперь весит: {ninth.weight}')
        elif user_input == 'доить':
          ninth.milk_a_goat(float(input('Сколько часов вы хотите доить козу: ')))
    elif user_input == 'Утка':
      user_input = input('Что вы хотите сделать: накормить или собрать яйца: \n')
      if user_input == 'накормить':
        tenth.eat(float(input('Сколько вы хотите дать корма: ')))
        print(f'Кряква набрала в весе и теперь весит: {tenth.weight}')
      elif user_input == 'собрать яйца':
        tenth.collecting_eggs(float(input('Сколько часов вы хотите собирать яйца: ')))
    elif user_input == 'w':
      both_weight = 0
      for animal in animals:
        both_weight += animal.weight
      print(f'Общий вес составляет: {both_weight} кг.')
    elif user_input == 't':
      name = ''
      max_weight = 0
      for animal in animals:
        if animal.weight > max_weight:
          max_weight = animal.weight
          name = animal.name
      print(f'{name} самое тяжелое животное. Вес: {max_weight} кг.')
    elif user_input == 'e':
      user_input = float(input('Сколько корма вы хотите дать животным: \n'))
      for animal in animals:
        animal.eat(user_input)
        print(f'Вес {animal.name} изминелся, {animal.weight}')


print(main())