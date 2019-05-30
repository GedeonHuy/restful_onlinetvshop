from django.db import models
from django.utils.translation import gettext_lazy as _


class Brand(models.Model):
    title = models.CharField(_('Title'), max_length=30, blank=False)
    description = models.CharField(_('Description'), max_length=3000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
