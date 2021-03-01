from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ReceivedQuestionsView

urlpatterns = [
    path("received_questions/", login_required(ReceivedQuestionsView.as_view()), name="received_questions"),
]