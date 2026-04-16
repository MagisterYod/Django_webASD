from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main_page'),
    path('take/', views.TakeDataPage.as_view(), name='take_page'),
    path('insert/<str:month>/<str:year>', views.InsertDataPage.as_view(), name='insert_page'),
    path('get/shift/', views.GetShiftReportPage.as_view(), name='get_shift_page'),
    path('get/cumulative/', views.GetCumulativeReportPage.as_view(), name='get_cumulative_page'),
    path('get/years/', views.GetYearsReportPage.as_view(), name='get_years_page'),
    path('get/overexc/', views.GetShovOverExcavation.as_view(), name='get_overexc_page'),
    path('get/report_17/', views.GetReport17.as_view(), name='get_report_17'),
    path('get/dsk', views.GetReportDSK.as_view(), name='get_report_dsk'),
    path('get/report', views.GetReport.as_view(), name='get_report')
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
