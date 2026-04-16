import openpyxl

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from ..helpers import p_date, report_folder, sql_get_budget_result_24hours, insert_technics_result_24hours


class GetCumulativeReportPage(View):

    @staticmethod
    def get(request):
        return render(request, 'get_cumulative_report_page.html', {
            'year': p_date[2]
        })

    @staticmethod
    def post(request):
        def insert_row(dict_res, num):
            item_dict = dict_res.get(num)
            item_dict.append(row)
            result[num_date] = item_dict

        month_post = request.POST.get(f'date')
        if month_post == 'None' or month_post == '':
            return render(
                request,
                'insert_fail_page.html',
                context={
                    'link': 'get_cumulative_page',
                    'e_label': 'Ошибка выбора даты',
                    'e': 'Необходимо выбрать дату'
                })
        month = str(request.POST.get(f'date')).split('-')
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="PO6_cumulative.xlsx"'
        result = {}
        for num_date in range(1, int(month[2]) + 1):
            result[num_date] = []
        for num_date in range(1, int(month[2]) + 1):
            for row in sql_get_budget_result_24hours(f'{num_date}.{month[1]}.{month[0]}').getvalue().fetchall():
                if int(row[1]) == 45:
                    insert_row(result, num_date)
                if int(row[1]) == 28:
                    insert_row(result, num_date)
                if int(row[1]) == 31:
                    insert_row(result, num_date)
                if int(row[1]) == 1:
                    insert_row(result, num_date)
                if int(row[1]) == 272:
                    insert_row(result, num_date)
                if int(row[1]) == 9:
                    insert_row(result, num_date)
                if int(row[1]) == 10:
                    insert_row(result, num_date)
                if int(row[1]) == 186:
                    insert_row(result, num_date)
                if int(row[1]) == 4:
                    insert_row(result, num_date)
                if int(row[1]) == 15:
                    insert_row(result, num_date)
                if int(row[1]) == 58:
                    insert_row(result, num_date)
                if int(row[1]) == 43:
                    insert_row(result, num_date)
                if int(row[1]) == 183:
                    insert_row(result, num_date)
                if int(row[1]) == 283:
                    insert_row(result, num_date)
                if int(row[1]) == 355:
                    insert_row(result, num_date)
                if int(row[1]) == 284:
                    insert_row(result, num_date)
                if int(row[1]) == 285:
                    insert_row(result, num_date)
                if int(row[1]) == 286:
                    insert_row(result, num_date)
        wb = openpyxl.load_workbook(f'{report_folder}PO6_day.xlsx')
        for item, value in result.items():
            ws = wb[str(item)]
            ws['A9'] = f'за {item}.{month[1]}.{month[0]} г.'
            for row in value:
                if row[1] == 45:
                    insert_technics_result_24hours(ws, 23, row)
                if row[1] == 28:
                    insert_technics_result_24hours(ws, 26, row)
                if row[1] == 31:
                    insert_technics_result_24hours(ws, 27, row)
                if row[1] == 1:
                    insert_technics_result_24hours(ws, 43, row)
                if row[1] == 272:
                    insert_technics_result_24hours(ws, 45, row)
                if row[1] == 9:
                    insert_technics_result_24hours(ws, 47, row)
                if row[1] == 10:
                    insert_technics_result_24hours(ws, 48, row)
                if row[1] == 186:
                    insert_technics_result_24hours(ws, 50, row)
                if row[1] == 4:
                    insert_technics_result_24hours(ws, 53, row)
                if row[1] == 15:
                    insert_technics_result_24hours(ws, 54, row)
                if row[1] == 58:
                    insert_technics_result_24hours(ws, 56, row)
                if row[1] == 43:
                    insert_technics_result_24hours(ws, 57, row)
                if row[1] == 183:
                    insert_technics_result_24hours(ws, 58, row)
                if row[1] == 283:
                    insert_technics_result_24hours(ws, 59, row)
                if row[1] == 355:
                    insert_technics_result_24hours(ws, 60, row)
                if row[1] == 284:
                    insert_technics_result_24hours(ws, 61, row)
                if row[1] == 285:
                    insert_technics_result_24hours(ws, 62, row)
                if row[1] == 286:
                    insert_technics_result_24hours(ws, 63, row)
        wb.save(response)
        return response
