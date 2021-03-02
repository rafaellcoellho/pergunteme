from django.forms import ModelForm, Textarea, HiddenInput
from .models import Answer, Like, Question


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ["content", "question"]
        labels = {
            "content": "Answer the question",
        }
        widgets = {
            "content": Textarea(attrs={"rows": 3}),
            "question": HiddenInput(),
        }


class LikeForm(ModelForm):
    class Meta:
        model = Like
        fields = ["user", "answer"]
        widgets = {
            "user": HiddenInput(),
            "answer": HiddenInput(),
        }


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["content", "anonymous", "sender", "adressee"]
        labels = {"content": "Send a question", "anonymous": "Send anonymously"}
        widgets = {
            "content": Textarea(attrs={"rows": 3}),
            "sender": HiddenInput(),
            "adressee": HiddenInput(),
        }
