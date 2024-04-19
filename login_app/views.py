from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from forms. models import UserProfile, LoginTable
from forms. models import Book

# Create your views here.


def userRegistration(request):
    login_table = LoginTable()
    userprofile = UserProfile()
    if request.method == 'POST':
        userprofile.username = request.POST['username']
        userprofile.password = request.POST['password']
        userprofile.password2 = request.POST['password1']

        login_table.username = request.POST['username']
        login_table.password = request.POST['password']
        login_table.password2 = request.POST['password1']
        login_table.type = 'user'

        if request.POST['password'] == request.POST['password']:
            userprofile.save()
            login_table.save()
            messages.info(request, 'Registration success')
            return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

    return render(request, 'login/register.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = LoginTable.objects.filter(username=username, password=password, type='user').exists()
        try:

            if user is not None:
                user_details = LoginTable.objects.get(username=username, password=password)
                user_name = user_details.username
                type = user_details.type
                if type == 'user':
                    request.session['username']= user_name
                    return redirect('user_view')
                elif type == 'admin':
                    request.session['username']= user_name
                    return redirect('admin_view')
            else:
                messages.error(request, 'Invalid username or password')
        except:
            messages.error(request, 'invalid role')
    return render(request, 'login/login.html')


def admin_view(request):
    user_name = request.session['username']
# return render(request, 'listbook.html', {'user_name': user_name})
    return redirect('lists')

def user_view(request):
    user_name = request.session['username']
# return render(request, 'user/user_listBook.html', {'user_name': user_name})
    return redirect('user_lists')


def logout_view(request):
    logout(request)
    return redirect('login')




