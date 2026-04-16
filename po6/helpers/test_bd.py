import oracledb
import datetime

import openpyxl
from openpyxl.styles import NamedStyle, Font, Border, Side, Alignment
from statics import report_folder
from insertXL import insert_vehicle, insert_shovels

p_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%d.%m.%Y')
oracledb.init_oracle_client(config_dir='C:\\app\product\instantclient_12_2')
connection = oracledb.connect(user='ORACLEASD', password='OracleASD', dsn='piteservice')
cursor = connection.cursor()

"Вставка нормальной даты у грейдера №5 после сбоя даты"


#def sql_get_17_tasks_reports(truck_id):
#    cursor.callproc('ZSU.INSERT_OR_UPDATE_TRUCK_ID_AUX', [truck_id])


#sql_get_17_tasks_reports(15)

"Выгрузка суточного объема воды за период"


# def sql_get_wellmetervalue(date, shift):
#     sql_get_wellmetervalue_result = cursor.var(oracledb.CURSOR)
#     cursor.callproc('ZSU.EXPORTFULLREPORT.GET_WELLMETERVALUE', [date, shift, sql_get_wellmetervalue_result])
#     return sql_get_wellmetervalue_result
#
#
# res_sum = 0
# res_mtime = 0
# for i in range(1, 29):
#     sum = 0
#     mtime = 0
#     for j in range(1, 3):
#         for row in sql_get_wellmetervalue(f'{i}.02.2026', j).getvalue():
#             sum += row[1]
#             mtime += row[2]
#             break
#     res_sum += sum
#     res_mtime += mtime
#     print(f'Дата: {i}.02.2026\nОбъем: {sum}, Моточасы: {mtime}\nПолный объем: {res_sum}, Общая наработка: {res_mtime} \n')


"Выгрузка Самосвалы в Рапорт"

#
# def sql_get_vehicle(date, shift):
#     sql_get_vehicle_result = cursor.var(oracledb.CURSOR)
#     cursor.callproc('ZSU.EXPORTFULLREPORT.GET_VEHICLE', [date, shift, sql_get_vehicle_result])
#     return sql_get_vehicle_result
#
#
# def sql_get_bulls(date, shift):
#     sql_get_bulls_result = cursor.var(oracledb.CURSOR)
#     cursor.callproc('ZSU.EXPORTFULLREPORT.GET_BULLS', [date, shift, sql_get_bulls_result])
#     return sql_get_bulls_result
#
#
# def sql_get_allstoppagesdet(date):
#     sql_get_allstoppagesdet_result = cursor.var(oracledb.CURSOR)
#     cursor.callproc('ZSU.EXPORTFULLREPORT.GET_ALLSTOPPAGESDET', [date, sql_get_allstoppagesdet_result])
#     return sql_get_allstoppagesdet_result
#
#
# def sql_get_wellmetervalue(date, shift):
#     sql_get_wellmetervalue_result = cursor.var(oracledb.CURSOR)
#     cursor.callproc('ZSU.EXPORTFULLREPORT.GET_WELLMETERVALUE', [date, shift, sql_get_wellmetervalue_result])
#     return sql_get_wellmetervalue_result
#
#
# def insert_vehicle(sheet, row_num, df):
#
#     columns = [
#         'D', 'E', 'F', 'G', 'I', 'J', 'L', 'M', 'N', 'O', 'R', 'S', 'T', 'U', 'X', 'Y', 'Z', 'AA', 'AB', 'AD',
#         'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AM', 'AN', 'AO', 'AP', 'AR', 'AS', 'AU', 'AY', 'BR', 'BS'
#     ]
#
#     for col in range(0, len(columns) - 1):
#         sheet[f'{columns[col]}{row_num}'] = df[col + 1]
#
#
# def insert_allstoppagesdet(sheet, row_num, df):
#
#     columns = ['H', 'I', 'J']
#
#     for col in range(0, len(columns)):
#         sheet[f'{columns[col]}{row_num}'] = df[1::][col]
#

def sql_get_allstoppagesdet(date):
    sql_get_allstoppagesdet_result = cursor.var(oracledb.CURSOR)
    cursor.callproc('ZSU.GET_ALLSTOPPAGESDET', [date, sql_get_allstoppagesdet_result])
    return sql_get_allstoppagesdet_result


def insert_allstoppagesdet(sheet, row_num, df):

    columns = ['H', 'I', 'J']

    for col in range(0, len(columns)):
        sheet[f'{columns[col]}{row_num}'] = df[2::][col]


def report_insert(date, shift):

    result_query_allstoppagesdet = []
    if shift == '0':
        # for sh in range(1, 3):
        result_query_allstoppagesdet.append(sql_get_allstoppagesdet(date).getvalue().fetchall())

    wb = openpyxl.load_workbook(f'{report_folder}report.xlsx')

    ws = wb[str('Техника new')]
    for rows in result_query_allstoppagesdet:
        row = rows[0]
        if len(row) > 0:
            if row[1] == 45:
                insert_allstoppagesdet(ws, 9, row)
            if row[1] == 28:
                insert_allstoppagesdet(ws, 12, row)
            if row[1] == 31:
                insert_allstoppagesdet(ws, 13, row)
            if row[1] == 186:
                insert_allstoppagesdet(ws, 15, row)
            if row[1] == 9:
                insert_allstoppagesdet(ws, 16, row)
            if row[1] == 4:
                insert_allstoppagesdet(ws, 18, row)
            if row[1] == 15:
                insert_allstoppagesdet(ws, 19, row)
            if row[1] == 58:
                insert_allstoppagesdet(ws, 21, row)
            if row[1] == 283:
                insert_allstoppagesdet(ws, 22, row)
            if row[1] == 183:
                insert_allstoppagesdet(ws, 23, row)
            if row[1] == 43:
                insert_allstoppagesdet(ws, 24, row)
            if row[1] == 284:
                insert_allstoppagesdet(ws, 25, row)
            if row[1] == 285:
                insert_allstoppagesdet(ws, 26, row)
            if row[1] == 286:
                insert_allstoppagesdet(ws, 27, row)

    wb.save(f'report_{date}.xlsx')


report_insert('07.03.2026', '0')


