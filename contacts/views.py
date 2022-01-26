from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect


# from django.views.generic import ListView, CreateView
from django.template import context
from django.template import defaulttags
from  django.db.models import *
from .forms import *
from django.forms import ModelForm
#
# class DateTimeInput(forms.DateTimeInput):
#     input_type: datetime

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have been Logged In !'))
            return redirect('homepage')
        else:
            messages.success(request, ('Error you can try again !'))
            return redirect('login')
    else:
        return render(request, 'account/login.html', {})


def logout_user(request):
     logout(request)
     messages.success(request, ('You Have Been Logged out...'))
     return redirect('login')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('You Have Registered now...'))
            return redirect('homepage')
    else:
        form = SignUpForm(request.POST)
    context = {'form': form}
    return render(request, 'account/register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You Have Edited Your Profiel...'))
            return redirect('homepage')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'account/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,('You Have Edited Your Password...'))
            return redirect('account/homepage.html')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}

    return render(request, 'account/change_password.html', context)


# ===========================
#      VIEWS KALALISO
#          START
# ===========================
# def CreatePostView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'kalaliso/post.html'
#     # success_url = reverse_lazy ('kalaliso/homepage.html')
#     return render(CreateView, 'kalaliso/post.html')
#
# def HomePageView(ListView):
#     qp = Post.objects.all()
#     model = Post
#     context = { 'homepage': qp}
#     # template_name =  'kalaliso/homepage.html'
#     return render(ListView, 'kalaliso/homepage.html', context)

#     global image
#     if request.method == "POST":
#         form=PostForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             obj=form.instance
#             return render(request,'kalaliso/homepage.html', {"obj":obj})
#     else:
#        form=PostForm()
#        image=Post.objects.all()
#     return render(request, 'kalaliso/homepage.html', {"image":image, "form":form})


def homepage(request,):
    p = Person.objects.count()
    o = Order.objects.count()
    context = {'p': p, 'o': o}
    return render(request, 'kalaliso/homepage.html', context)


def vuesimg(request,):
    images = Image.objects.all().order_by('Date')
    # images = Product_image.objects.all()
    context = {'images':images}
    # return HttpResponseRedirect(reverse('kalaliso/detail_image.html', args=[pk]))
    return redirect('kalaliso/detail_image.html')
# return HttpResponseRedirect(reverse('app_blog:blog_detail',args=[pk]))


def image_upload_view(request, **kwargs):
    f = ImageForm
    if request.method == "POST" or None:
        f=ImageForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            img_obj=f.instance
            return render(request, 'kalaliso/index.html', {'form': f, 'img_obj': img_obj})
        else:
            f = ImageForm()
    return render(request, 'kalaliso/index.html', {'form': f})

def person(request,):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mesure'))
    else:
       form=PersonForm()

    return render(request, 'kalaliso/person.html', {'form': form,})


def person_detail(request, person_id):
    qs = Person.objects.all().order_by('-created_at')

    context = {'detail_person': qs,}

    return render(request, 'kalaliso/person_detail.html', context)


def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('order'))
    else:
       form = ProductForm()
    return render(request, 'kalaliso/product.html', {'form': form})


def product_detail(request, product_id):
    qs = Product.objects.all()
    context = {'product': qs,}

    return render(request, 'kalaliso/product_detail.html', context)


class DateTimePickerInput():
    pass


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('order_detail'))
    else:
        form=OrderForm()
    return render(request, 'kalaliso/order.html', {'form': form})


def order_items(request, order_id):
    qs = Order.objects.all().order_by()

    context = {'order_items': qs,}

    return render(request, 'kalaliso/order_items.html', context)


def order_items(request, ):
    if request.method == 'POST':
        form=Order_ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('order_items'))
    else:
        form = Order_ItemsForm()
    return render(request, 'kalaliso/order_items.html', {'form': form})

def orderdetail_detail(request, orderdetail_id):

    qs = Order_Items.objects.all().order_by(Order)
    context = {'orderdetail': qs, }

    return render(request, 'kalaliso/orderdetail_detail.html', context)

def mesure(request,):
    if request.method == 'POST':
        form = MesureForm(request.POST)
        if form.is_valid():
             form.save()
             return HttpResponseRedirect(reverse('Order'))
    else:
       form = MesureForm()
    return render(request, 'kalaliso/mesure.html', {'form': form})

# research for OVER STACK FLOW this Bug

# response = wrapped_callback(request, *callback_args, **callback_kwargs)

def mesure_detail(request, mesure_id):
    qs = Mesure.objects.all()

    context = {'detail_mesure': qs,}

    return render(request, 'kalaliso/mesure_detail.html', context)


def payment(request,):
        if request.method == 'POST':
          form = PaymentForm(request.POST)
          if form.is_valid():
              form.save()
              return HttpResponseRedirect(reverse('Order'))
        else:
            form = PaymentForm()
        return render(request, 'kalaliso/payment.html', {'form': form})

def payment_detail(request, payment_id):
    qs = Payment.objects.all()

    context = {'detail_payment': qs, }

    return render(request, 'kalaliso/payment_detail.html', context)



def maps(request, ):
    return render(request, 'maps/maps.html',)


def region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('cercle')
    else:
            form = RegionForm()
    return render(request, 'localisation/region.html', {'form': form})

def cercle(request):
    if request.method == 'POST':
        form = CercleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('commune')
    else:
        form = CercleForm()
    return render(request, 'localisation/cercle.html', {'form': form})

def commune(request):
    if request.method == 'POST':
        form = CommuneForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('village')
    else:
        form = CommuneForm()
    return render(request, 'localisation/commune.html', {'form': form})

def village(request):
    if request.method == 'POST':
        form = VillageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('village'))
    else:
        form = VillageForm()
    return render(request, 'localisation/village.html', {'form': form})


def profile(request):
    return render(request, 'kalaliso/profile.html', {})

# ===========================
#      VIEWS KALALISO
#          END
# ===========================

