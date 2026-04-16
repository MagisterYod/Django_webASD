from django.views import View
from django.shortcuts import render


class MainView(View):

    @staticmethod
    def get(request):
        addr = request.META['REMOTE_ADDR']
        # profile = models.Profile.objects.get(addr=addr)

        # print(profile.redistribution, profile.user.id, profile.user.username)
        # if str(profile.redistribution) == 'АДМ':
        #     return render(request, 'home.html', context={'var': 'adm', 'user': addr})
        # elif str(profile.redistribution) == 'ПТО':
        #     return render(request, 'home.html', context={'var': 'pto', 'user': addr})
        # elif str(profile.redistribution) == 'ЗИФ':
        #     return render(request, 'home.html', context={'var': 'zif', 'user': addr})
        # else:
        #     return render(request, 'home.html', context={'var': 'no', 'user': addr})

        return render(request, 'home.html')
