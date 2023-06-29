from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files import images
from django.template.context_processors import static

from .models import Product, Category, UserAuthentication, Order, AdminProfile


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # for field in self.visible_fields():
        #     field.field.widget.attrs["class"] = "form-control"
        # field.field.widget.attrs["class"] = "bg-transparent rounded-0"
        # field.field.widget.attrs["style"] = "border-color: darkorchid; height:70px; width: 500px; " \
        #                                     "background-image: {% static 'images/slika.png' %}; " \
        #                                     "background-repeat: no-repeat; background-position: right; " \
        #                                     "background-size: 70px "

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'Name: '})
    )
    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=forms.Select(
    #         attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'Category: '})
    # )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Category',
        widget=forms.Select(attrs={'class': 'form-control input-with-background rounded-0'})
    )
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'Image: '})
    )
    in_Stocked = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'In Stock: '})
    )
    price = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'Price: '})
    )
    ingredients = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'Ingredients: '})
    )

    class Meta:
        model = Product
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        # for field in self.visible_fields():
        #     field.field.widget.attrs["class"] = "form-control"
        # field.field.widget.attrs["class"] = "bg-transparent rounded-0"
        # field.field.widget.attrs["style"] = "border-color: darkorchid; height:70px; width: 500px; " \
        #                                     "background-image: {% static 'images/slika.png' %}; " \
        #                                     "background-repeat: no-repeat; background-position: right; " \
        #                                     "background-size: 70px "

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'FIRST NAME'})
    )

    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'Surname'})
    )

    street = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'Street'})
    )

    card_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'Card_Number'})
    )

    state = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'State'})
    )

    city = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'City'})
    )

    class Meta:
        model = Order
        fields = '__all__'


# <input type="text" class="bg-transparent form-control rounded-0" style="border-color: " \
#         "darkorchid; height: 70px; width: 500px; background-image: url('Screenshot 2023-06-21 " \
#         "213504.png'); background-repeat: no-repeat; background-position: right; background-size: 70px"
# placeholder="NAME">

# class UserForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(UserForm, self).__init__(*args, **kwargs)
#
#     name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'NAME'})
#     )
#
#     surname = forms.CharField(
#         widget=forms.TextInput(
#             attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'SURNAME'})
#     )
#
#     user = forms.CharField(
#         widget=forms.TextInput(
#             attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'NAME'})
#     )
#
#     name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'NAME'})
#     )
#
#     class Meta:
#         model = UserAuthentication
#         fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control input-with-background rounded-0'})


class UserAuthenticationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control input-with-background rounded-0', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control input-with-background rounded-0', 'placeholder': 'Password1'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control input-with-background rounded-0', 'placeholder': 'Password2'})

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'Name'})
    )
    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'Surname'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'surname']


class AdminUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AdminUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control input-with-background rounded-0'})


class AdminAuthenticationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(AdminAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control input-with-background rounded-0', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control input-with-background rounded-0', 'placeholder': 'Password1'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control input-with-background rounded-0', 'placeholder': 'Password2'})

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'Name'})
    )
    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-with-background rounded-0', 'placeholder': 'Surname'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'surname']
