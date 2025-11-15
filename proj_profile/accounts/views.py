from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register_view(request):
    
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            form.save()
        return redirect("accounts:login")         
    
    context = {
        'form': form,
    }
    return render(request, "registration/register.html", context)