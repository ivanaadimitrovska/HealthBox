from django.contrib.auth import authenticate, login
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from app.forms import ProductForm, UserAuthenticationForm, PaymentForm, AdminAuthenticationForm, LoginForm
from app.models import Product, UserAuthentication, Cart, AdminProfile, Order
from django.contrib import messages


def index(request):
    return render(request, "index.html")


def customer(request):
    if request.method == "POST":
        form_data = UserAuthenticationForm(request.POST, request.FILES)
        if form_data.is_valid():
            user = form_data.save(commit=False)
            user.save()

            user_authentication = UserAuthentication.objects.create(
                user=user,
                name=form_data.cleaned_data['name'],
                surname=form_data.cleaned_data['surname']
            )

            return redirect("glavna")
        else:
            print(form_data.errors)
    else:
        form_data = UserAuthenticationForm()
    return render(request, "register.html", context={"form": form_data})


def addProduct(request):
    if request.method == "POST":
        form_data = ProductForm(request.POST, request.FILES)
        if form_data.is_valid():
            post = form_data.save(commit=False)
            post.image = form_data.cleaned_data['image']
            post.save()
            return redirect("addPr", product_id=post.id)
        else:
            print(form_data.errors)
    return render(request, "addProduct.html", context={"form": ProductForm})


