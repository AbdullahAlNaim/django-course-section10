from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm

from .models import UserProfile

# Create your views here.

class UserProfileView(ListView):
    template_name = 'profiles/user_profiles.html'
    model = UserProfile
    context_object_name = 'pictures'

    # make sure to add MEDIA_URL = '/user-media/' to bottom settings file
    # in template can see like this:
    # <img src="{{ picture.image.url }}" alt="{{ picture.image }}">

class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/profiles'

# Use this only if not using CreateView
# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             'form': form
#         })
#
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#
#         if submitted_form.is_valid():
#            profile = UserProfile(image=request.FILES['user_image'])
#            profile.save()
#            return HttpResponseRedirect('/profiles')
#
#         return render(request, "profiles/create_profile.html", {
#             'form': submitted_form
#         })
