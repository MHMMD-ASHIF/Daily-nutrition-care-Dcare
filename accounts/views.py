from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .forms import *
from django.forms import inlineformset_factory
from .filter import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from .models import *
from .forms import contactform
import json
import datetime


def introduction(request):
    return render(request, 'accounts/introduction.html')


@login_required(login_url='login')
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'accounts/a_store.html', context)


@login_required(login_url='login')
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'accounts/a_cart.html', context)


@login_required(login_url='login')
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'accounts/a_checkout.html', context)


@login_required(login_url='login')
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('ProductId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


@login_required(login_url='login')
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],


                zipcode=data['shipping']['zipcode'],

            )


    else:
        print("User is not logged in..")
    return JsonResponse('Payment complete', safe=False)


@login_required(login_url='login')
def help(request):
    return render(request, 'accounts/a_home_help.html')


@login_required(login_url='login')
def chat(request):
    return render(request, 'accounts/chat.html')


@login_required(login_url='login')
def menu(request):
    return render(request, 'accounts/menu.html')


@login_required(login_url='login')
def weight_gain(request):
    return render(request, 'accounts/weight_gain.html')


@login_required(login_url='login')
def weight_reduce(request):
    return render(request, 'accounts/weight_reduce.html')


@login_required(login_url='login')
def normal_diet(request):
    return render(request, 'accounts/normal_diet.html')


@login_required(login_url='login')
def food_chart(request):
    return render(request, 'accounts/food_chart.html')


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for  ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@login_required(login_url='login')
def accountSettings(request):
    form = CreateUserForm()

    context = {'form': form}
    return render(request, 'accounts/accounts_settings.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password Incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('intro')


@login_required(login_url='login')
@admin_only
def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}

    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def bmi(request):
    return render(request, 'accounts/BMI.html')


@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/home.html')


@login_required(login_url='login')
def Calorie(request):
    return render(request, 'accounts/calorie.html')


@login_required(login_url='login')
def Nutrition(request):
    nutrition = Nutritious.objects.get(id=1)
    context = {'title': nutrition.title,
               'description': nutrition.description,
               'title_two': nutrition.title_two,
               'description_two': nutrition.description_two}
    return render(request, 'accounts/nutrition.html', context)


@login_required(login_url='login')
def Brain(request):
    context = {}
    return render(request, 'accounts/brain.html', context)


@login_required(login_url='login')
def Eyes(request):
    context = {}
    return render(request, 'accounts/eyes.html', context)


@login_required(login_url='login')
def Heart(request):
    context = {}
    return render(request, 'accounts/heart.html', context)


@login_required(login_url='login')
def Kidney(request):
    context = {}
    return render(request, 'accounts/kidney.html', context)


@login_required(login_url='login')
def Muscles(request):
    context = {}
    return render(request, 'accounts/muscles.html', context)


@login_required(login_url='login')
def Bones(request):
    context = {}
    return render(request, 'accounts/bones.html', context)


@login_required(login_url='login')
def Skin(request):
    context = {}
    return render(request, 'accounts/skin.html', context)


@login_required(login_url='login')
def Hair(request):
    context = {}
    return render(request, 'accounts/hair.html', context)


@login_required(login_url='login')
def Liver(request):
    context = {}
    return render(request, 'accounts/liver.html', context)


@login_required(login_url='login')
def Lungs(request):
    context = {}
    return render(request, 'accounts/lungs.html', context)


@login_required(login_url='login')
def policy(request):
    context = {}
    return render(request, 'accounts/privacy.html', context)


@login_required(login_url='login')
def contact(request):
    context = {}
    return render(request, 'accounts/contact.html', context)


@login_required(login_url='login')
def About(request):
    context = {}
    return render(request, 'accounts/about_us.html', context)


@login_required(login_url='login')
def terms_conditions(request):
    context = {}
    return render(request, 'accounts/terms&conditions.html', context)


@login_required(login_url='login')
def Workout(request):
    context = {}
    return render(request, 'accounts/workouts.html', context)


@login_required(login_url='login')
def beginner(request):
    context = {}
    return render(request, 'accounts/beginner.html', context)


@login_required(login_url='login')
def intermediate(request):
    context = {}
    return render(request, 'accounts/intermediate.html', context)


@login_required(login_url='login')
def advance(request):
    context = {}
    return render(request, 'accounts/advance.html', context)


@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


@login_required(login_url='login')
def shop(request):
    return render(request, 'accounts/shop.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders': orders, 'order_count': order_count, 'myFilter': myFilter}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk_test):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=15)
    customer = Customer.objects.get(id=pk_test)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'accounts/order_forum.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk_test):
    order = Order.objects.get(id=pk_test)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'accounts/order_forum.html', context)


@login_required(login_url='login')
def profile_edit(request):
    account = Users.objects.all()
    user = request.user.users
    form = UsersForm(instance=user)
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form, 'account': account}

    return render(request, 'accounts/profile_edit.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk_test):
    order = Order.objects.get(id=pk_test)
    if request.method == "POST":
        order.delete()
        return redirect('dashboard')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
