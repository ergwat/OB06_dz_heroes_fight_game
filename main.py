import time
import random

class Hero():
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def info(self):
        print(f"У героя {self.name} {self.health} здоровья и сила удара {self.attack_power}")

    def attack(self, other):
        this_attack = int(self.attack_power*(random.randint(1, 11)/10))
        other.health -= this_attack
        print(f"{self.name} атаковал героя {other.name}, нанеся {this_attack} урона!")
        print(f"У героя {other.name} осталось {other.health} здоровья \n")

    def is_alive(self):
        return True if self.health > 0 else False


class Game():
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            time.sleep(1)
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"Герой {self.player.name} победил!")
                break
            time.sleep(1)
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"Герой {self.computer.name} победил!")
                break

hero2 = Hero("Железяка", random.randint(1, 101), random.randint(1, 21))
#hero2.info()
print(f"Добро пожаловать на битву героев. Вы будете сражаться с бездушной железякой по имени {hero2.name}.")
time.sleep(1)
print(f"У неё {hero2.health} здоровья и сила удара {hero2.attack_power} единиц.\n")
time.sleep(2)
name = input("Введите ваше имя: ")
health = int(input("Сколько здоровья желаете? "))
attack_power = int(input(f"А силушки сколько богатырской? "))
print("\n")
print("Начинаем бой!")
time.sleep(2)

hero1 = Hero(name, health, attack_power)


game = Game(hero1, hero2)
Game.start(game)