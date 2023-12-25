from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from assignment.models import Quiz
from student.models import StudentProfile


def validate_quiz_id(quiz_id):
    if not Quiz.objects.filter(id=quiz_id).exists():
        raise ValidationError(
            _('%(quiz_id)s does not exist'),
            params={'quiz_id': quiz_id},
        )


def validate_student_slug(student_slug):
    if not StudentProfile.objects.filter(slug=student_slug).exists():
        raise ValidationError(
            _('%(student_slug)s does not exist'),
            params={'student_slug': student_slug},
        )
