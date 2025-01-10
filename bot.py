from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackContext

# Токен Telegram-бота
TELEGRAM_TOKEN = "7599013879:AAGq_fJ5WdRpmmpzArUMFsQm_CzXgxmszZ8"  # Укажите токен от @BotFather
WEB_APP_URL = "https://your-web-app-url.com"  # Укажите URL вашего мини-приложения

def start(update: Update, context: CallbackContext):
    """Приветственное сообщение с кнопкой для мини-приложения."""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎥 Выбрать фильм", web_app=WebAppInfo(url=WEB_APP_URL))]
    ])
    update.message.reply_text("Привет! Нажми на кнопку, чтобы открыть каталог фильмов:", reply_markup=keyboard)

def main():
    """Запуск бота."""
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()





