
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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