from student.models import StudentProfile
from teacher.models import TeacherProfile

def profile_global(request):
    user = request.user
    print(user)
    # bring me profile 
    profile = StudentProfile.objects.get(user=user)
    return {'profile_global': profile}

def profile_image(request):
    user = request.user
    profile_image_path = 'default_image_path'
    profile_global = None
    
    if user.is_authenticated:
        if user.role == 'student':
            try:
                profile_student = StudentProfile.objects.get(user=user)
                profile_image_path = profile_student.user.profile_image.url
                profile_global = profile_student
            except StudentProfile.DoesNotExist:
                pass  # No need to change profile_image_path or profile_global
        elif user.role == 'teacher':
            try:
                profile_teacher = TeacherProfile.objects.get(user=user)
                profile_image_path = profile_teacher.user.profile_image.url
                profile_global = profile_teacher
            except TeacherProfile.DoesNotExist:
                pass  # No need to change profile_image_path or profile_global
        # elif user.role == 'parent':
        #     try:
        #         profile_parent = ParentProfile.objects.get(user=user)
        #         profile_image_path = profile_parent.user.profile_image.url
        #         profile_global = profile_parent
        #     except ParentProfile.DoesNotExist:
        #         pass  # No need to change profile_image_path or profile_global

    return {
        'profile_image': profile_image_path,
        'profile_global': profile_global
    }

def completion_percentage(request):
    user = request.user
    if user.is_authenticated:
        try:
            total_fields = 4
            completed_fields = 0 
            completion_percentage = 0 
            if user.role == 'student':
                profile = StudentProfile.objects.get(user=user)
                completed_fields = sum(
                    field is not None and field != ""
                    for field in [profile.birth_date, profile.bio, profile.phone_number, profile.address]
                )
            elif user.role == 'teacher':
                profile = TeacherProfile.objects.get(user=user)
                print('teacher--------------')
                completed_fields = sum(
                    field is not None and field != ""
                    for field in [profile.birth_date, profile.bio, profile.phone_number, profile.address, profile.experience, profile.salary]
                )
                print(completed_fields)
            # elif user.role == 'parent':
            #     completed_fields = sum(
            #         field is not None and field != ""
            #         for field in [profile.birth_date, profile.bio, profile.phone_number, profile.address, profile.job]
            #     )
            completion_percentage = (completed_fields / total_fields) * 100
            print('---------completion_percentage')
            print(completion_percentage)   
        except StudentProfile.DoesNotExist:
            completion_percentage = 0  # No profile, so completion is 0%
    else:
        completion_percentage = 0  # User is not authenticated, so completion is 0%
    
    return {'completion_percentage': completion_percentage}

