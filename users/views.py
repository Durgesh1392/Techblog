from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# Create your views here.
def register(request):
   # print("hi")
    if request.method == 'POST':
        #print("post")
        form = UserRegisterForm(request.POST)
       # print(form)
        if form.is_valid():
            #print(form )
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account is created. You can login now using your credentials')
            return redirect('login')
    else:
        print("else")
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
