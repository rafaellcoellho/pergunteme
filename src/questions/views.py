from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib import messages

from .models import Question
from .forms import AnswerForm


class ReceivedQuestionsView(CreateView):
    template_name = "question/received_questions.html"

    def get(self, request):
        my_user_id = request.user.id
        unanswered_questions_queryset = Question.objects.filter(
            answer__id__isnull=True, adressee__id=my_user_id
        )

        def process_information(question):
            return {
                "form": AnswerForm(initial={"question": question.id}),
                "question": question,
            }

        infos = map(process_information, unanswered_questions_queryset)

        context = {"infos_unanswered_questions": infos}
        return render(request, self.template_name, context)

    def post(self, request):
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Answer added!")
            return redirect("received_questions")

        context = {"form": form}
        return render(request, self.template_name, context)
