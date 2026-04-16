from django.views import View
from django.shortcuts import render
from typing import Callable, Any
from ..helpers import months, techs, sql_get_po6, sql_insert_po6_month


class InsertDataPage(View):

    @staticmethod
    def get(request, month, year):
        month_text = str({i for i in months if months[i] == month}).split("'")[1]
        insert_date = f'{month_text} {year}'

        detect: Callable[[Any], Any | None] = lambda x: x if x is not None else None
        detect_hour: Callable[[Any], int | str] = lambda x: (
            int(str(detect(x)).split('.')[0]) if x is not None and str(detect(x)).split('.')[0] != '0' else "")
        detect_tens: Callable[[Any], int | str] = lambda x: (int(f'{detect(x)}0')) if (
                not str(detect(x)).startswith('0') and len(str(detect(x))) == 1) else int(x)
        detect_minute: Callable[[Any], int | str] = lambda x: int(
            round((detect_tens(str(detect(x)).split('.')[1]) / 1.67), 0)) if x is not None and type(
            detect(x)) is float else ""

        result = {}

        def insert_dict(_row, num):
            result[num] = {
                _row[1]: [
                    {'text': techs.get(_row[1], 0)},
                    {'vol': detect_hour(_row[2])},
                    {'to_h': detect_hour(_row[3])},
                    {'to_m': detect_minute(_row[3])},
                    {'tr_h': detect_hour(_row[4])},
                    {'tr_m': detect_minute(_row[4])},
                    {'kr_h': detect_hour(_row[5])},
                    {'kr_m': detect_minute(_row[5])},
                    {'rg_h': detect_hour(_row[6])},
                    {'rg_m': detect_minute(_row[6])},
                    {'oi_h': detect_hour(_row[7])},
                    {'oi_m': detect_minute(_row[7])},
                    {'ir_h': detect_hour(_row[8])},
                    {'ir_m': detect_minute(_row[8])},
                    {'bv_h': detect_hour(_row[9])},
                    {'bv_m': detect_minute(_row[9])}
                ]
            }

        if len(sql_get_po6(f'01.{month}.{year}').getvalue().fetchall()) != 0:
            for row in sql_get_po6(f'01.{month}.{year}').getvalue().fetchall():
                if row[1] == 45:
                    insert_dict(row, 1)
                if row[1] == 28:
                    insert_dict(row, 2)
                if row[1] == 31:
                    insert_dict(row, 3)
                if row[1] == 1:
                    insert_dict(row, 4)
                if row[1] == 272:
                    insert_dict(row, 5)
                if row[1] == 9:
                    insert_dict(row, 6)
                if row[1] == 10:
                    insert_dict(row, 7)
                if row[1] == 186:
                    insert_dict(row, 8)
                if row[1] == 4:
                    insert_dict(row, 9)
                if row[1] == 15:
                    insert_dict(row, 10)
                if row[1] == 58:
                    insert_dict(row, 11)
                if row[1] == 43:
                    insert_dict(row, 12)
                if row[1] == 183:
                    insert_dict(row, 13)
                if row[1] == 283:
                    insert_dict(row, 14)
                if row[1] == 355:
                    insert_dict(row, 15)
                if row[1] == 284:
                    insert_dict(row, 16)
                if row[1] == 285:
                    insert_dict(row, 17)
                if row[1] == 286:
                    insert_dict(row, 18)
        else:
            insert_dict((None, 45, None, None, None, None, None, None, None, None, None, None, None, None, None), 1)
            insert_dict((None, 28, None, None, None, None, None, None, None, None, None, None, None, None, None), 2)
            insert_dict((None, 31, None, None, None, None, None, None, None, None, None, None, None, None, None), 3)
            insert_dict((None, 1, None, None, None, None, None, None, None, None, None, None, None, None, None), 4)
            insert_dict((None, 272, None, None, None, None, None, None, None, None, None, None, None, None, None), 5)
            insert_dict((None, 9, None, None, None, None, None, None, None, None, None, None, None, None, None), 6)
            insert_dict((None, 10, None, None, None, None, None, None, None, None, None, None, None, None, None), 7)
            insert_dict((None, 186, None, None, None, None, None, None, None, None, None, None, None, None, None), 8)
            insert_dict((None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None), 9)
            insert_dict((None, 15, None, None, None, None, None, None, None, None, None, None, None, None, None), 10)
            insert_dict((None, 58, None, None, None, None, None, None, None, None, None, None, None, None, None), 11)
            insert_dict((None, 43, None, None, None, None, None, None, None, None, None, None, None, None, None), 12)
            insert_dict((None, 183, None, None, None, None, None, None, None, None, None, None, None, None, None), 13)
            insert_dict((None, 283, None, None, None, None, None, None, None, None, None, None, None, None, None), 14)
            insert_dict((None, 355, None, None, None, None, None, None, None, None, None, None, None, None, None), 15)
            insert_dict((None, 284, None, None, None, None, None, None, None, None, None, None, None, None, None), 16)
            insert_dict((None, 285, None, None, None, None, None, None, None, None, None, None, None, None, None), 17)
            insert_dict((None, 286, None, None, None, None, None, None, None, None, None, None, None, None, None), 18)

        result_sorted = sorted(result.items(), key=lambda x: x[0])
        return render(request, 'insert_data_page.html', {
            'insert_date': insert_date,
            'month': month,
            'year': year,
            'result': dict(result_sorted)
        })

    @staticmethod
    def post(request, month, year):

        def check_time(h, m):
            if (
                    h is None and m is None
                    or h == "" and m == ""
                    or h == "0" and m == "0"
                    or h == "" and m == "0"
                    or h == "0" and m == ""
            ):
                return None
            elif (
                    h is not None and len(str(h)) == 1 and h != '0' and m is None
                    or h is not None and len(str(h)) > 1 and m is None
                    or h is not None and len(str(h)) == 1 and h != '0' and m == ""
                    or h is not None and len(str(h)) > 1 and m == ""
                    or h is not None and len(str(h)) == 1 and h != '0' and m == "0"
                    or h is not None and len(str(h)) > 1 and m == "0"
            ):
                return int(h)
            elif (
                    h is None and len(str(m)) == 1 and m != '0'
                    or h is None and len(str(m)) > 1 and len(str(m)) > 1 and str(m).startswith('0')
                    or h is not None and len(str(h)) == 1 and h == '0' and len(str(m)) == 1 and m != '0'
                    or h is not None and len(str(h)) == 1 and h == '0' and len(str(m)) > 1 and str(m).startswith('0')
                    or h is not None and h == "" and len(str(m)) == 1 and m != '0'
                    or h is not None and h == "" and len(str(m)) > 1 and str(m).startswith('0')
            ):
                return float(f'0.0{int(round(int(m) * 1.67, 0))}')
            elif (
                    h is None and len(str(m)) != 1 and not str(m).startswith('0')
                    or h is not None and len(str(h)) == 1 and h == '0'
                    and len(str(m)) > 1 and not str(m).startswith('0')
                    or h is not None and h == "" and len(str(m)) > 1 and not str(m).startswith('0')
            ):
                return float(f'0.{int(round(int(m) * 1.67, 0))}')
            elif (
                    h is not None and len(str(h)) == 1 and h != '0' and len(str(m)) == 1 and m != '0'
                    or h is not None and len(str(h)) > 1 and len(str(m)) == 1 and m != '0'
                    or h is not None and len(str(h)) > 1 and len(str(m)) == 1 and m != '0'
                    or h is not None and len(str(h)) > 1 and len(str(m)) > 1 and str(m).startswith('0')

            ):
                if int(round(int(m) * 1.67, 0)) < 10:
                    return float(f'{int(h)}.0{int(round(int(m) * 1.67, 0))}')
                else:
                    return float(f'{int(h)}.{int(round(int(m) * 1.67, 0))}')
            elif (
                    h is not None and len(str(h)) == 1 and h != '0' and len(str(m)) > 1 and not str(m).startswith('0')
                    or h is not None and len(str(h)) > 1 and len(str(m)) > 1 and not str(m).startswith('0')
                    or h is not None and len(str(h)) > 1 and len(str(m)) == 1 and m != '0'
                    or h is not None and len(str(h)) > 1 and len(str(m)) > 1 and str(m).startswith('0')
            ):
                return float(f'{int(h)}.{int(round(int(m) * 1.67, 0))}')

        result = []
        keys_list = list(techs.keys())
        try:
            for num in keys_list:
                half_res = [
                    f'01.{month}.{year}',
                    num,
                    int(techs.get(num).split('№')[1]),
                    request.POST.get(f'vol_{num}'),
                    check_time(request.POST.get(f'to_h_{num}'), request.POST.get(f'to_m_{num}')),
                    check_time(request.POST.get(f'tr_h_{num}'), request.POST.get(f'tr_m_{num}')),
                    check_time(request.POST.get(f'kr_h_{num}'), request.POST.get(f'kr_m_{num}')),
                    check_time(request.POST.get(f'rg_h_{num}'), request.POST.get(f'rg_m_{num}')),
                    check_time(request.POST.get(f'oi_h_{num}'), request.POST.get(f'oi_m_{num}')),
                    check_time(request.POST.get(f'ir_h_{num}'), request.POST.get(f'ir_m_{num}')),
                    check_time(request.POST.get(f'bv_h_{num}'), request.POST.get(f'bv_m_{num}'))
                ]
                result.append(half_res)
        except Exception as e:
            return render(
                request,
                'insert_fail_page.html',
                context={
                    'link': 'main_page',
                    'e_label': 'Ошибка внесения данных',
                    'e': e
                })
        for item in result:
            sql_insert_po6_month(
                item[0],
                item[1],
                item[2],
                item[3],
                item[4],
                item[5],
                item[6],
                item[7],
                item[8],
                item[9],
                item[10],
            )
        return render(request, 'insert_success_page.html')
