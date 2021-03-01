from django.db import models
from accounts.models import CustomUser


class Question(models.Model):
    content = models.TextField("content of the question")
    sender = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="questions_sender",
        related_query_name="question",
    )
    adressee = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="questions_adressee",
        related_query_name="question",
    )
    anonymous = models.BooleanField("if the question is send as anonymous")

    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("question_detail", args=[str(self.id)])


class Answer(models.Model):
    content = models.TextField("content of the answer")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("answer_detail", args=[str(self.id)])


class Like(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "like"
        verbose_name_plural = "likes"

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("like_detail", args=[str(self.id)])
