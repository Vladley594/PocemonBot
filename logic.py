from random import randint,choice
import requests
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.super_sila = choice(["Молния","Вода","Огонь","Липкость","Природа"])
        self.pokemon_trainer = pokemon_trainer

        self.power = randint(15,25)
        self.hp = randint(50,100)
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.victories = 0
        self.last_feed_time=datetime.now()

        Pokemon.pokemons[pokemon_trainer] = self

    def attack(self, enemy):
        if enemy.hp <=0:
            return f"Враг повержен.Лежачих не бъют!"
        if self.hp <=0:
            return f"Твой покимон погиб героем!Как он будет сражаться дальше?!"

        if isinstance(enemy, Wizard):
            d = randint(1,5)
            if d == 1:
               return "Покемон использовал щит!!" 
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"""Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}
Осталось здоровья:{enemy.hp}"""
        else:
            enemy.hp = 0
            self.victories +=1
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        
    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["sprites"]["other"]["home"]["front_default"]
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
мощь твоего покемона:{self.power}
сила твоего покемона:{self.super_sila}
здоровье твоего покемона:{self.hp}
количество побед твоего покемона:{self.victories}"""

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"



class Fighter(Pokemon):
    def attack(self, enemy):
        c = randint(1,3)
        if c == 1:
            s = randint(1,10)
            self.power += s
            res = super().attack(enemy)+f"\nТвой покемон использовал супер силу мего удара:{s}"
            self.power -= s
            return res
        else:
            return super().attack(enemy)


class Wizard(Pokemon):
    pass
#Всё вверху;)












