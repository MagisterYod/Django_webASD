import datetime
from typing import Callable, Any

# import helpers.variables as va


# for i in range(1, 13):
#     if i < 10:
#         i = f'0{i}'
#     va.sql_insert_or_update_budget_result_month(f'01.{i}.2024')
#     print('month', i)
#     try:
#         for j in range(1, 32):
#             if j < 10:
#                 j = f'0{j}'
#             va.sql_insert_or_update_budget_result_24hours(f'{j}.{i}.2024')
#             print('day', f'{j}.{i}.2024')
#             for s in range(1, 3):
#                 va.sql_insert_or_update_budget_result_shift(f'{j}.{i}.2024', s)
#                 print('shift', f'{j}.{i}.2024 shift={s}')
#     except Exception as e:
#         print(e)
#         continue


# va.sql_insert_or_update_budget_result_month('01.11.2024')

# detect_hour: Callable[[Any], int | str] = lambda x: int(x) if x is not None else ""
#
# detect_tens: Callable[[Any], int | str] = lambda x: (
#     int(round(int(f'{x}0') * 0.0167, 0))) if (not str(x).startswith('0')
#                                               and len(str(x)) == 1) else int(round(int(x) * 0.0167, 0))
# detect_minute: Callable[[Any], int | str] = lambda x: (
#     detect_tens(str(x).split('.')[1])) if x is not None and type(x) is float else ""
#
# d = lambda x: int(str(x).split('.')[1]) * 0.0167 if x is not None and len(str(x).split('.')) != 1 else ""
# # detect_minute_2 = lambda x:
# a = 9.03
# b = 10.50
# c = 25
#
# print(a)
# print(str(a))
# print(b)
# print(str(b))
# print(str(a).split('.'))
# print(str(b).split('.'))
# print(str(c).split('.'))
#
# print(detect_hour(a), d(a))
# print(detect_hour(a), detect_minute(a))
# print(detect_hour(b), d(b))
# print(detect_hour(b), detect_minute(b))
# print(detect_hour(b), round(detect_minute(b) / 0.0167))
# print(detect_hour(c), d(c))c

# def check_time(h, m):
#     print('h =', h, 'm =', m)
#     if (
#             h is None and m is None
#             or h == "" and m == ""
#             or h == "0" and m == "0"
#             or h == "" and m == "0"
#             or h == "0" and m == ""
#     ):
#         print(None, '\n')
#     elif (
#             h is not None and len(str(h)) == 1 and h != '0' and m is None
#             or h is not None and len(str(h)) > 1 and m is None
#             or h is not None and len(str(h)) == 1 and h != '0' and m == ""
#             or h is not None and len(str(h)) > 1 and m == ""
#             or h is not None and len(str(h)) == 1 and h != '0' and m == "0"
#             or h is not None and len(str(h)) > 1 and m == "0"
#     ):
#         print('2', h)
#         print(int(h), '\n')
#     elif (
#             h is None and len(str(m)) == 1 and m != '0'
#             or h is None and len(str(m)) > 1 and len(str(m)) > 1 and str(m).startswith('0')
#             or h is not None and len(str(h)) == 1 and h == '0' and len(str(m)) == 1 and m != '0'
#             or h is not None and len(str(h)) == 1 and h == '0' and len(str(m)) > 1 and str(m).startswith('0')
#             or h is not None and h == "" and len(str(m)) == 1 and m != '0'
#             or h is not None and h == "" and len(str(m)) > 1 and str(m).startswith('0')
#     ):
#         print('3', h, str(m))
#         print(float(f'0.0{int(round(int(m) * 1.67, 0))}'), '\n')
#     elif (
#             h is None and len(str(m)) != 1 and not str(m).startswith('0')
#             or h is not None and len(str(h)) == 1 and h == '0' and len(str(m)) > 1 and not str(m).startswith('0')
#             or h is not None and h == "" and len(str(m)) > 1 and not str(m).startswith('0')
#     ):
#         print('4', h, str(m))
#         print(float(f'0.{int(round(int(m) * 1.67, 0))}'), '\n')
#     elif (
#             h is not None and len(str(h)) == 1 and h != '0' and len(str(m)) == 1 and m != '0'
#             or h is not None and len(str(h)) > 1 and len(str(m)) == 1 and m != '0'
#             or h is not None and len(str(h)) > 1 and len(str(m)) == 1 and m != '0'
#             or h is not None and len(str(h)) > 1 and len(str(m)) > 1 and str(m).startswith('0')
#
#     ):
#         print('5', h, str(m))
#         if int(round(int(m) * 1.67, 0)) < 10:
#             print(float(f'{int(h)}.0{int(round(int(m) * 1.67, 0))}'), '\n')
#         else:
#             print(float(f'{int(h)}.{int(round(int(m) * 1.67, 0))}'), '\n')
#     elif (
#             h is not None and len(str(h)) == 1 and h != '0' and len(str(m)) > 1 and not str(m).startswith('0')
#             or h is not None and len(str(h)) > 1 and len(str(m)) > 1 and not str(m).startswith('0')
#             or h is not None and len(str(h)) > 1 and len(str(m)) == 1 and m != '0'
#             or h is not None and len(str(h)) > 1 and len(str(m)) > 1 and str(m).startswith('0')
#     ):
#         print('6', h, str(m))
#         print(float(f'{int(h)}.{int(round(int(m) * 1.67, 0))}'), '\n')
#     else:
#         print('FUCK', '\n')


# check_time("", "")
# check_time("0", "")
# check_time("", "0")
# check_time("0", "0")
# check_time("01", "")
# check_time("1", "")
# check_time("01", "0")
# check_time("1", "0")
# check_time("", "02")
# check_time("", "2")
# check_time("0", "02")
# check_time("0", "2")
# check_time("01", "02")
# check_time("1", "2")
# check_time("10", "")
# check_time("10", "0")
# check_time("122", "01")
# check_time("122", "1")
# check_time("122", "5")
# check_time("122", "06")
# check_time("122", "6")
# check_time("122", "08")
# check_time("122", "8")
# check_time("122", "9")
# check_time("122", "10")
# check_time("122", "20")
# check_time("10", "20")
# check_time("", "20")
# check_time("0", "20")
# check_time("01", "20")
# check_time("1", "20")
# check_time("12", "23")
# check_time("12", "")
# check_time("12", "0")
# check_time("", "23")
# check_time("0", "23")

# for row in va.sql_get_budget_resull_shift('03.12.2024', 1).getvalue().fetchall():
#     print(len(row) ,row, '\n')

# for row in va.sql_get_budget_resull_24hours('06.12.2024').getvalue().fetchall():
#     print(len(row) ,row, '\n')
#
# for row in va.sql_get_budget_resull_month('01.11.2024').getvalue().fetchall():
#     print(len(row) ,row, '\n')

# sec = round(datetime.timedelta(days=0.00486111).total_seconds()/3600, 3)
# print(int(sec), int(sec % 1 / 0.0167))

# months = {
#     '01': 'Январь',
#     '02': 'Февраль',
#     '03': 'Март',
#     '04': 'Апрель',
#     '05': 'Май',
#     '06': 'Июнь',
#     '07': 'Июль',
#     '08': 'Август',
#     '09': 'Сентябрь',
#     '10': 'Октябрь',
#     '11': 'Ноябрь',
#     '12': 'Декабрь'
# }
#
# print(months.get('10'))

# import socket
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('85.140.19.87', 6003))
# client.send(b'hello')
from .helpers.statics import sql_insert_17_overexc


