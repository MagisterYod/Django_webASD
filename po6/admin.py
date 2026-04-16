from django.contrib import admin
from .models import Profile, Redistribution


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'get_full_name', 'user', 'redistribution', 'addr']


class RedistributionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Redistribution, RedistributionAdmin)
