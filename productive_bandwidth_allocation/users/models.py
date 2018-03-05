import re
from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=False, max_length=255)
    birth_date = models.DateField(_('Birth date of user'), default=now())
    department = models.CharField(_('Department of User'), blank=False, max_length=255)
    is_student = models.BooleanField(_('Student or not'), blank=False, default=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def is_user_student(self):
        student_email = r'\w+@(student).mes.ac.in'
        staff_email = r'\w+@(staff).mes.ac.in'
        if re.match(staff_email, self.email):
            return True
        else:
            return False
