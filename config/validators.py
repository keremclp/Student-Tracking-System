import os
from django.forms import ValidationError, forms

from config.settings import ALLOWED_FILE_TYPES

def min_lenght_7(value):
    if len(value) < 7 :
        raise forms.ValidationError('Title must be greater than 3 characters')
    

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # Get file extension
    if not ext.lower() in ALLOWED_FILE_TYPES:
        raise ValidationError('Unsupported file extension.')
