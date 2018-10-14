from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.error(request, 'The Username already exists')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'The Email already exists')
          return redirect('register')
        else:
          # Validation passed
          user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')


def login(request):
  if request.method == 'POST':
    # Login user logic
    return
  else:
    return render(request, 'accounts/login.html')


def logout(request):
  return redirect('index')


def dashboard(request):
  return render(request, 'accounts/dashboard.html')
