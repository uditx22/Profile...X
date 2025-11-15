from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.

# Home view.
def home_view(request):
    return render(request, 'profile_app/home.html')


# Dashboard view.
@login_required
def dashboard_view(request):
    profiles = Profile.objects.filter(manager=request.user)
    # profiles = Profile.objects.all()
    context = {
        'profiles': profiles,
    }
    return render(request, 'profile_app/dashboard.html', context)


# Detail Profile view.
@login_required
def profile_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {
        'profile': profile,
    }
    return render(request, 'profile_app/profil.html', context)


# Create view.
@login_required
def create_view(request):
        
    if request.method != "POST":
        form = ProfileForm()
    else:
        form = ProfileForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            # new_profile = form.save(commit=False)
            # new_profile.manager = request.user
            # new_profile.save()
            return redirect("profile_app:dashboard")  
            
    context = {
        'form': form,
    }
    return render(request, 'profile_app/create.html', context)


# Update view.
@login_required
def update_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    
    if profile.manager != request.user:
        raise Http404
    
    if request.method != "POST":
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect("profile_app:dashboard")  
            
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile_app/update.html', context)


# Delete.
@login_required
def delete_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    
    if request.method == "POST":
        profile.delete()
        return redirect('profile_app:home')
    
        