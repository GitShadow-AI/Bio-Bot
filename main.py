import telebot, time, os, random 

 
bot = telebot.TeleBot("TOKEN")
tconv = lambda x: time.strftime("%H", time.localtime(x))    
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
        name = message.from_user.first_name
        bot.reply_to(message, f'Привет, {name}! Я бот {bot.get_me().first_name}! /start, /hello, /bye, /iron, /glass, /plastic, /organika, /paper ')
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
        bot.reply_to(message, "Пока! Удачи!")
@bot.message_handler(commands=['iron'])
def send_iron(message):
        bot.reply_to(message, '''Алюминий — до 500 лет. Алюминий устойчив к коррозии и может сохранять свои свойства в течение длительного времени.
Железо — примерно за 90–100 лет.
Сталь — может разлагаться в течение несколько сотен лет, в зависимости от условий окружающей среды.
Медь — может разлагаться в течение несколько сотен лет, хотя точные сроки зависят от условий окружающей среды.
Свинец — может разлагаться в течение несколько сотен лет.''' )
@bot.message_handler(commands=['glass'])
def send_glass(message):
        bot.reply_to(message,' стекло в природной среде может разлагаться до 1 млн лет')
@bot.message_handler(commands=['plastic'])
def send_plastic(message):
        bot.reply_to(message,'''Полиэтилен (ПЭ) — от 100 до 1000 лет.
Полиэтилентерефталат (ПЭТ) — около 200 лет.
Полипропилен (ПП) — от 20 до 30 лет.
Полиуретан — от 30 до 50 лет.
Поливинилхлорид (ПВХ) — от 100 до 400 лет.
Стирол-акрилонитрил (SAN) — около 100 лет.
Биопластики (PLA) — от 6 месяцев до 2 лет (в условиях компостирования).''')
@bot.message_handler(commands=['organika'])
def send_organika(message):
        bot.reply_to(message,'''Экскременты без дополнительной переработки разлагаются за порядка 10 дней.
Пищевые отходы разлагаются в природе несколько недель.
Газетная бумага разлагается не меньше месяца, туалетной бумаге для самостоятельной естественной утилизации потребуется всего неделя.
Картон разлагается от двух месяцев до трёх лет. На продолжительность процесса влияют температура и влажность окружающей среды: чем эти параметры выше, тем быстрей он идёт.
Опавшая листва перегнивает за 4–9 месяцев.
Одежда из натуральных волокон разлагается до трёх лет. Для одежды из синтетических тканей период разложения — минимум 50 лет (как и для старой обуви).
Сигаретные окурки разлагаются не меньше 5 лет.''')    
@bot.message_handler(commands=['paper'])
def send_paper(message):
        bot.reply_to(message,'''обычная бумага — месяцы — 2 года;
бумага с полиэтиленовой подкладкой — несколько лет.''')
@bot.message_handler(content_types=['text'])
def send_smile(message):
        r = tconv(message.date)
        emojies = ['(* ^ ω ^)', '(´ ∀ ` *)','(◕‿◕｡)۶','☆*:.｡.o(≧▽≦)o.｡.:*☆', '(o^▽^o)']
        if r == '18':
                bot.reply_to(message, emojies[0])
        elif r == '19':
                bot.reply_to(message, emojies[1])
        elif r == '20':
                bot.reply_to(message, emojies[2])
        elif r == '21':
                bot.reply_to(message, emojies[3])
        else:
                bot.reply_to(message, f'Сейчас {r}, эмодзи грузится') 
        #bot.reply_to(message, gen_smile(r))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
@bot.message_handler(content_types=['text'])
def send_smile(message):
        r = tconv(message.date)
        emojies = ['(* ^ ω ^)', '(´ ∀ ` *)','(◕‿◕｡)۶','☆*:.｡.o(≧▽≦)o.｡.:*☆', '(o^▽^o)']
        if r == '18':
                bot.reply_to(message, emojies[0])
        elif r == '19':
                bot.reply_to(message, emojies[1])
        elif r == '20':
                bot.reply_to(message, emojies[2])
        elif r == '21':
                bot.reply_to(message, emojies[3])
        else:
                bot.reply_to(message, f'Сейчас {r}, эмодзи грузится')    
bot.polling()