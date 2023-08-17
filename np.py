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
        city_num = input('Введіть, будь ласка місто: ')
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
