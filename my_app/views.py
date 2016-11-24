from django.http import HttpResponse
from django.shortcuts import render
from connection_class import connection, Example

# Create your views here.
from django.views import View
events = [
    {
        'id': 1,
        'name': 'Круг света',
        'image': 'http://metrogorodok.mos.ru/about/staff/Москва,%20фестиваль,%20награда.jpg',
        'will': 5,
        'address': 'красная площадь',
        'description': '1',
        'elect': 0
    },
    {
        'id': 2,
        'name': 'Собрание последователей Кости',
        'image': 'https://pp.vk.me/c630331/v630331731/1c6d9/337_gmvdcTA.jpg',
        'will': 12,
        'address': 'везде',
        'description': 'Ну собарние последователей Кости',
        'elect': 1
    },
    {
        'id': 3,
        'name': 'Тайная вечеря',
        'image': 'http://www.isrageo.com/wp-content/uploads/2016/07/taynayavecherya.jpg',
        'will': 5,
        'address': 'не указано',
        'description': 'Описание',
        'elect': 0
    },
    {
        'id': 4,
        'name': 'Танцы',
        'image': 'http://boombob.ru/img/picture/Apr/04/4c623ea9df05644a5ed3f32e4164740a/1.jpg',
        'will': 5,
        'address': 'адресс',
        'description': 'описание',
        'elect': 0
    },
]

def index(request):
    return render(request, 'index.html', {'events': events, 'width': 100})

def event(request, p):
    ev = events[int(p) - 1]
    return render(request, 'event.html', {'event': ev, 'width': 60})

def laba6(request):
    conn = connection("host1371925_rip", "WouHDWpq", "host1371925_lab6")
    conn.connect()
    with conn:
        user = Example(conn)
        users = user.get()
    return render(request, 'laba6.html', {'users': users, 'title': 'Лаба6'})
