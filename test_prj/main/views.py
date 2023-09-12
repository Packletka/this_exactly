from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['test_str', 69, 86.2, True],
        'person_obj': {
            'name': 'Вася',
            'age': 23,
            'hobby': 'coding'
        }}
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def news(request):
    return render(request, 'news/home_news.html')
