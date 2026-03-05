
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import CustomUserRegistrationForm
from .forms import ShowForm
from .models import Shows

def home(request):
    from .models import Shows
    print(Shows.objects.all())
    shows = Shows.objects.all()
    return render(request, 'home.html', {'shows': shows})

def signup(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()

    return render(request, 'signup.html', {'form': form})

def login(request):
    return render(request, 'login.html')

@login_required
def upload(request):
    if request.method == 'POST':
        form = ShowForm(request.POST, request.FILES)
        if form.is_valid():
            show = form.save(commit=False)
            show.user = request.user
            show.save()
            return redirect('home')
    else:
        form = ShowForm()

    return render(request, 'upload.html', {'form': form})

@login_required
def update_show(request, id):
    show = get_object_or_404(Shows, id=id)

    # Only uploader can update
    if show.user != request.user:
        return HttpResponseForbidden("You cannot edit this.")

    if request.method == 'POST':
        form = ShowForm(request.POST, request.FILES, instance=show)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ShowForm(instance=show)

    return render(request, 'update.html', {'form': form})

@login_required
def delete_show(request, id):
    shows = get_object_or_404(Shows, id=id)

    # Only uploader can delete
    if shows.user != request.user:
        return HttpResponseForbidden("You cannot delete this.")

    shows.delete()
    return redirect('home')

@login_required
def my_shows(request):
    shows = Shows.objects.filter(user=request.user)
    return render(request, 'my_shows.html', {'shows': shows})