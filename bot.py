# Импортируем класс Логирования - такие модули общего назначения принято импортировать в самом вверху
import logging
# Импортируем компоненты(классы) из библиотек
from telegram.ext import Updater, CommandHandler , MessageHandler, Filters
# 'Updater' - компонент отвечающий за коммуникацию с сервером Telegram - именно он получает/передает сообщения.
# 'CommandHandler' - для обработки команд - смотрит что за команда,ищет обработчкика команда и передает ее ему
# 'MessageHandler' - для обработки сообщений
# 'Filters' - библиотека для фильтров, тоесть чтобы MessegeHandler обрабатывал только Текст
# Классы сами по себе не работают, их надо инстанцировать, положить в переменную

# Импоруем настройки - скрытые переменные, которые не стоит ни кому показывать в ГитХабе
import settings

# Настраиваем логирование
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

# Функция , которую вызывает обработчик команд при нажатии старта в телеграме - приветсвие Пользователя
def greet_user(update, context): # update - информация пришла с платформы телеграм(команда старт, информация о пользователе)
    logger.info('Вызван /Start')
    update.message.reply_text('Здравствуй, пользователь!') # Отвечаем пользователю

# Функция , отвечает за обработку сообщений и за ответ Пользователю
def talk_to_me(update, context):
    text = update.message.text
    logger.info(f'сообщение ЭХО: {text}')
    update.message.reply_text(text)

#Создаем функцию - тело бота
def main():
    mybot = Updater(settings.API_KEY) # В аргументе вписываем АПИ ключ бота - для регистрации

    dp = mybot.dispatcher # Создаем диспетчера и для удобства чтобы не писать каждый раз 'mybot.dispatcher'
    dp.add_handler(CommandHandler('start', greet_user)) # Добавляем обработчик CommandHandler с аргументами('какая команда', Название функции которую он должен вызвать )
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logger.info('Бот запущен')
    mybot.start_polling() # Регулярное обращение за обновлениями
    mybot.idle() # Бесконечный цикл работы - постоянно работает, пока не остановим

# Запускаем Бота
if __name__ == '__main__':
    main()


