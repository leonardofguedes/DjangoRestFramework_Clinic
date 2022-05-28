from django.contrib import admin
from Schedule.models import Room, Doctor


class Rooms(admin.ModelAdmin):
    list_display = ('id', 'number','name')
    list_display_links = ('number',)
    search_fields = ('number', 'name',)
    list_per_page = 10


admin.site.register(Room, Rooms)


class Doctors(admin.ModelAdmin):
    list_display = ('nome', 'especialidade', 'crm', 'email')
    list_display_links = ('nome', 'crm')
    search_fields = ('nome', 'crm')


admin.site.register(Doctor, Doctors)