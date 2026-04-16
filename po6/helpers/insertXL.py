from typing import Callable


def insert_technics_result_shift(ws, row_tech, df):
    ws[f'F{row_tech}'] = df[4]  # 6 ДВС
    ws[f'H{row_tech}'] = df[5]  # 8 пробег общий
    ws[f'I{row_tech}'] = df[6]  # 9 пробег с грузом
    ws[f'K{row_tech}'] = df[7]  # 11 объем работ план
    ws[f'L{row_tech}'] = df[8]  # 12 объем работ факт
    ws[f'N{row_tech}'] = df[9]  # 14 факт ТО
    ws[f'P{row_tech}'] = df[10]  # 16 факт ТР
    ws[f'R{row_tech}'] = df[11]  # 18 фатк КР
    ws[f'T{row_tech}'] = df[12]  # 20 факт регламент
    ws[f'V{row_tech}'] = df[13]  # 22 факт обед
    ws[f'X{row_tech}'] = df[14]  # 24 факт прием/передача
    ws[f'Z{row_tech}'] = df[15]  # 26 факт забой
    ws[f'AB{row_tech}'] = df[16]  # 28 факт БВР
    ws[f'AC{row_tech}'] = df[17]  # 29 ДВС
    ws[f'AD{row_tech}'] = df[18]  # 30 трансмиссия
    ws[f'AE{row_tech}'] = df[19]  # 31 ходовая
    ws[f'AF{row_tech}'] = df[20]  # 32 навесное
    ws[f'AG{row_tech}'] = df[21]  # 33 электро
    ws[f'AH{row_tech}'] = df[22]  # 34 гибравлика
    ws[f'AI{row_tech}'] = df[23]  # 35 прочие
    ws[f'AJ{row_tech}'] = df[24]  # 36 автошины
    ws[f'AK{row_tech}'] = df[25]  # 37 фронт работ
    ws[f'AL{row_tech}'] = df[26]  # 38 зап.части
    ws[f'AM{row_tech}'] = df[27]  # 39 ГСМ
    ws[f'AN{row_tech}'] = df[28]  # 40 персонал
    ws[f'AO{row_tech}'] = df[29]  # 41 метеоусловия
    ws[f'AP{row_tech}'] = df[30]  # 42 прочие
    ws[f'AT{row_tech}'] = float(df[31])  # 46 фонд времени


def insert_technics_result_24hours(ws, row_tech, df):
    ws[f'F{row_tech}'] = df[3]  # 6 ДВС
    ws[f'H{row_tech}'] = df[4]  # 8 пробег общий
    ws[f'I{row_tech}'] = df[5]  # 9 пробег с грузом
    ws[f'K{row_tech}'] = df[6]  # 11 объем работ план
    ws[f'L{row_tech}'] = df[7]  # 12 объем работ факт
    ws[f'N{row_tech}'] = df[8]  # 14 факт ТО
    ws[f'P{row_tech}'] = df[9]  # 16 факт ТР
    ws[f'R{row_tech}'] = df[10]  # 18 фатк КР
    ws[f'T{row_tech}'] = df[11]  # 20 факт регламент
    ws[f'V{row_tech}'] = df[12]  # 22 факт обед
    ws[f'X{row_tech}'] = df[13]  # 24 факт прием/передача
    ws[f'Z{row_tech}'] = df[14]  # 26 факт забой
    ws[f'AB{row_tech}'] = df[15]  # 28 факт БВР
    ws[f'AC{row_tech}'] = df[16]  # 29 ДВС
    ws[f'AD{row_tech}'] = df[17]  # 30 трансмиссия
    ws[f'AE{row_tech}'] = df[18]  # 31 ходовая
    ws[f'AF{row_tech}'] = df[19]  # 32 навесное
    ws[f'AG{row_tech}'] = df[20]  # 33 электро
    ws[f'AH{row_tech}'] = df[21]  # 34 гибравлика
    ws[f'AI{row_tech}'] = df[22]  # 35 прочие
    ws[f'AJ{row_tech}'] = df[23]  # 36 автошины
    ws[f'AK{row_tech}'] = df[24]  # 37 фронт работ
    ws[f'AL{row_tech}'] = df[25]  # 38 зап.части
    ws[f'AM{row_tech}'] = df[26]  # 39 ГСМ
    ws[f'AN{row_tech}'] = df[27]  # 40 персонал
    ws[f'AO{row_tech}'] = df[28]  # 41 метеоусловия
    ws[f'AP{row_tech}'] = df[29]  # 42 прочие
    ws[f'AT{row_tech}'] = float(df[30])  # 46 фонд времени


