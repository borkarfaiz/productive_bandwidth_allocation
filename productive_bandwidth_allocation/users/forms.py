from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.timezone import now

from .models import User

DEPARTMENTS = [
    ('comps', 'Computer'),
    ('extc', 'Electronics'),
    ('civil', 'Civil'),
    ('mech', 'Mechanical'),
]


class MySignupForm(forms.Form):
    birth_date = forms.DateField(widget=SelectDateWidget(years=(range(1980, now().year))))
    department = forms.CharField(label='Select Your Branch', widget=forms.Select(choices=DEPARTMENTS))

    def signup(self, request, user):
        # user.first_name = self.cleaned_data['first_name']
        # user.last_name = self.cleaned_data['last_name']
        user.birth_date = self.cleaned_data["birth_date"]
        user.department = self.cleaned_data['department']
        user.is_student = User.is_user_student(user)
        user.save()

