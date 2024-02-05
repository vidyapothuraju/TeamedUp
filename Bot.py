"""Bot for telegram"""
# import asyncio
import logging
import sqlite3# , os, pathlib

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from Bot_scripts.scripts import sort_sport_data, string_maker

storage = MemoryStorage()

API_TOKEN = '6111677280:AAEVGmw4i0YlEoKKONKcGq6mVVqG7t81JMM'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)

class User_state(StatesGroup):
    '''Class for auth. persons'''
    auth = State()
    find_id = State()
    page = 3
    end = 0

async def send_massege_from_all_participants(id, sport):
    '''Function for notifications about new sportsman'''
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    for i in cur.execute("SELECT Telegram_id FROM TeamedUp_univer_profile WHERE Active = ?", (1,)).fetchall():
        try:
            await bot.send_message(i[0], "We have new sportsman!\n"+"id: "+str(id)+'\nSport: '+str(sport))
        except:
            pass
    cur.close()
    conn.close()


async def send_welcome(message: types.Message):
    '''Start's function'''
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    check = "@"+message.from_user.username
    if (check in cur.execute("SELECT Telegram FROM TeamedUp_univer_profile WHERE Telegram=?", (check,)).fetchall()[0])\
            and (cur.execute("SELECT Active FROM TeamedUp_univer_profile WHERE Telegram=?", (check,)).fetchall()[0][0]):
        await User_state.auth.set()
        button_menu = KeyboardButton("/menu")
        greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_menu)
        temp = str(message.from_user.id)
        cur.execute("UPDATE TeamedUp_univer_profile SET Telegram_id = ? WHERE Telegram=?", (temp, check))
        conn.commit()
        await message.answer("hi", reply_markup=greet_kb1)

    elif not "@"+check in cur.execute("SELECT Telegram FROM TeamedUp_univer_profile WHERE Telegram=?",
                                      (check)).fetchall()[0]:
        await message.answer("Sorry, we don't know <b>who you are</b>.")
    else:
        await message.answer("Yours profile is <b>NOT</b> activated. Please contact support.")
    cur.close()
    conn.close()

def main_menu_button():
    button_all_sportsman = KeyboardButton("/all")
    button_find_sportsman = KeyboardButton("/find")
    button_back_to_menu = KeyboardButton("/back_to_menu")
    return ReplyKeyboardMarkup(resize_keyboard=True).add(button_all_sportsman).add(button_find_sportsman)\
        .add(button_back_to_menu)

async def main_menu(message: types.Message):
    '''Main menu for work'''
    await message.answer("What do you would like to see:\n/all - All athletes\n/find - Find athlete",
                         reply_markup=main_menu_button())

def sport_data_default_db():
    '''Getter of all sportsman'''
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    t = cur.execute("SELECT * FROM TeamedUp_profile").fetchall()
    cur.close()
    conn.close()
    return t

def sport_data_default_button():
    '''Default menu for sportsman pages'''
    b0 = KeyboardButton("/First")
    b1 = KeyboardButton("/<<")
    b2 = KeyboardButton("/>>")
    b3 = KeyboardButton("/Last")
    button_back_to_menu = KeyboardButton("/back_to_menu")
    return ReplyKeyboardMarkup(resize_keyboard=True).row(b0, b1, b2, b3).add(button_back_to_menu)

async def sportsman_first_page(message: types.Message):
    '''Go to last sportsman's page'''
    t=sport_data_default_db()
    for i in range(len(t[-1])):
        print(i-1,t[-1][i])
    User_state.page = 3
    User_state.end = 0
    for i in t[User_state.page-3+User_state.end:User_state.page]:
        await message.answer(i[0])
        await message.answer(string_maker(sort_sport_data(i)),reply_markup=sport_data_default_button())

async def sportsman_last_page(message: types.Message):
    '''Go to first sportsman's page'''
    t=sport_data_default_db()
    User_state.page = len(t)
    User_state.end = 0
    for i in t[User_state.page-3+User_state.end:User_state.page]:
        await message.answer(i[0])
        await message.answer(string_maker(sort_sport_data(i)),reply_markup=sport_data_default_button())

async def sportsman_plus_page(message: types.Message):
    '''Show last 3 profile'''
    t=sport_data_default_db()
    if User_state.page!=len(t):
        if User_state.page+3<=len(t):
            User_state.page+=3
        else:
            User_state.end = 3-(len(t)-User_state.page)
            User_state.page = len(t)
    else:
        User_state.page = 3
        User_state.end = 0
    for i in t[User_state.page-3+User_state.end:User_state.page]:
        await message.answer(i[0])
        await message.answer(string_maker(sort_sport_data(i)),reply_markup=sport_data_default_button())

async def sportsman_minus_page(message: types.Message):
    '''Show next 3 profile'''
    t = sport_data_default_db()
    if User_state.page!=3:
        if User_state.page-3>3:
            User_state.page-=3
        else:
            User_state.end = 3-(len(t)-User_state.page)
            User_state.page = 3
    else:
        User_state.page = len(t)
        User_state.end = 0
    for i in t[User_state.page-3+User_state.end:User_state.page]:
        await message.answer(i[0])
        await message.answer(string_maker(sort_sport_data(i)),reply_markup=sport_data_default_button())



async def find_sportsman_menu(message: types.Message):

    await message.answer("Please choose filter(/filter)", reply_markup=None)
    sport_menu = [
        'find_id',
    ]
    mes = ''
    for i in sport_menu:
        mes = i.replace('_', ' ')+': /'+i
    find_id_button = KeyboardButton("/find_id")
    await message.answer(mes, reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(find_id_button))

async def enter_sportsman_id(message: types.Message):
    await message.answer("Please, enter id")
    await User_state.find_id.set()

async def find_sportsman_id(message: types.Message):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    try:
        await message.answer(string_maker(sort_sport_data(cur.execute("SELECT * FROM TeamedUp_profile WHERE id=?",
                                                                      (str(int(message.text)),)).fetchone())),
                             reply_markup=main_menu_button())
    except:
        await message.answer('Wrong id', reply_markup=main_menu_button())
    cur.close()
    conn.close()
    await User_state.auth.set()

'''handlers'''
dp.register_message_handler(send_welcome, commands=['start', 'help'], state='*')
dp.register_message_handler(main_menu, commands=['menu', 'back_to_menu'], state=User_state.auth)

dp.register_message_handler(sportsman_last_page, commands=['all'], state=User_state.auth)
dp.register_message_handler(sportsman_minus_page, commands=['>>'], state=User_state.auth)
dp.register_message_handler(sportsman_plus_page, commands=['<<'], state=User_state.auth)
dp.register_message_handler(sportsman_first_page, commands=['Last'], state=User_state.auth)
dp.register_message_handler(sportsman_last_page, commands=['First'], state=User_state.auth)

dp.register_message_handler(find_sportsman_menu, commands=['find'], state=User_state.auth)
dp.register_message_handler(enter_sportsman_id, commands=['find_id'], state=User_state.auth)
dp.register_message_handler(find_sportsman_id, content_types=['any'], state=User_state.find_id)

"""async def before_start():
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    for i in cur.execute("SELECT Telegram_id FROM TeamedUp_univer_profile WHERE Active = ?", (1,)).fetchall():
        try:
            await bot.send_message(i[0],text='Please, press /start')
        except:
            pass
    cur.close()
    conn.close()"""

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
