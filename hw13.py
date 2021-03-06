# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)

# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).

# Предложить свою реализацию классов Unit, Mage, Archer, Knight.

class Unit:
    def __init__(self, name, clan):
        self._agility = 1
        self._intelligence = 1
        self._strength = 1
        self._base_stat = 1
        self.health = 100
        self.clan = clan
        self.name = name

    def increase_health(self, plus_health):
        if plus_health > 199:
            print("Unavailable to increase health.")
            return None

        if self.health == 0:
            print(f"You have been returned to life. Congratulations!")
            self.health += plus_health

        if self.health <= 90:
            print(f"You have healed at {plus_health} points.")
            self.health += plus_health

        if self.health > 100:
            tmp = self.health % 100
            self.health -= tmp

    def decrease_health(self, damage):
        if self.health >= 1:
            self.health -= damage
            print(f"You have taken damage, your current health = {self.health}.")

        if self.health == 0:
            print("YOU DIED")  # reference to the Dark Souls series

    def increase_base_stat(self, lvl):
        self._base_stat += lvl
        if self._base_stat > 10:
            print('\n', "You have reached the highest level.")
            tmp = self._base_stat % 10
            self._base_stat -= tmp
            print(f"Your level has settled at {self._base_stat}.\n")

    def __repr__(self):
        return f"Name: {self.name}"


class Mage(Unit):
    def __init__(self, name, clan, magic_type):
        super().__init__(name, clan)
        self._magic_type = magic_type

    @property
    def increase_lvl(self):
        self._intelligence = self._base_stat
        return self._intelligence

    def __repr__(self):
        self._intelligence = self._base_stat
        return f"Great Mage, his name is {self.name}, belongs to the clan '{self.clan}'.\n" \
               f"His main stat is Intelligence and equals {self._intelligence}.\n" \
               f"Other stats are Strength: {self._strength} and Agility: {self._agility}.\n" \
               f"He is capable of doing {self._magic_type} magic.\n" \
               f"His current health equals {self.health}." if self.health > 0 else "Your hero is dead!"


class Knight(Unit):
    def __init__(self, name, clan, weapon_type):
        super().__init__(name, clan)
        self._weapon_type = weapon_type

    @property
    def increase_lvl(self):
        self._strength = self._base_stat
        return self._strength

    def __repr__(self):
        self._strength = self._base_stat
        return f"Great Knight, his name is {self.name}, belongs to the clan '{self.clan}'.\n" \
               f"His main stat is Strength and equals {self._strength}.\n" \
               f"Other stats are Intelligence: {self._intelligence} and Agility: {self._agility}.\n" \
               f"He can fight with {self._weapon_type}.\n" \
               f"His current health equals {self.health}." if self.health > 0 else "Your hero is dead!"


class Archer(Unit):
    def __init__(self, name, clan, weapon_type):
        super().__init__(name, clan)
        self._weapon_type = weapon_type

    @property
    def increase_lvl(self):
        self._agility = self._base_stat
        return self._agility

    def __repr__(self):
        self._agility = self._base_stat
        return f"Great Archer, his name is {self.name}, belongs to the clan '{self.clan}'.\n" \
               f"His main stat is Agility and equals {self._agility}.\n" \
               f"Other stats are Intelligence: {self._intelligence} and Strength: {self._strength}.\n" \
               f"She can shoot with {self._weapon_type}.\n" \
               f"His current health equals {self.health}." if self.health > 0 else "Your hero is dead!"


gendalf = Mage("Gendalf", "White Mages", "Fire")
gendalf.increase_base_stat(7)
# print('\n', gendalf, '\n')

devian = Knight("Devian", "Dragon Knights", "Divine Rapier")
# devian.increase_base_stat(3)
# devian.decrease_health(100)
# devian.increase_health(199)
# print('\n', devian, '\n')
# print(devian.health)

lyralei = Archer("Lyralei", "Windrangers", "Bow")
lyralei.increase_base_stat(6)
lyralei.decrease_health(20)
lyralei.increase_health(7)
print(lyralei)
