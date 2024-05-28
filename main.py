import telebot

# Вставьте сюда ваш токен
API_TOKEN = 'YOUR TG API'

# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я ваш Telegram бот. Как я могу помочь вам?")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "/start - Начать работу с ботом\n"
        "/help - Получить список команд\n"
        "/perevorot <текст> - Перевернуть введённый текст\n"
        "/caps <текст> - Преобразовать текст в заглавные буквы\n"
        "/cut <текст> - Удалить гласные буквы из текста\n"
        "/len <текст> - Подсчитать количество символов в тексте"
    )
    bot.reply_to(message, help_text)

# Функция для переворота текста
def perevorot_text(text):
    return text[::-1]

# Обработчик команды /perevorot
@bot.message_handler(commands=['perevorot'])
def perevorot(message):
    # Получаем текст после команды /perevorot
    text_to_reverse = message.text[len('/perevorot '):]
    reversed_text = perevorot_text(text_to_reverse)
    bot.reply_to(message, reversed_text)

# Функция для преобразования текста в заглавные буквы
def caps_text(text):
    return text.upper()

# Обработчик команды /caps
@bot.message_handler(commands=['caps'])
def caps(message):
    # Получаем текст после команды /caps
    text_to_caps = message.text[len('/caps '):]
    caps_text_result = caps_text(text_to_caps)
    bot.reply_to(message, caps_text_result)

# Функция для удаления гласных букв из текста
def cut_vowels(text):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return ''.join([char for char in text if char not in vowels])

# Обработчик команды /cut
@bot.message_handler(commands=['cut'])
def cut(message):
    # Получаем текст после команды /cut
    text_to_cut = message.text[len('/cut '):]
    cut_text_result = cut_vowels(text_to_cut)
    bot.reply_to(message, cut_text_result)

# Обработчик команды /len
@bot.message_handler(commands=['len'])
def length(message):
    # Получаем текст после команды /len
    text_to_count = message.text[len('/len '):]
    length_of_text = len(text_to_count)
    bot.reply_to(message, f"Количество символов: {length_of_text}")

# Основной цикл обработки сообщений
bot.polling()
