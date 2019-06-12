from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


def validate_file_size(value):
    filesize = value.size
    max_file_size = 10485760  # 10MB
    if filesize > max_file_size:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value


class PhoneNumberValidator(RegexValidator):
    regex = r'^\+?1?\d{9,15}$',
    message = _("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
