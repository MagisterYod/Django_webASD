import datetime
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

p_date = datetime.datetime.now().strftime('%d.%m.%Y').split('.')
p_time = datetime.datetime.now().strftime('%H.%M.%S')
report_folder = os.getenv('LOCAL_REPORT_FOLDER')

users = {
    'it_kuznecovia': 'adm',

}

months = {
    'Январь': '01',
    'Февраль': '02',
    'Март': '03',
    'Апрель': '04',
    'Май': '05',
    'Июнь': '06',
    'Июль': '07',
    'Август': '08',
    'Сентябрь': '09',
    'Октябрь': '10',
    'Ноябрь': '11',
    'Декабрь': '12'
}
months_keys = list(months.items())

techs = {
    45: 'Экскаватор ЭШ 6/45 №17',
    28: 'Самосвал БелАЗ №32',
    31: 'Самосвал БелАЗ №35',
    1: 'Трактор МТЗ-82 №25',
    272: 'Будьдозер ДТ-75А №38',
    9: 'Будьдозер CAT-D6R №28',
    10: 'Будьдозер CAT-D9R №33',
    186: 'Будьдозер CAT-D9R №36',
    4: 'Автогрейдер CAT-140М №4',
    15: 'Автогрейдер Komatsu GD825А-2 №5',
    58: 'Погрузчик CAT-962 №15',
    43: 'Погрузчик CAT-988H №16',
    283: 'Погрузчик Shantui SL60W №26',
    284: 'Погрузчик Shantui SL60W №30',
    286: 'Погрузчик Shantui L58K-B5 №32',
    183: 'Погрузчик CAT-962 №24',
    355: 'Погрузчик Hyundai HL770-9s №27',
    285: 'Погрузчик CAT-988H №31'
}

colors = {
    'top': '#fce5cd',
    'trp': '#fff2cc',
    'krp': '#d9ead3',
    'rgp': '#d0e0e3',
    'oip': '#cfe2f3',
    'ir': '#d9d2e9',
    'bvr': '#ead1dc'
}
