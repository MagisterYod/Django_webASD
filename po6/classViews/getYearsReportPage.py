import openpyxl

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from ..helpers import months, p_date, report_folder, sql_get_budget_result_month, insert_technics_result_month


class GetYearsReportPage(View):

    @staticmethod
    def get(request):
        return render(request, 'get_years_report_page.html', {
            'year': p_date[2],
            'months': months
        })

    @staticmethod
    def post(request):

        result = {}

        def insert_row(dict_res, num, _row):
            if dict_res.get(num) is None:
                result[num] = [_row]
            else:
                item_dict = dict_res.get(num)
                item_dict.append(_row)
                result[num] = item_dict

        res_list_m = [
            request.POST.get('month_01'),
            request.POST.get('month_02'),
            request.POST.get('month_03'),
            request.POST.get('month_04'),
            request.POST.get('month_05'),
            request.POST.get('month_06'),
            request.POST.get('month_07'),
            request.POST.get('month_08'),
            request.POST.get('month_09'),
            request.POST.get('month_10'),
            request.POST.get('month_11'),
            request.POST.get('month_12')
        ]
        res_list_q = [
            request.POST.get('quar_01'),
            request.POST.get('quar_02'),
            request.POST.get('quar_03'),
            request.POST.get('quar_04'),
        ]
        res_list_h = [
            request.POST.get('half_01'),
            request.POST.get('half_02'),
        ]
        result_post = set()
        months_post = [int(x) for x in res_list_m if x is not None]
        quarter_post = [list(range(int(x) - 2, int(x) + 1)) for x in res_list_q if x is not None]
        half_post = [list(range(int(x) - 5, int(x) + 1)) for x in res_list_h if x is not None]
        year_post = request.POST.get('year')
        if len(months_post) == 0 and len(quarter_post) == 0 and len(half_post) == 0:
            return render(
                request,
                'insert_fail_page.html',
                context={
                    'link': 'get_years_page',
                    'e_label': 'Ошибка выбора периода',
                    'e': 'Необходимо выбрать период'
                })
        elif len(months_post) != 0 and len(quarter_post) == 0 and len(half_post) == 0:
            for month in months_post:
                result_post.add(month)
        elif (len(months_post) == 0 and len(quarter_post) != 0 and len(half_post) == 0 or
              len(months_post) != 0 and len(quarter_post) != 0 and len(half_post) == 0):
            if len(months_post) == 0:
                for item in quarter_post:
                    for i in item:
                        result_post.add(i)
            else:
                for item in quarter_post:
                    for i in item:
                        result_post.add(i)
                for j in months_post:
                    result_post.add(j)
        elif (len(months_post) == 0 and len(quarter_post) == 0 and len(half_post) != 0 or
              len(months_post) != 0 and len(quarter_post) == 0 and len(half_post) != 0 or
              len(months_post) == 0 and len(quarter_post) != 0 and len(half_post) != 0 or
              len(months_post) != 0 and len(quarter_post) != 0 and len(half_post) != 0):
            if len(months_post) == 0 and len(quarter_post) == 0:
                for item in half_post:
                    for i in item:
                        result_post.add(i)
            elif len(months_post) == 0:
                for item in half_post:
                    for i in item:
                        result_post.add(i)
                for item in quarter_post:
                    for i in item:
                        result_post.add(i)
            else:
                for item in half_post:
                    for i in item:
                        result_post.add(i)
                for item in quarter_post:
                    for i in item:
                        result_post.add(i)
                for j in months_post:
                    result_post.add(j)
        for month_i in sorted(result_post):
            if month_i < 10:
                num_month = f'0{month_i}'
            else:
                num_month = month_i
            for row in sql_get_budget_result_month(str(f'01.{num_month}.{year_post}')).getvalue().fetchall():
                if int(row[1]) == 45:
                    insert_row(result, month_i, row)
                if int(row[1]) == 28:
                    insert_row(result, month_i, row)
                if int(row[1]) == 31:
                    insert_row(result, month_i, row)
                if int(row[1]) == 1:
                    insert_row(result, month_i, row)
                if int(row[1]) == 272:
                    insert_row(result, month_i, row)
                if int(row[1]) == 9:
                    insert_row(result, month_i, row)
                if int(row[1]) == 10:
                    insert_row(result, month_i, row)
                if int(row[1]) == 186:
                    insert_row(result, month_i, row)
                if int(row[1]) == 4:
                    insert_row(result, month_i, row)
                if int(row[1]) == 15:
                    insert_row(result, month_i, row)
                if int(row[1]) == 58:
                    insert_row(result, month_i, row)
                if int(row[1]) == 43:
                    insert_row(result, month_i, row)
                if int(row[1]) == 183:
                    insert_row(result, month_i, row)
                if int(row[1]) == 283:
                    insert_row(result, month_i, row)
                if int(row[1]) == 355:
                    insert_row(result, month_i, row)
                if int(row[1]) == 284:
                    insert_row(result, month_i, row)
                if int(row[1]) == 285:
                    insert_row(result, month_i, row)
                if int(row[1]) == 286:
                    insert_row(result, month_i, row)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename="PO6_{year_post}.xlsx"'
        wb = openpyxl.load_workbook(f'{report_folder}PO6.xlsx')
        for item, value in result.items():
            ws = wb[str(item)]
            ws['A9'] = f'за {list(months.keys())[item - 1]} {year_post} г.'
            for row in value:
                if row[1] == 45:
                    insert_technics_result_month(ws, 23, row)
                if row[1] == 28:
                    insert_technics_result_month(ws, 26, row)
                if row[1] == 31:
                    insert_technics_result_month(ws, 27, row)
                if row[1] == 1:
                    insert_technics_result_month(ws, 43, row)
                if row[1] == 272:
                    insert_technics_result_month(ws, 45, row)
                if row[1] == 9:
                    insert_technics_result_month(ws, 47, row)
                if row[1] == 10:
                    insert_technics_result_month(ws, 48, row)
                if row[1] == 186:
                    insert_technics_result_month(ws, 50, row)
                if row[1] == 4:
                    insert_technics_result_month(ws, 53, row)
                if row[1] == 15:
                    insert_technics_result_month(ws, 54, row)
                if row[1] == 58:
                    insert_technics_result_month(ws, 56, row)
                if row[1] == 43:
                    insert_technics_result_month(ws, 57, row)
                if row[1] == 183:
                    insert_technics_result_month(ws, 58, row)
                if row[1] == 283:
                    insert_technics_result_month(ws, 59, row)
                if row[1] == 355:
                    insert_technics_result_month(ws, 60, row)
                if row[1] == 284:
                    insert_technics_result_month(ws, 61, row)
                if row[1] == 285:
                    insert_technics_result_month(ws, 62, row)
                if row[1] == 286:
                    insert_technics_result_month(ws, 63, row)
        wb.save(response)
        return response
