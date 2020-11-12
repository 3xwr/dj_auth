from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import UserProfileForm
from .models import UserProfile


def index(request):
    if request.user.is_authenticated:
        return details(request)
    else:
        return render(request, 'soc_auth/index.html')


@login_required
def details(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except:
        profile=UserProfile.objects.create(user=request.user)

    form = UserProfileForm(instance=profile)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    return render(request, 'soc_auth/details.html', {'form': form, 'userprofile': profile})
