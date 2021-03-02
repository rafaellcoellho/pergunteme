from django.forms import ModelForm, Textarea, HiddenInput
from .models import Answer, Like


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
