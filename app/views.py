import urllib

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, F
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponse, JsonResponse
from dateutil.parser import parse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from app.forms import ProductForm, UserAuthenticationForm, PaymentForm, AdminAuthenticationForm
from app.models import Product, UserAuthentication, Cart, AdminProfile, Order


def index(request):
    return render(request, "index.html")


def customer(request):
    if request.method == "POST":
        form_data = UserAuthenticationForm(request.POST, request.FILES)
        if form_data.is_valid():
            user = form_data.save(commit=False)  # Step 1: Create a new user record in auth_user table
            user.save()

            user_authentication = UserAuthentication.objects.create(
                # Step 2: Create a new UserAuthentication record associated with the user
                user=user,
                name=form_data.cleaned_data['name'],
                surname=form_data.cleaned_data['surname']
            )

            return redirect("glavna")
        else:
            print(form_data.errors)
    else:
        form_data = UserAuthenticationForm()
    return render(request, "adminCustomer.html", context={"form": form_data})


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
    return render(request, "adminLogin.html", context={"form": form_data})


def addPr(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'dodaden.html', {'product': product})


def glavna(request):
    return render(request, 'glavnaStrana.html')


def cokoladni(request):
    candies = Product.objects.filter(category__name='Chocolate Candy')

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


# @login_required
# def add_to_cart(request):
#     if request.method == 'POST':
#         candy_type = request.POST.get('candyType')
#         #decoded_candy_type = urllib.parse.unquote(candy_type)
#         product_id = request.POST.get('productId')
#         quantity = 100  # Assuming a fixed quantity of 100 grams
#
#         # Retrieve the product from the database
#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             return redirect('add_to_cart')  # or show an error message
#
#         # Get the authenticated user
#         user = request.user
#
#         # Create or update the cart item
#         cart_item, created = Cart.objects.get_or_create(user=user, product=product)
#         if not created:
#             cart_item.quantity += quantity
#             cart_item.save()
#
#     return redirect('add_to_cart')


# @login_required
# def add_to_cart(request):
#     if request.method == 'POST':
#         # Get the product details from the request
#         product_id = request.POST.get('product_id')
#         quantity = int(request.POST.get('quantity', 1))  # Default to 1 if quantity is not provided
#
#         # Retrieve the product from the database
#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             return redirect('cart')  # or show an error message
#
#         # Get the authenticated user
#         user = request.user
#
#         # Retrieve or create the cart item
#         cart_item, created = Cart.objects.get_or_create(product=product, user=user)
#
#         # Update the quantity
#         if created:
#             cart_item.quantity = quantity
#         else:
#             cart_item.quantity += quantity
#
#         cart_item.save()
#
#     return redirect('add_to_cart')

# from django.shortcuts import get_object_or_404

@login_required  # OVA E TOCHNOTO
def add_to_cart(request):
    if request.method == 'POST':
        # Get the candy type and quantity from the request
        candy_type = request.POST.get('candyType')
        quantity = int(request.POST.get('quantity', 100))

        # Retrieve the product from the database
        product = get_object_or_404(Product, name=candy_type)

        # Get the authenticated user
        user = request.user

        # Create a new cart item for each click
        cart_item = Cart(product=product, quantity=quantity, user=user)
        cart_item.save()

        return redirect('cart')  # or redirect to the appropriate page

    return HttpResponseBadRequest()


# @login_required
# def add_to_cart(request):
#     if request.method == 'POST':
#         # Get the product details from the request
#         product_id = request.POST.get('product_id')
#         quantity = int(request.POST.get('quantity', 1))  # Default to 1 if quantity is not provided
#
#         # Retrieve the product from the database
#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             return redirect('cart')  # or show an error message
#
#         # Get the authenticated user
#         user = request.user
#
#         # Check if the product is already in the cart for the user
#         cart_item, created = Cart.objects.get_or_create(user=user, product=product)
#
#         # Update the quantity of the cart item
#         cart_item.quantity += quantity
#         cart_item.save()
#
#     return redirect('cart')


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
        context['gummy_candies'] = gummy_candy  # Update the key to 'gummy_candies'
        return render(request, "allIngredientsGummy.html", context)
    else:
        return HttpResponse("No candies found.")
    # candies = Product.objects.filter(category__name='chocolate')
    #
    # context = {
    #     'candies': candies
    # }
    # return render(request, "allIngredientsChocolate.html", context)


