# views.py
from django.db.models import Count, Q
from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

def entry_list(request):
    qs = Entry.objects.all()

    # фильтрация
    name_q = request.GET.get('name')
    program_q = request.GET.get('program')
    if name_q:
        qs = qs.filter(
            Q(last_name__icontains=name_q) |
            Q(first_name__icontains=name_q)
        )
    if program_q:
        qs = qs.filter(program=program_q)

    # сортировка
    order = request.GET.get('order', 'date')
    qs = qs.order_by(order)

    # статистика: сколько записей на каждый балл
    stats = (
        Entry.objects
        .values('score')
        .annotate(count=Count('id'))
        .order_by('score')
    )

    return render(request, 'eduapp/list.html', {
        'entries': qs,
        'stats': stats,
    })

def entry_create(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
    else:
        form = EntryForm()
    return render(request, 'eduapp/form.html', {'form': form})

def entry_stats(request):
    # Получаем распределение: для каждого score — количество записей
    stats = (
        Entry.objects
        .values('score')
        .annotate(count=Count('id'))
        .order_by('score')
    )
    return render(request, 'eduapp/stats.html', {
        'stats': stats,
    })

ABOUT_DATA = {
    "education_link": "https://github.com/vmarshirov/WebApplicationsDevelopment/blob/main/task2/education.txt",
    "my_info": {
        "fio": "Подойников Иван Александрович",
        "photo": "images/maxresdefault.jpg",     # лежит в static/images/maxresdefault.jpg
        "email": "podoynikov@example.com",
        "phone": "+7 (953) 456-78-90"
    },
    "program_info": {
        "name": "Математика",
        "description": "Математика",
        "link": "https://math.hse.ru",
        "director": {
            "fio": "Скрипченко Александра Сергеевна",
            "photo": "images/decan.jpg",
            "email": "skripchenko@example.com"
        },
        "manager": {
            "fio": "Иванова Татьяна Сергеевна",
            "photo": "images/manager.jpg",
            "email": "ivanovats@example.com"
        }
    },
    "classmates": [
        {
            "name": "Яковчук Николай Павлович",
            "photo": "images/kolya.jpg",
            "email": "yakovchuk@example.com",
            "phone": "+7 (111) 111-11-11"
        },
        {
            "name": "Шатов Савва Глебович",
            "photo": "images/savva.jpg",
            "email": "shatov@example.com",
            "phone": "+7 (000) 000-00-00"
        }
    ]
}

def about_me(request):
    return render(request, 'eduapp/about_me.html', ABOUT_DATA)

