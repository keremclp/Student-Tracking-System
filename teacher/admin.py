from django.contrib import admin
from teacher.models import TeacherProfile

# Register your models here.


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    # list display
    list_display = (
        'user_username',
        'classroom',
    )

    def user_username(self, obj):
        return obj.user.first_name + " " + obj.user.last_name
