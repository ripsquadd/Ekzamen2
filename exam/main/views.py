from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main.forms import ServiceAddForm
from main.models import Service


def indexview(request):
    return render(request, 'main/index.html')


def service(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceAddForm(request.POST)
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
