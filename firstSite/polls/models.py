from django.db import models

# Create your models here.


class Question(models.Model):
    ques_text = models.CharField(max_length=180)
    ques_date = models.DateTimeField()
    def __str__(self):
        return self.ques_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=20)
    agreeCount = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text