from allauth.account.adapter import DefaultAccountAdapter
from django import forms
from django.conf import settings


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION', True)

    def clean_email(self, email):
        college_email = r'\w+@(student|staff).mes.ac.in'
        # if re.match(college_email, email):
        if email:
            return email
        else:
            raise forms.ValidationError("Email should be of college")
