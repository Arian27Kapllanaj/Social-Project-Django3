from re import template
from django.http import JsonResponse
from django.shortcuts import render
from .models import Profile
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required

# Create your views here.

#@login_required
def profile_test_view(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'profiles/test_profile.html', {'profile':profile})

class MyProfileView(TemplateView):
    template_name = 'profile/my_profile.html'

class MyProfileData(View):
    def get(self, *args, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        qs = profile.get_proposals_for_following()
        profiles_to_follow_list = []
        for user in qs:
            p = Profile.objects.filter(user_username=user.username)
            profile_item = {
                'id': p.id,
                'user': p.user.username,
                'avatar': p.avatar.url,
            }
            profiles_to_follow_list.append(profile_item)
        return JsonResponse({'pf_data': profiles_to_follow_list})