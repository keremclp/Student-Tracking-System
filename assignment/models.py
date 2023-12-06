# quiz/models.py
from django.db import models
from student.models import StudentProfile
from teacher.models import TeacherProfile


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text


class Result(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self) -> str:
        return str(self.score)
