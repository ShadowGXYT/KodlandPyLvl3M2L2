import telebot
from config import token
from logic import Pokemon, Wizzard, Fighter
from random import randint

bot = telebot.TeleBot(token)


pokemon = None


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который поможет тебе создать своего покемона. Для этого введи команду /go")


@bot.message_handler(commands=['go'])
def go(message):
    # if message.from_user.username not in Pokemon.pokemons.keys():
    chance = randint(1, 3)
    if chance == 1:
        pokemon = Pokemon(message.from_user.username)
    elif chance == 2:
        pokemon = Wizzard(message.from_user.username)
    elif chance == 3:
        pokemon = Fighter(message.from_user.username)
    bot.send_message(message.chat.id, pokemon.info())
    bot.send_photo(message.chat.id, pokemon.show_img())
    # else:
    #     bot.reply_to(message, "Ты уже создал себе покемона")


@bot.message_handler(commands=['attack'])
def attack(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        if len(Pokemon.pokemons) > 1:
            for username, pokemon in Pokemon.pokemons.items():
                if username != message.from_user.username:
                    enemy = pokemon
                    break
            result = pok.attack(enemy)
            bot.send_message(message.chat.id, result)
        else:
            bot.send_message(message.chat.id, "Нет других покемонов для атаки")
    else:
        bot.send_message(message.chat.id, "У тебя нет покемона. Создай его командой /go")


@bot.message_handler(commands=['feed'])
def feed(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        result = pok.feed()
        bot.send_message(message.chat.id, result)
    else:
        bot.send_message(message.chat.id, "У тебя нет покемона. Создай его командой /go")


@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())
    else:
        bot.send_message(message.chat.id, "У тебя нет покемона. Создай его командой /go")


bot.infinity_polling(none_stop=True)
