# quiz/models.py
from django.db import models
from django.urls import reverse
from config.validators import validate_file_extension
from student.models import StudentProfile
from teacher.models import TeacherProfile

# ASSIGNMENT VIA QUIZ
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    # deadline with a default value 
    deadline = models.DateTimeField(blank=True, null=True)    
    def __str__(self):
        return self.title

    def get_solve_quiz_url(self):
        return reverse(
            "assignment:solve_quiz",
            kwargs={
                "quiz_id": self.pk,
            },
        )
    
    class Meta:
        ordering = ('deadline',)

class Question(models.Model):
    text = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    # added a new field to the Question model which is realted o score of the question
    score = models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='choice_set')
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


class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user_answers')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='user_answers')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        unique_together = ('question', 'student')

    def __str__(self) -> str:
        return self.choice.text

class SolvedQuiz(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_solved = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.student} solved {self.quiz} with score {self.score}"

# ASSIGNMENT VIA UPLOADING FILE
class AssignmentFile(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    description = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('deadline',)

class UploadedSolution(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    assignment = models.ForeignKey(AssignmentFile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)