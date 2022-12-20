from django.shortcuts import render


def indexview(request):
    return render(request, 'main/index.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')