def insert_technics_result_month(ws, row_tech, df):
    ws[f'F{row_tech}'] = df[3]  # 6 ДВС
    ws[f'H{row_tech}'] = df[4]  # 8 пробег общий
    ws[f'I{row_tech}'] = df[5]  # 9 пробег с грузом
    ws[f'K{row_tech}'] = df[6]  # 11 объем работ план
    ws[f'L{row_tech}'] = df[7]  # 12 объем работ факт
    ws[f'M{row_tech}'] = df[8]  # 13 план ТО
    ws[f'N{row_tech}'] = df[9]  # 14 факт ТО
    ws[f'O{row_tech}'] = df[10]  # 16 планТР
    ws[f'P{row_tech}'] = df[11]  # 16 факт ТР
    ws[f'Q{row_tech}'] = df[12]  # 18 план КР
    ws[f'R{row_tech}'] = df[13]  # 18 фатк КР
    ws[f'S{row_tech}'] = df[14]  # 20 план регламент
    ws[f'T{row_tech}'] = df[15]  # 20 факт регламент
    ws[f'U{row_tech}'] = df[16]  # 22 план обед
    ws[f'V{row_tech}'] = df[17]  # 22 факт обед
    ws[f'X{row_tech}'] = df[18]  # 24 факт прием/передача
    ws[f'Y{row_tech}'] = df[19]  # 26 план забой
    ws[f'Z{row_tech}'] = df[20]  # 26 факт забой
    ws[f'AA{row_tech}'] = df[21]  # 28 план БВР
    ws[f'AB{row_tech}'] = df[22]  # 28 факт БВР
    ws[f'AC{row_tech}'] = df[23]  # 29 ДВС
    ws[f'AD{row_tech}'] = df[24]  # 30 трансмиссия
    ws[f'AE{row_tech}'] = df[25]  # 31 ходовая
    ws[f'AF{row_tech}'] = df[26]  # 32 навесное
    ws[f'AG{row_tech}'] = df[27]  # 33 электро
    ws[f'AH{row_tech}'] = df[28]  # 34 гибравлика
    ws[f'AI{row_tech}'] = df[29]  # 35 прочие
    ws[f'AJ{row_tech}'] = df[30]  # 36 автошины
    ws[f'AK{row_tech}'] = df[31]  # 37 фронт работ
    ws[f'AL{row_tech}'] = df[32]  # 38 зап.части
    ws[f'AM{row_tech}'] = df[33]  # 39 ГСМ
    ws[f'AN{row_tech}'] = df[34]  # 40 персонал
    ws[f'AO{row_tech}'] = df[35]  # 41 метеоусловия
    ws[f'AP{row_tech}'] = df[36]  # 42 прочие
    ws[f'AT{row_tech}'] = float(df[37])  # 46 фонд времени


def insert_vehicle(sheet, row_num, df):

    columns = [
        'D', 'E', 'F', 'G', 'I', 'J', 'L', 'M', 'N', 'O', 'R', 'S', 'T', 'U', 'X', 'Y', 'Z', 'AA', 'AB', 'AD',
        'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AM', 'AN', 'AO', 'AP', 'AR', 'AS', 'AU', 'AY', 'BR', 'BS'
    ]

    for col in range(0, len(columns) - 1):
        sheet[f'{columns[col]}{row_num}'] = df[col + 1]


def insert_shovels(sheet, row_num, df, point):

    columns = [
        'D', 'E', 'F', 'G', 'H', 'J', 'L', 'M', 'N', 'O', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'AC', 'AD', 'AE',
        'AF', 'AG', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AR', 'AS', 'AT', 'AU', 'AV', 'AX', 'AY', 'BA',
        'BE'
    ]
    none_int: Callable[[None, float], float] = lambda x: x if x is not None else 0
    downtime = (float(none_int(df[14])) + float(none_int(df[15])) + float(none_int(df[16])) + float(none_int(df[17]))
                + float(none_int(df[18])) + float(none_int(df[19])) + float(none_int(df[20])) + float(none_int(df[21]))
                + float(none_int(df[22])) + float(none_int(df[23])) + float(none_int(df[24])) + float(none_int(df[25]))
                + float(none_int(df[26])) + float(none_int(df[27])) + float(none_int(df[28])) + float(none_int(df[29]))
                + float(none_int(df[30])) + float(none_int(df[31])) + float(none_int(df[32])) + float(none_int(df[33]))
                + float(none_int(df[34])) + float(none_int(df[35])) + float(none_int(df[36])) + float(none_int(df[37]))
                + float(none_int(df[38])) + float(none_int(df[39])))
    for col in range(0, len(columns)):
        sheet[f'{columns[col]}{row_num}'] = df[col + 1]
    if point == 'ir':
        sheet[f'S{row_num}'] = None if round(12 - downtime, 2) == 0 else round(12 - downtime, 2)
    if point == 'rd':
        sheet[f'T{row_num}'] = None if round(12 - downtime - float(none_int(df[12])), 2) == 0 else (
            round(12 - downtime - float(none_int(df[12])), 2))
    sheet[f'BH{row_num}'] = df[0]
    sheet[f'BI{row_num}'] = df[41]


def insert_bulls(sheet, row_num, df):

    columns = [
        'D', 'E', 'F', 'I', 'J', 'K', 'L', 'O', 'P', 'Q', 'R', 'S', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'AA', 'AC', 'AD', 'AE', 'AF', 'AH', 'AI', 'AK', 'AO', 'AP', 'AS', 'AU'
    ]

    for col in range(0, len(columns) - 1):
        sheet[f'{columns[col]}{row_num}'] = df[2::][col]


def insert_allstoppagesdet(sheet, row_num, df):

    columns = ['H', 'I', 'J']

    for col in range(0, len(columns)):
        sheet[f'{columns[col]}{row_num}'] = df[2::][col]
