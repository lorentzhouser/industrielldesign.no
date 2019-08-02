from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from authentication.forms import RegisterForm
from authentication.models import Profile
from books.models import Book


def get_user(request):
    return Profile.objects.get(pk=request.user.pk)


def my_profile(request):
    user = get_user(request)
    form = RegisterForm(instance=user)
    my_books = Book.objects.filter(
        seller=Profile.objects.get(pk=request.user.pk))
    context = {
        'user': user,
        'form': form,
        'my_books': my_books
    }

    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return render(request, 'profilepage/profilepage.html', context)


def change_password(request):
    user = get_user(request)
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'profilepage/change-password.html', {})
        else:
            password = request.POST['password']
            user.set_password(password)
            user.save()
            login(request, authenticate(
                request, email=user.email, password=user.password))
            redirect('my_profile')
    else:
        redirect('login')


def change_info(request):
    user = get_user(request)
    form = RegisterForm(request.POST, instance=user)
    user.allergies = form['allergies'].value()
    user.is_komite = form['is_komite'].value()
    user.graduation_year = form['graduation_year'].value()
    user.save()


def delete_book(request):
    book_pk = request.POST.get('book_pk')
    Book.objects.filter(pk=book_pk).delete()
    return HttpResponse('deleted')
