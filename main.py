from aiogram.types import Message


async def get_form(message: Message):
    await message.answer(f'{message.from_user.first_name}, начинаем заполнять анкету. Введите свое имя')


async def get_name(message: Message):
    name = message.text
    await message.answer(f'Ваше имя:\r\n{name}\r\nТеперь введите фамилию')
    return name


async def get_last_name(message: Message, name: str):
    last_name = message.text
    await message.answer(f'Ваша фамилия:\r\n{last_name}\r\nтеперь введите ваш возраст')
    return last_name


async def get_age(message: Message, name: str, last_name: str):
    age = message.text
    await message.answer(f'Ваш возраст:\r\n{age}\r\n')
    data_user = f'Вот ваши данные\r\n' \
                f'Имя: {name}\r\n' \
                f'Фамилия: {last_name}\r\n' \
                f'Возраст: {age}'
    await message.answer(data_user)
