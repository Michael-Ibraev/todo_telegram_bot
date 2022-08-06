import random
import telebot

token = "5385088020:AAGib96mlhARw7jeuIWY2Fc-zhW-76IuHYU"

bot = telebot.TeleBot(token)

HELP = """/help - напечатать справку по программе.
/add - добавить задачу в список (название задачи запрашивается у пользователя).
/show - напечатать все добавленные задачи.
/exit - выход из программы.
/random - добавлять случайную задачу на сегодня"""

RANDOM_TASKS = ["Почитать", "Побегать", "Убраться дома",
                "Приготовить что-нибудь вкусненькое"]

tasks = {

}

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command [2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "- " + task + "\n"
    else:
        text = "Задач на эту дату нет."
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)