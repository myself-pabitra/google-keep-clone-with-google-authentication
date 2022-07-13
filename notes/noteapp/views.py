from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# ================================================== Home Page View =========================================
# @login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        my_task = keepnotes.objects.filter(user=user).order_by('time2')
        username = request.user
        context = {'notes': my_task, 'username': username}
        return render(request, 'home.html', context)
    else:
       return redirect(login_page)


# else:
#     return redirect(register_page)


# ================================================ Add Note View===================================================

def addnote(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        if request.method == 'POST':
            title1 = request.POST['title']
            note1 = request.POST['note']
            obj = keepnotes(title=title1, note=note1, user=user)
            # keepnotes.user = user
            obj.save()
            messages.success(request, 'Your Note added Successfully...!!!')
            return redirect(home)
        else:
            return render(request, 'addnote.html')

    else:
        return redirect(login_page)


# ========================================== Edit Note View =====================================================

def edit_note(request, pk):
    if request.user.is_authenticated:
        my_task = keepnotes.objects.get(id=pk)
        if request.method == 'POST':
            new_title = request.POST['title']
            new_note = request.POST['note']
            my_task.title = new_title
            my_task.note = new_note
            my_task.save()
            messages.success(request, 'Your note Updated successfully...!!!')
            return redirect(home)
        else:
            my_task = keepnotes.objects.get(id=pk)
            context = {'objects': my_task}
        return render(request, 'addnote.html', context)
    else:
        return redirect(login_page)


# ========================================== Delete Note View =====================================================

def delete_note(request, pk):
    if request.user.is_authenticated:
        my_note = keepnotes.objects.get(id=pk)
        if request.method == 'POST':
            my_note.delete()
            messages.success(request, 'your note is Deleted successfully..!!!')
            return redirect(home)
        else:
            my_note = keepnotes.objects.get(id=pk)
            context = {'del_note': my_note}
        return render(request, 'delete.html', context)
    else:
        return redirect(login_page)


# ========================================== Register View =====================================================

def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.success(request, 'This Username already Exists..!!')
                return redirect(register_page)
            elif User.objects.filter(email=email).exists():
                messages.success(request, 'This Email already Exists..!!')
                return redirect(register_page)

            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.info(request, 'User created Successfully..')
            return redirect(login_page)
        else:
            messages.info(request, 'Password Does not match')
            return redirect(register_page)
    return render(request, 'register.html')


# ==========================================Login View ========================================
def login_page(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(home)
            else:
                messages.info(request, 'Invalid Caredentials Given')
                return redirect(login_page)
        return render(request, 'accounts/login.html')
    else:
        return redirect(home)


# =================================================== Logout View   =========================================
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(login_page)
    else:
        return redirect(login_page)


# ==========================================================Search Note=================================================

def search_note(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "POST":
            sr_text = request.POST['search']
            if keepnotes.objects.filter(title__icontains=sr_text, user=user):
                sr_note = keepnotes.objects.filter(title__icontains=sr_text, user=user)
                context = {
                    'search_result': sr_note
                }
                return render(request, 'search_note.html', context)
            else:
                messages.error(request, 'No Search Results found !!')
                return render(request, 'home.html')
        return render(request, "home.html")
    else:
        return redirect(login_page)
