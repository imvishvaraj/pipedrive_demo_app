from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from pipedrive.client import Client
from .forms import NewCustomer, PipedriveKey
from .models import Pipedrive

client = Client(domain="https://digital-dirt.pipedrive.com/")
client.set_api_token("89b7790a4d20c41fada19ce175955c4e3572d188")

@login_required
def hm(request):
    persons = client.persons.get_all_persons()['data']
    products = client.products.get_all_products()['data']

    context = {
        'persons': persons,
        'products': products
    }
    return render(request, 'index.html', context)

class Home(View):
    @login_required
    def get(self, request):
        persons = client.persons.get_all_persons()['data']
        products = client.products.get_all_products()['data']

        context = {
            'persons': persons,
            'products': products
        }
        return render(request, 'index.html', context)


class Customer(View):
    def get(self, request):
        form = NewCustomer()
        context = {
            'form': form
        }
        return render(request, 'new_customer.html', context)

    def post(self, request):
        form = NewCustomer(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            data = {
                'name': name,
                'email': email,
                'phone': phone
            }
        response = client.persons.create_person(data)

        return redirect('home')


class PipeDriveSettings(View):
    def get(self, request):
        key = Pipedrive.objects.all().get()
        form = PipedriveKey()
        context = {
            'form': form,
            'pipedrive_key': key
        }
        return render(request, 'settings.html', context)

    def post(self, request):
        form = PipedriveKey(request.POST or None)
        if form.is_valid():
            key = form.cleaned_data['key']
            print(key)
            data = {
                'key': key
            }
        pkey = Pipedrive(key=key)
        pkey.save()

        return redirect('home')