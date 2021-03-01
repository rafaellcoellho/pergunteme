from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import SignUpView, ExploreView, ProfileView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("explore/", login_required(ExploreView.as_view()), name="explore"),
    path("<str:user_username>/", login_required(ProfileView.as_view()), name="profile"),
]
