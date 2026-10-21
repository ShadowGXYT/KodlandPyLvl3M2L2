# Pokémon Telegram Bot

A small Telegram bot that lets you create, view, feed, and battle a Pokémon. The data for names, weight, height, and images is loaded from the public PokeAPI.

## Features

- `/start` – Greeting and explanation
- `/go` – Creates a random Pokémon, Wizzard, or Fighter
- `/info` – Shows information about your Pokémon
- `/feed` – Feeds the Pokémon and increases its health
- `/attack` – Attacks another Pokémon in the bot system

## Project Structure

- `main.py` – Telegram bot and command logic
- `logic.py` – Classes for Pokémon, Wizzard, and Fighter, including battle and feeding logic
- `config.py` – File containing the Telegram bot token

## Setup

1. Create a file named `config.py` in the project folder.
2. Add your Telegram bot token there:

```python
 token = "YOUR_BOT_TOKEN"
```

3. Install the required packages:

```bash
pip install pyTelegramBotAPI requests
```

## Run

```bash
python main.py
```

## Notes

- The bot works only if the token in `config.py` is set correctly.
- A random Pokémon type is chosen when a new game starts.
- Pokémon information is fetched from the PokeAPI and partly generated randomly.

## Example

```text
/start
/go
/info
/feed
/attack
```

This project is a good exercise for OOP, inheritance, API requests, and Telegram bot programming.
