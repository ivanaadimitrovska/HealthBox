"""
URL configuration for probnaProekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.storage import staticfiles_storage

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from app.views import addProduct, addPr, customer, glavna, cokoladni, add_to_cart, cart, ingredients, kosnicka, \
    cancel_order, payment, finish, adminLogin, index, cotton, chewing, gummy, hard, lollipop, gummyIngre, chewingIngre, \
    chocoIngre, cottonIngre, hardIngre, lollipopIngre, blog, aboutUs, contact, login_view, login_viewAdmin, editProduct, \
    delete_product

app_name = 'app'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('glavna1/', glavna, name="anything"),
                  path('index/', index, name="index"),
                  path('addProduct/', addProduct, name="addProduct"),
                  path('product/<int:product_id>/', addPr, name='addPr'),
                  path('product/edit/<int:product_id>/', editProduct, name='editProduct'),
                  path('product/<int:product_id>/addProduct/', addProduct, name='addProduct'),
                  path('product/delete/<int:product_id>/', delete_product, name='delete_product'),
                  path('customer/', customer, name="customer"),
                  path('adminLogin/', adminLogin, name="adminLogin"),
                  path('glavna/', glavna, name="glavna"),
                  path('cokoladni/', cokoladni, name="cokoladni"),
                  path('add_to_cart/', add_to_cart, name='add_to_cart'),
                  path('cart/', cart, name='cart'),
                  path('cokoladni/cart.html', kosnicka, name='kosnicka'),
                  path('index/adminCustomer.html', login_view, name="login"),
                  path('index/adminLogin.html', login_viewAdmin, name='login_viewAdmin'),
                  path('index/register.html', customer, name="customer"),
                  path('index/registerAdmin.html', adminLogin, name="adminLogin"),
                  path('glavna/glavnaStrana.html', glavna, name="glavna"),
                  path('cokoladni/cotton.html', cotton, name="cotton"),
                  path('cokoladni/gummy.html', gummy, name="cotton"),
                  path('cokoladni/hard.html', hard, name="cotton"),
                  path('cokoladni/lollipop.html', lollipop, name="cotton"),
                  path('cokoladni/chewing.html', chewing, name="cotton"),
                  path('cokoladni/cokoladni.html', cokoladni, name="cotton"),
                  path('cokoladni/allIngredientsGummy.html', gummyIngre, name="gummyIngre"),
                  path('cokoladni/allIngredientsChewing.html', chewingIngre, name="gummyIngre"),
                  path('cokoladni/allIngredientsChocolate.html', chocoIngre, name="gummyIngre"),
                  path('cokoladni/allIngredientsCotton.html', cottonIngre, name="gummyIngre"),
                  path('cokoladni/allIngredientsHard.html', hardIngre, name="gummyIngre"),
                  path('cokoladni/allIngredientsLollipop.html', lollipopIngre, name="gummyIngre"),

                  path('cokoladni/cokoladni.html', cokoladni, name='cokoladni'),
                  path('cotton/cotton.html', cotton, name='cotton'),
                  path('chewing/chewing.html', chewing, name='chewing'),
                  path('gummy/gummy.html', gummy, name='gummy'),
                  path('hard/hard.html', hard, name='hard'),
                  path('lollipop/lollipop.html', lollipop, name='lollipop'),
                  path('glavna/cokoladni.html', cokoladni, name='cokoladni'),
                  path('glavna/cotton.html', cotton, name='cotton'),
                  path('glavna/chewing.html', chewing, name='chewing'),
                  path('glavna/gummy.html', gummy, name='gummy'),
                  path('glavna/hard.html', hard, name='hard'),
                  path('glavna/lollipop.html', lollipop, name='lollipop'),
                  path('glavna/allIngredientsGummy.html', gummyIngre, name="gummyIngre"),
                  path('glavna/allIngredientsChewing.html', chewingIngre, name="gummyIngre"),
                  path('glavna/allIngredientsChocolate.html', chocoIngre, name="gummyIngre"),
                  path('glavna/allIngredientsCotton.html', cottonIngre, name="gummyIngre"),
                  path('glavna/allIngredientsHard.html', hardIngre, name="gummyIngre"),
                  path('glavna/allIngredientsLollipop.html', lollipopIngre, name="gummyIngre"),
                  path('cokoladni/allIngredientsChocolate.html', chocoIngre, name="gummyIngre"),
                  path('glavna/cart.html', kosnicka, name="kosnicka"),
                  path('glavna/payment.html', payment, name="payment"),
                  path('glavna/ourBlog.html', blog, name="blog"),
                  path('ourBlog.html', blog, name="blog"),
                  path('ourBlog/', blog, name="blog"),
                  path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
                  path('cokoladni/ourBlog.html', blog, name="blog"),
                  path('cokoladni/aboutUs.html', aboutUs, name="aboutUs"),
                  path('cokoladni/contact.html', contact, name="contact"),
                  path('glavna/aboutUs.html', aboutUs, name="aboutUs"),
                  path('glavna/contact.html', contact, name="contact"),
                  path('cokoladni/glavnaStrana.html', glavna, name='glavna'),
                  path('kosnicka/', kosnicka, name='kosnicka'),
                  path('cancel_order/', cancel_order, name='cancel_order'),
                  path('payment/', payment, name="payment"),
                  path('kosnicka/payment.html', payment, name="payment"),
                  path('finish/', finish, name="finish"),
                  path('cokoladni/payment.html', payment, name="payment")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
