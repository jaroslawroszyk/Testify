from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=100)

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class TestTaker(models.Model):
    name = models.CharField(max_length=100)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)