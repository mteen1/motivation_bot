import telegram
import random
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from bot_token import bot_token

updater = Updater(f"{bot_token}", use_context=True)

# sticker objects
giga_stick = telegram.Sticker(file_unique_id='AgADSg4AAs9V8VM',
                              file_id='CAACAgQAAxkBAAPYY6A3Pyq0sLoW-1nEbGAGJu4or0sAAkoOAALPVfFTgWfInAT1m_4sBA',
                              width=10, height=398, is_animated=False, type='regular', is_video=True)
cat = telegram.Sticker(file_unique_id='AgADGgADQ7MwHQ',
                       file_id='CAACAgQAAxkBAAPmY6BClHG4IjTyV_gOPjxWZpoblToAAhoAA0OzMB2aBRjYJupZLiwE', width=512,
                       height=509, is_animated=False, type='regular', is_video=False)
cat2 = telegram.Sticker(file_unique_id='AgADGQADQ7MwHQ',
                        file_id='CAACAgQAAxkBAAPnY6BCzFqTo5a9iyFpzFJuag8mmLkAAhkAA0OzMB0BkGQFD7wHiCwE', width=512,
                        height=512, is_animated=False, type='regular', is_video=False)
rick = telegram.Sticker(file_unique_id='AgADMQMAArVx2gY',
                        file_id='CAACAgIAAxkBAAPoY6BC4VOgKy5x86664zOzQ4avatQAAjEDAAK1cdoGop1e4ngmbuYsBA', width=512,
                        height=512, is_animated=True, type='regular', is_video=False)
stickers = [giga_stick, cat2, cat, rick]


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to Mteen bot!\nclick /help for more info")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("/email for email address\n/linkedin for linkedin profile\nsend wisdom for wisdom quotes")


def email_url(update: Update, context: CallbackContext):
    update.message.reply_text("matinmoharami@yahoo.com")


def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://www.linkedin.com/in/matin-moharami/")


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def gigachad(update: Update, context: CallbackContext):
    quotes = ['life is a race, so be racist!?',
              'Do not say a little in many words, but a great deal in a few',
              'Silence is better than unmeaning words',
              "Opportunities don't happen, you create them.",
              "If you’re not positive energy, you’re negative energy.",
              "Love your family, work super hard, live your passion.",
              "Inspiration does exist, but it must find you working.",
              "be yourself!",
              "Every man dies. Not every man lives.",
              "Nothing is impossible. The word itself says “I’m possible!",
              "Be so good they can’t ignore you.",
              "Happiness depends upon ourselves.",
              "Happiness is not by chance, but by choice.",
              "If opportunity doesn’t knock, build a door.",
              "Never, never, never give up.",
              "No pressure, no diamonds.",
              "We will either find a way, or make one.",
              "Make each day your masterpiece.",
              "stay hungry. Stay foolish.",
              "Dream big and dare to fail.",
              "Every moment is a fresh beginning.",
              "No guts, no story.",
              "I’m not afraid of dying, I’m afraid of not trying.",
              "work hard, play harder.",
              ]
    update.message.reply_text(random.choice(quotes))
    update.message.reply_sticker(random.choice(stickers))


def stick_handler(update: Update, context: CallbackContext):
    print("file_unique_id: " + str(update.message.sticker))


def hack(update: Update, context: CallbackContext):
    update.message.reply_text("I'm not hackable bitch")
    update.message.reply_sticker(giga_stick)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('email', email_url))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('wisdom') | Filters.regex('gigachad'), gigachad))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('hack'), hack))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.sticker, stick_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
