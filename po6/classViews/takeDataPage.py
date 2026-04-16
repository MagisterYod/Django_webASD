from django.views import View
from django.shortcuts import render, redirect
from ..helpers import months_keys, p_date


class TakeDataPage(View):

    @staticmethod
    def get(request):
        return render(request, 'take_data_page.html', {
            'months': months_keys,
            'year': p_date[2]
        })

    @staticmethod
    def post(request):
        month = request.POST.get('month')
        year = request.POST.get('year')
        if month == 'None':
            return render(
                request,
                'insert_fail_page.html',
                context={
                    'link': 'take_page',
                    'e_label': 'Ошибка выбора месяца',
                    'e': 'Необходимо выбрать месяц из представленных'
                })
        return redirect('insert_page', month, year)
