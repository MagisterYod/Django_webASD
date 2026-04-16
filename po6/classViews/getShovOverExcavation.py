from django.views import View
from django.shortcuts import render, redirect
from ..helpers import sql_get_17_tasks_reports, sql_update_17_overexc, months_keys


class GetShovOverExcavation(View):

    @staticmethod
    def get(request):
        result = []
        for _row in sql_get_17_tasks_reports().getvalue().fetchall():
            result.append([_row[11].strftime('%d.%m.%Y'), _row[12], _row[8] if _row[8] is not None else "", _row[0]])
        return render(request, 'get_overexc.html', context={'result': result, 'months': months_keys})

    @staticmethod
    def post(request):
        result = request.POST
        for k, v in result.items():
            if str(k).startswith('c'):
                continue
            else:
                sql_update_17_overexc(int(k), int(v))
        return redirect('get_overexc_page')
