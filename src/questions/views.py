from django.shortcuts import render
from django.views.generic import DetailView

from .models import Question


class ReceivedQuestionsView(DetailView):
    template_name = "question/received_questions.html"

    def get(self, request):
        my_user_id = request.user.id
        unanswered_questions = Question.objects.filter(answer__id__isnull=True, id=my_user_id)
        return render(request, self.template_name, {'unanswered_questions': unanswered_questions})
