from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.forms import ServiceAddForm, LoginForm
from main.models import Service


def indexview(request):
    lastfive = Service.objects.order_by('-date')[:5]
    return render(request, 'main/index.html', {'lastfive': lastfive})


def service(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('service_add')
            else:
                return HttpResponse('Invalid login')

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id = request.user.pk
            form.save()
            return redirect('index')
    else:
        form = ServiceAddForm(initial={'author': request.user})
    context = {'form': form}
    return render(request, 'service_add.html', context)


def service_render(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})
