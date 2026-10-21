from random import randint
import requests
from datetime import datetime, timedelta
import datetime as dt


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)

    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer

        self.pokemon_number = randint(1, 1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.height = self.get_height()
        self.weight = self.get_weight()
        self.hp = randint(200, 400)
        self.power = randint(30, 60)
        self.last_feed_time = dt.datetime.now()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    # Метод для получения роста покемона через API
    def get_height(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['height'])
        else:
            return "1"

    # Метод для получения веса покемона через API
    def get_weight(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['weight'])
        else:
            return "1"

    # Метод класса для атаки
    def attack(self, enemy):
        if isinstance(enemy, Wizzard):
            chance = randint(1, 5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            bonus = randint(10, 50)
            self.hp += bonus
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! Earned additional HP: {bonus}"

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}, \n Рост: {self.height}, \n Вес: {self.weight}, \n HP: {self.hp}, \n Сила: {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    def feed(self, feed_interval = 20, hp_increase = 10):
        current_time = datetime.now()
        delta_time = timedelta(hours=feed_interval)

        if (current_time - self.last_feed_time) >= delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time + delta_time}"


class Wizzard(Pokemon):
    def info(self):
        return "You have a Wizzard Pokemon \n\n" + super().info()

    def attack(self, enemy):
        superhp = randint(15, 25)
        self.hp += superhp
        result = super().attack(enemy)
        self.power -= superhp
        return result + f"\nБоец применил супер-атаку силой:{superhp}"

    def feed(self):
        return super().feed(hp_increase=20)


class Fighter(Pokemon):
    def info(self):
        return "You have a Fighter Pokemon \n\n" + super().info()

    def attack(self, enemy):
        superattack = randint(5, 15)
        self.power += superattack
        result = super().attack(enemy)
        self.power -= superattack
        return result + f"\nБоец применил супер-атаку силой:{superattack}"

    def feed(self):
        return super().feed(feed_interval=10)


if __name__ == '__main__':
    wizard = Wizzard("Wizzard")
    fighter = Fighter("Fighter")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))