def delete_product(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        return redirect('addProduct')
    else:
        return redirect('addProduct')


def editProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form_data = ProductForm(request.POST, request.FILES, instance=product)
        if form_data.is_valid():
            form_data.save()
            return redirect("addPr", product_id=product.id)
    else:
        form = ProductForm(instance=product)
        return render(request, "editProduct.html", {'form': form, 'product': product})


def adminLogin(request):
    if request.method == "POST":
        form_data = AdminAuthenticationForm(request.POST, request.FILES)
        if form_data.is_valid():
            user = form_data.save(commit=False)
            user.save()
            print(user.id)

            admin_profile = AdminProfile.objects.create(
                user=user,
                name=form_data.cleaned_data['name'],
                surname=form_data.cleaned_data['surname']
            )
            print(admin_profile.id)

            return redirect("addProduct")
        else:
            print(form_data.errors)
    else:
        form_data = AdminAuthenticationForm()
    return render(request, "registerAdmin.html", context={"form": form_data})


def addPr(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'dodaden.html', {'product': product})


def glavna(request):
    return render(request, 'glavnaStrana.html')


def cokoladni(request):
    candies = Product.objects.filter(category__name='Vegetables')

    context = {
        'candies': candies
    }

    print(candies)
    return render(request, 'cokoladni.html', context)


def cotton(request):
    candies = Product.objects.filter(category__name='Cotton Candy')

    context = {
        'candies': candies
    }

    return render(request, 'cotton.html', context)


def chewing(request):
    candies = Product.objects.filter(category__name='Chewing Gum')

    context = {
        'candies': candies
    }

    return render(request, 'chewing.html', context)


def hard(request):
    candies = Product.objects.filter(category__name='Hard Candy')

    context = {
        'candies': candies
    }

    return render(request, 'hard.html', context)


def gummy(request):
    candies = Product.objects.filter(category__name='Gummy Candy')

    context = {
        'candies': candies
    }

    return render(request, 'gummy.html', context)


def lollipop(request):
    candies = Product.objects.filter(category__name='Lollipop')

    context = {
        'candies': candies
    }

    return render(request, 'lollipop.html', context)


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        candy_type = request.POST.get('candyType')
        quantity = int(request.POST.get('quantity', 100))

        product = get_object_or_404(Product, name=candy_type)

        user = request.user

        cart_item = Cart(product=product, quantity=quantity, user=user)
        cart_item.save()

        return redirect('cart')

    return HttpResponseBadRequest()


def cart(request):
    return render(request, 'cart.html')


def gummy(request):
    gummy_candies = Product.objects.filter(category__name='Gummy Candy')
    context = {'candies': gummy_candies}
    return render(request, "gummy.html", context)


def gummyIngre(request):
    candies = Product.objects.filter(category__name='Gummy Candy')
    context = {
        'candies': candies
    }
    return render(request, "allIngredientsGummy.html", context)


def chewingIngre(request):
    candies = Product.objects.filter(category__name='Chewing Gum')
    context = {
        'candies': candies
    }
    return render(request, "allIngredientsChewing.html", context)


def chocoIngre(request):
    candies = Product.objects.filter(category__name='Chocolate Candy')
    context = {
        'candies': candies
    }
    return render(request, "allIngredientsChocolate.html", context)


def cottonIngre(request):
    candies = Product.objects.filter(category__name='Cotton Candy')
    context = {
        'candies': candies
    }
    return render(request, "allIngredientsCotton.html", context)


def hardIngre(request):
    candies = Product.objects.filter(category__name='Hard Candy')
    context = {
        'candies': candies
    }
    return render(request, "allIngredientsHard.html", context)


def lollipopIngre(request):
    candies = Product.objects.filter(category__name='Lollipop')
    context = {
        'candies': candies
    }
    return render(request, "allIngredientsLollipop.html", context)


def ingredients(request):
    chocolates = Product.objects.filter(category__name='Chocolate Candy')
    cotton_candies = Product.objects.filter(category__name='Cotton Candy')
    chewing = Product.objects.filter(category__name='Chewing Gum')
    lollipop = Product.objects.filter(category__name='Lollipop')
    hard = Product.objects.filter(category__name='Hard Candy')
    gummy_candy = Product.objects.filter(category__name='Gummy Candy')

    context = {}

    if chocolates.exists():
        context['chocolates'] = chocolates
        return render(request, "allIngredientsChocolate.html", context)
    elif cotton_candies.exists():
        context['cotton_candies'] = cotton_candies
        return render(request, "allIngredientsCotton.html", context)
    elif chewing.exists():
        context['cotton_candies'] = cotton_candies
        return render(request, "allIngredientsChewing.html", context)
    elif lollipop.exists():
        context['cotton_candies'] = cotton_candies
        return render(request, "allIngredientsLollipop.html", context)
    elif hard.exists():
        context['cotton_candies'] = cotton_candies
        return render(request, "allIngredientsHard.html", context)
    elif gummy_candy.exists():
        context['gummy_candies'] = gummy_candy
        return render(request, "allIngredientsGummy.html", context)
    else:
        return HttpResponse("No candies found.")


@login_required
def kosnicka(request):
    cart_items = Cart.objects.filter(user=request.user)

    quantities = {}

    for cart_item in cart_items:
        product_name = cart_item.product.name
        quantity = cart_item.quantity
        if product_name in quantities:
            if quantity is not None:
                quantities[product_name]['quantity'] += quantity
        else:
            quantities[product_name] = {'quantity': quantity or 0,
                                        'image_url': cart_item.product.image.url if cart_item.product.image else None}

    return render(request, 'cart.html', {'quantities': quantities})


def cancel_order(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        if product_name:
            cart_items = Cart.objects.filter(user=request.user, product__name=product_name)

            if cart_items.exists():
                cart_items.delete()

    return redirect('cart')


def finish(request):
    return render(request, "finish.html")


def payment(request):
    if request.method == "POST":
        form_data = PaymentForm(request.POST, request.FILES)
        if form_data.is_valid():
            post = form_data.save(commit=False)
            post.save()
            return redirect("finish")
        else:
            print(form_data.errors)
    return render(request, "payment.html", context={"form": PaymentForm})


def blog(request):
    return render(request, "ourBlog.html")


def aboutUs(request):
    return render(request, "aboutUs.html")


def contact(request):
    return render(request, "contact.html")


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('glavna')
            else:
                error_message = 'Invalid username or password, please register to our site!'
                messages.error(request, error_message)
    else:
        form = LoginForm()

    return render(request, 'adminCustomer.html', {'form': form})


def login_viewAdmin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('addProduct')
            else:
                error_message = 'Invalid username or password, please register to our site!'
                messages.error(request, error_message)
    else:
        form = LoginForm()

    return render(request, 'adminLogin.html', {'form': form})
