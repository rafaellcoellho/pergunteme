from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.contrib import messages

from .forms import CustomUserCreationForm
from .models import CustomUser

from questions.models import Answer, Like
from questions.forms import LikeForm, QuestionForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ExploreView(ListView):
    template_name = "account/explore.html"

    def get(self, request):
        my_user_id = request.user.id
        all_users = CustomUser.objects.exclude(id=my_user_id).exclude(is_superuser=True)
        return render(request, self.template_name, {"all_users": all_users})

    def post(self, request):
        order = request.POST.get("order")
        my_user_id = request.user.id

        if order == "desc":
            all_users = CustomUser.objects.exclude(id=my_user_id).exclude(is_superuser=True).order_by('-username')
        else:
            all_users = CustomUser.objects.exclude(id=my_user_id).exclude(is_superuser=True).order_by('username')

        return render(request, self.template_name, {"all_users": all_users})


class ProfileView(CreateView):
    template_name = "account/profile.html"

    def get(self, request, user_username):
        my_user_id = request.user.id
        user = CustomUser.objects.get(username=user_username)
        answers_queryset = Answer.objects.select_related("question").filter(question__adressee=user.id)

        def process_information(answer):
            return {
                "form": LikeForm(initial={"user": my_user_id, "answer": answer.id}),
                "answer": answer,
                "number_of_likes": answer.like_set.count(),
                "current_user_like": answer.like_set.filter(user=my_user_id).exists()
            }

        infos = list(map(process_information, answers_queryset))

        form = QuestionForm(initial={"sender": my_user_id, "adressee": user.id})
        context = {
            "form": form,
            "profile": user,
            "infos": infos,
            "number_of_answered_questions": len(infos),
        }
        return render(request, self.template_name, context)

    def post(self, request, user_username):
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Question added! When the user responds he will appear here on his profile!",
            )
            return redirect("profile", user_username=user_username)

        context = {"form": form}
        return render(request, self.template_name, context)


class HomeView(CreateView):
    template_name = "home.html"

    def get(self, request):
        my_user_id = request.user.id
        answers_queryset = Answer.objects.select_related("question").filter(
            question__adressee=my_user_id
        )


        def process_information(answer):
            return {
                "form": LikeForm(initial={"user": my_user_id, "answer": answer.id}),
                "answer": answer,
                "number_of_likes": answer.like_set.count(),
                "current_user_like": answer.like_set.filter(user=my_user_id).exists()
            }

        infos = list(map(process_information, answers_queryset))

        context = {"infos_answers": infos, "number_of_answered_questions": len(infos)}
        return render(request, self.template_name, context)

    def post(self, request):
        form = LikeForm(request.POST)
        user = form.data["user"]
        answer = form.data["answer"]

        like_exists = False
        try:
            like = Like.objects.get(user=user, answer=answer)
            like_exists = True
        except Like.DoesNotExist:
            like_exists = False

        if like_exists:
            like.delete()
            messages.error(
                request,
                "Don't you like that answer anymore? What a pity",
            )
            return redirect("home")
        elif form.is_valid():
            form.save()
            messages.success(
                request,
                "You liked this answer!",
            )
            return redirect("home")

        context = {"form": form}
        return render(request, self.template_name, context)
