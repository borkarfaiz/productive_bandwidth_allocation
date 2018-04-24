import re
from datetime import timedelta, date

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from .users_classification import predict_group
from .website_classifier import classify_url

DEFAULT_AGE = 18


@python_2_unicode_compatible
class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=False, max_length=255)
    birth_date = models.DateField(_('Birth date of user'), default=now() - timedelta(days=DEFAULT_AGE * 365 - 1))
    department = models.CharField(_('Department of User'), blank=False, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def is_student(self):
        student_email = r'\w+@(student).mes.ac.in'
        staff_email = r'\w+@.mes.ac.in'
        if re.match(student_email, self.email):
            return True
        else:
            return False

    def user_class(self):
        group = int(predict_group(department_name=self.department, is_student=self.is_student(), age=self.age()))
        return group


class SiteUrl(models.Model):
    user = models.ForeignKey(User,
                             verbose_name=_('user'),
                             on_delete=models.CASCADE)
    url = models.URLField(verbose_name=_('site_url'),
                          help_text='Enter the url of a website you want to visit')

    def domain_name(self):
        start = self.url.index('//') + 2
        end = self.url.index('/', start)
        return self.url[start:end]

    def __str__(self):
        return f'{self.user.user_class()} grp visited {self.domain_name()}'


class Usage(models.Model):
    group = models.PositiveIntegerField(unique=True,
                                        verbose_name=_('group number'),
                                        help_text='Group of the user')
    education = models.PositiveIntegerField(default=0)
    education_related = models.PositiveIntegerField(default=0)
    other = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Group Number:{self.group} Education:{self.education} ' \
               f'Related Education:{self.education_related} Other:{self.other}'

    def productive_percentage(self):
        total_no_of_visited_site = self.education + self.education_related + self.other
        productive = self.education * 1 + self.education_related * 0.7 + self.other * 0.2
        try:
            productive_percentage = str(round((productive / total_no_of_visited_site) * 100, 2)) + '%'
        except ZeroDivisionError:
            productive_percentage = '0%'
        return productive_percentage