def kosnicka(request):
    cart_items = Cart.objects.filter(user=request.user)

    # quantities = {}
    #
    # for cart_item in cart_items:
    #     product_name = cart_item.product.name
    #     quantity = cart_item.quantity
    #     if product_name in quantities:
    #         if quantity is not None:
    #             quantities[product_name] += quantity
    #     else:
    #         quantities[product_name] = quantity or 0
    #
    # # Pass the quantities dictionary to the template for rendering
    # return render(request, 'cart.html', {'quantities': quantities})

    # quantities = {}
    #
    # for cart_item in cart_items:
    #     product_name = cart_item.product.name
    #     quantity = cart_item.quantity
    #     if product_name in quantities:
    #         if quantity is not None:
    #             quantities[product_name] += quantity
    #     else:
    #         quantities[product_name] = quantity or 0
    #
    # # Fetch the product images using the product names
    # product_images = {product.name: product.image for product in Product.objects.filter(name__in=quantities.keys())}
    #
    # # Pass the quantities and product_images dictionaries to the template for rendering
    # return render(request, 'cart.html', {'quantities': quantities, 'product_images': product_images})

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

    # quantities = {}
    #
    # for cart_item in cart_items:
    #     product_name = cart_item.product.name
    #     quantity = cart_item.quantity
    #     category = cart_item.product.category.name  # Get the category name
    #
    #     if category == 'Cotton Candy':
    #         # Adjust the quantity for "Cotton Candy" product
    #         quantity += 1  # Assuming 1 piece = 100 grams
    #
    #     if product_name in quantities:
    #         if quantity is not None:
    #             quantities[product_name]['quantity'] += quantity
    #     else:
    #         quantities[product_name] = {'quantity': quantity or 0,
    #                                     'category': category,  # Add the category information
    #                                     'image_url': cart_item.product.image.url if cart_item.product.image else None}
    #
    # return render(request, 'cart.html', {'quantities': quantities})


# def cancel_order(request, product_name):
#     # Retrieve the cart item based on the product_name and user
#     try:
#         cart_item = Cart.objects.get(product__name=product_name, user=request.user)
#     except Cart.DoesNotExist:
#         # Handle case when cart item is not found
#         return redirect('cart')  # Redirect to the cart page or any other suitable page
#
#     # Perform any additional checks or logic before canceling the order
#
#     # Delete the cart item
#     cart_item.delete()
#
#     # Redirect back to the cart page or any other suitable page
#     return redirect('cart')

# def cancel_order(request, product_name):
#     # Retrieve the user's cart
#     cart_item = Cart.objects.filter(user=request.user, product__name=product_name).first()
#
#     if cart:
#         # Delete the cart item
#         cart_item.delete()
#
#     # Redirect back to the cart page or any other suitable page
#     return redirect('cart')


# def cancel_order(request, product_name):
#     # Retrieve the user's cart items for the specified product
#     cart_items = Cart.objects.filter(user=request.user, product__name=product_name)
#
#     # Get the total quantity to be removed
#     total_quantity = cart_items.aggregate(total_quantity=Sum('quantity'))['total_quantity']
#
#     if cart_items.exists():
#         # Delete the cart items
#         cart_items.delete()
#
#         # Update the remaining quantities in the cart
#         Cart.objects.filter(user=request.user).exclude(product__name=product_name).update(quantity=F('quantity') - total_quantity)
#
#     # Redirect back to the cart page or any other suitable page
#     return redirect('cart')

# def cancel_order(request, product_name):
#     # Retrieve the user's cart items for the specified product
#     cart_items = Cart.objects.filter(user=request.user, product__name=product_name)
#
#     if cart_items.exists():
#         # Delete the cart items
#         cart_items.delete()
#
#     # Redirect back to the cart page or any other suitable page
#     return redirect('cart')

# def cancel_order(request):
#     if request.method == 'POST':
#         item_id = request.POST.get('item_id')
#         if item_id:
#             # Retrieve the user's cart item for the specified product
#             cart_item = Cart.objects.filter(user=request.user, product__name=item_id).first()
#
#             if cart_item:
#                 # Delete the cart item
#                 cart_item.delete()
#
#     # Redirect back to the cart page or any other suitable page
#     return redirect('cart')

# def cancel_order(request):
#     if request.method == 'POST':
#         product_name = request.POST.get('product_name')
#         if product_name:
#             # Retrieve the user's cart item for the specified product
#             cart_item = Cart.objects.filter(user=request.user, product__name=product_name).first()
#
#             if cart_item:
#                 # Delete the cart item
#                 cart_item.delete()
#
#     # Redirect back to the cart page or any other suitable page
#     return redirect('cart')


def cancel_order(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        if product_name:
            # Retrieve the user's cart items for the specified product
            cart_items = Cart.objects.filter(user=request.user, product__name=product_name)

            if cart_items.exists():
                # Delete all the cart items for the product
                cart_items.delete()

    # Redirect back to the cart page or any other suitable page
    return redirect('cart')


# def cancel_order(request):
#     if request.method == 'POST':
#         product_name = request.POST.get('product_name')
#         if product_name:
#             # Delete the order associated with the product
#             Order.objects.filter(product__name=product_name).delete()
#
#             # Return a JSON response indicating the success of the operation
#             return JsonResponse({'success': True})
#
#     # Return a JSON response indicating the failure of the operation
#     return JsonResponse({'success': False})


def finish(request):
    return render(request, "finish.html")


def payment(request):
    if request.method == "POST":
        form_data = PaymentForm(request.POST, request.FILES)
        if form_data.is_valid():
            post = form_data.save(commit=False)
            # post.image = form_data.cleaned_data['image']
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
