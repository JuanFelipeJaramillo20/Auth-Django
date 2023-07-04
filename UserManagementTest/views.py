from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Product
from .decorators import admin_only

def home(request):
    return render(request, 'index.html')


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        passwordConfirmation = request.POST['passwordConfirmation']

        newUser = User.objects.create_user(username, email, password)
        newUser.first_name = firstName
        newUser.last_name = lastName

        newUser.save()

        messages.success(request, 'Your account has been created!')

        return redirect('signing')

    return render(request, 'signup.html')


def signing(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            firstName = user.first_name
            print(user)
            return render(request, 'index.html', {'firstName': firstName})
        else:
            messages.error(request, 'Bad credentials')
            return redirect('home')

    return render(request, 'signin.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged out!")
    return redirect("home")


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

@admin_only
def product_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']

        product = Product(name=name, description=description, price=price)
        product.save()
        return redirect('product_list')

    return render(request, 'product_create.html')

@admin_only
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']

        product.save()
        return redirect('product_list')

    return render(request, 'product_update.html', {'product': product})

@admin_only
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'product_delete.html', {'product': product})


@admin_only
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')