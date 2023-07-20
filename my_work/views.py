from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'my_work/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'my_work/contact.html', context)
