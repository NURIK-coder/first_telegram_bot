# handlers.py
import requests
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import html

router = Router()

main_commands = [
    'Home',
    'Language',
    'History',
    'Support'
]
limit_page = [
    '1',
    '5',
    '10',
    '12'
]

@router.message(CommandStart())
async def start_handler(message: Message):
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Home'), KeyboardButton(text='Language')],
        [KeyboardButton(text='History')],
        [KeyboardButton(text='Support')],
    ])

    print(message.text)
    await message.answer(f'''
    Hello {html.bold(message.from_user.full_name)}🙋‍♂️
    Id: {message.from_user.id}
    Welcome my not first bot👋''', reply_markup=kb)


@router.message(Command('do', 'work'))
async def do_handler(message: Message):
    await message.answer('OK')


# @router.message(F.text == 'Home')
# async def home(message: Message):
#     await message.answer('Home page!')


@router.message(F.text.in_(main_commands))
async def main_command_handlers(message: Message):
    if message.text == 'Home':
        await message.answer('Home😊')
    elif message.text == 'Language':
        await message.answer('english or spanish?😂')
    elif message.text == 'History':
        await message.answer('I dont know your history🤷‍♂️')
    elif message.text == 'Support':
        await message.answer('Call +998 91 234 56 78📞')
    await message.answer('You didnt select message')



@router.message(Command('users'))
async def main_handler(message: Message):
    limit = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='1'), KeyboardButton(text='5')],
        [KeyboardButton(text='10'), KeyboardButton(text='12')]
    ])

    data = requests.get(f'https://reqres.in/api/users?per_page=12').json()
    user_data = data['data']
    users = ''
    for i in user_data:
        id = i['id']
        first_name = i['first_name']
        last_name = i['last_name']
        users += f'''
ID: {id}
First name: {first_name} 
Last name: {last_name}
---------------------------------------\n'''
    await message.answer(users, reply_markup=limit)

@router.message(F.text.in_(limit_page))
async def filtred_data(message: Message):
    limit = int(message.text)
    limit_kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='1'), KeyboardButton(text='5')],
        [KeyboardButton(text='10'), KeyboardButton(text='12')]
    ])

    data = requests.get(f'https://reqres.in/api/users?per_page={limit}').json()
    user_data = data['data']
    users = ''
    for i in user_data:
        id = i['id']
        first_name = i['first_name']
        last_name = i['last_name']
        users += f'''
ID: {id}
First name: {first_name} 
Last name: {last_name}
---------------------------------------\n'''
    await message.answer(users, reply_markup=limit_kb)
@router.message()
async def user_id(message: Message):
    user = int(message.text)
    data = requests.get(f'https://reqres.in/api/users?per_page=12').json()
    user_data = data['data']
    users = ''
    for i in user_data:
        id = i['id']
        first_name = i['first_name']
        last_name = i['last_name']
        if user == id:
            users += f'''
ID: {id}
First name: {first_name} 
Last name: {last_name}
---------------------------------------\n'''
    await message.answer(users)