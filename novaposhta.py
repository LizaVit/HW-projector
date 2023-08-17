import json
from novaposhta import NovaPoshtaApi

client = NovaPoshtaApi(api_key='d616387301ffa24f5c7f4bd40918926f')

city_part = input('Введіть місто: ')

response = client.address.search_settlements(city_name = city_part, limit = 21).json();
if not response['success']:
    print ('API error:')
    print(response['errors'])
else:
    rec_num = len(response['data'][0]['Addresses']);
    if rec_num == 21:
        print('Забагато записів. Даталізуйте, будь ласка')
    elif rec_num == 0:
        print('Не знайшли такого міста')
    else:
        i = 1
        cities = {}
        for city_rec in response['data'][0]['Addresses']:
            city_name = city_rec['Present']
            city_ref = city_rec['DeliveryCity']
            cities[str(i)] = { 'name': city_name, 'ref': city_ref }
            print(f'{i}. {city_name}')
            i = i + 1
        city_num = input('Виберіть, будь ласка номер населеного пункту: ')
        print('Chosen city:')
        print(cities[city_num]['name'])
        ref = cities[city_num]['ref']

        response2 = client.address.get_warehouses(city_ref = ref, limit = 1000).json();
        if not response2['success']:
             print ('API error:')
             print(response2['errors'])
        else:
            warehouses = {}
            for wh_rec in response2['data']:
                wh_name = wh_rec['Description']
                wh_number = wh_rec['Number']
                wh_ref = wh_rec['Ref']
                warehouses[wh_number] = { 'name': wh_name, 'ref': wh_ref }
                print(f'{wh_name}')
            if len(warehouses) == 0:
                print('На жаль, немає відділень')
            else:
                wh_num = input('Введіть номер відділення: ')
                print('Вибранне відділення:')
                print(warehouses[wh_num]['name'])

# Bot

import json
from novaposhta import NovaPoshtaApi

# Создаем экземпляр API Новой Почты
client = NovaPoshtaApi(api_key='ваш_api_ключ_здесь')

# Определяем коды данных
PHONE_NUMBER = "phone_number"
FULL_NAME = "full_name"
POST_OFFICE_NUMBER = "post_office_number"
DELIVERY_CITY = "delivery_city"
CASE = "case"
DEVICE = "device"

data_prompts = {
    PHONE_NUMBER: 'номер телефону',
    FULL_NAME: 'прізвище, ім\'я та по-батькові',
    POST_OFFICE_NUMBER: 'номер відділення нової пошти',
    DELIVERY_CITY: 'населений пункт',
    CASE: 'обраний кейс',
    DEVICE: 'вашу модель пристрою',
}

async def ask_for_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    assert isinstance(context.user_data, dict)

    current_data = context.user_data.get(CURRENT_DATA)

    if current_data == DELIVERY_CITY:
        city_part = update.message.text
        response = client.address.search_settlements(city_name=city_part, limit=21).json()

        if response['success']:
            i = 1
            cities = {}
            for city_rec in response['data'][0]['Addresses']:
                city_name = city_rec['Present']
                cities[str(i)] = {'name': city_name}
                i = i + 1

            text = "Оберіть місто:\n"
            for num, city in cities.items():
                text += f"{num}. {city['name']}\n"

            await update.message.reply_text(text=text)
            return SELECTING_CITY
        else:
            await update.message.reply_text("Помилка під час отримання списку міст.")
            return ENTERING

    elif current_data == POST_OFFICE_NUMBER:
        chosen_city_number = update.message.text
        chosen_city_name = cities[chosen_city_number]['name']

        city_ref = ...  # Получите city_ref из ранее выбранного города

        response2 = client.address.get_warehouses(city_ref=city_ref, limit=1000).json()

        if response2['success']:
            i = 1
            warehouses = {}
            for wh_rec in response2['data']:
                wh_name = wh_rec['Description']
                warehouses[str(i)] = {'name': wh_name}
                i = i + 1

            text = f"Оберіть відділення у місті {chosen_city_name}:\n"
            for num, warehouse in warehouses.items():
                text += f"{num}. {warehouse['name']}\n"

            await update.message.reply_text(text=text)
            return SELECTING_WAREHOUSE
        else:
            await update.message.reply_text("Помилка під час отримання списку відділень.")
            return ENTERING

    # Добавьте обработку остальных типов данных (FULL_NAME, PHONE_NUMBER и т. д.)

    else:
        text = "Напишіть будь ласка " + data_prompts[current_data]

        if not context.user_data.get(START_OVER):
            if update.callback_query is not None:
                await update.callback_query.answer()
                await update.callback_query.edit_message_text(text=text)
        else:
            if update.message is not None:
                text = "Виберіть варіант"
                await update.message.reply_text(text=text)

        return ENTERING

