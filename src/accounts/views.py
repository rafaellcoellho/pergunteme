from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.db.models import Q

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class ExploreView(CreateView):
    template_name = "account/explore.html"

    def get(self, request):
        my_user_id = request.user.id
        all_users = CustomUser.objects.exclude(id=my_user_id).exclude(is_superuser=True)
        return render(request, self.template_name, {'all_users': all_users})


class ProfileView(CreateView):
    template_name = "account/profile.html"

    def get(self, request, user_username):
        user = CustomUser.objects.get(username=user_username)
        return render(request, self.template_name, {'profile': user})
