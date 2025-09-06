from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from listings.models import address
from .models import more_users
def login_user(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username, password=password1).exists():
            return redirect('signin')
        if password1 != password2:
            print('رمز ورود با هم همخوانی ندارد')
        else:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password2
            )
            user.save()


            return redirect('signin')
    return render(request, 'login.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            print("نام کاربری یا رمز عبوذ اشتباه است")
            return redirect('signin')
    return render(request, 'signin.html')

def forgot(request):
    if request.method == "POST":
        email = request.POST['email']
        user = User.objects.get(email=email)
        password = user.password
        print(f"رمز شما {password}")
        return redirect("signin")
    return render(request, 'forgot.html')

def profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        Address = address.objects.filter(user_id=request.user.id)
        more = more_users.objects.filter(user_id=request.user.id)
        if request.method == "POST":
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.username = request.POST['username']
            user.save()

        return render(request, 'profile.html',{'user': user, 'Address': Address, 'more': more})


    return render(request, 'profile.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def more_user(request):
    if request.method == "POST":
        user_name = request.POST['username']
        user_id = request.POST['id']
        image = request.POST['image']
        phone = request.POST['mobile']
        obj, created = more_users.objects.get_or_create(
            user_name=user_name,
            user_id=user_id,
            image=image,
            phone=phone
        )
        obj.save()
        return redirect('profile')



    return redirect('profile')