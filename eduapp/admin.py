# eduapp/admin.py
from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    # поля, которые увидите в таблице
    list_display = (
        'id',
        'last_name',
        'first_name',
        'program',
        'email',
        'phone',
        'score',
        'date',
    )

    # фильтры справа: по программе, по баллу, по дате
    list_filter = (
        'program',
        'score',
        'date',
    )

    # строка поиска по фамилии, имени и e-mail
    search_fields = (
        'last_name',
        'first_name',
        'email',
    )

    # по умолчанию сортировать по дате (от поздних к старым)
    ordering = ('-date',)

    # править прямо в списке можно будет балл и телефон
    list_editable = (
        'score',
        'phone',
    )

    # опционально: максимально сколько записей одновременно
    list_per_page = 25
