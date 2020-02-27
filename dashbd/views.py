from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .pipedrive_client import client
from .forms import NewCustomer

@login_required
def home(request):
    persons = client.persons.get_all_persons()['data']
    products = client.products.get_all_products()['data']

    context = {
        'persons': persons,
        'products': products
    }
    return render(request, 'index.html', context)


def new_customer(request):
    if request.method == 'POST':
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

    form = NewCustomer()
    context = {
        'form': form
    }
    return render(request, 'new_customer.html', context)


def update_customer(request, id):
    pass

def delete_customer(request, id):
    pass
