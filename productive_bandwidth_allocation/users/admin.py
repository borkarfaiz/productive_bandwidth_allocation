from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .models import User, SiteUrl


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    AuthUserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    fieldsets = (
                    ('User Profile', {'fields': ('name', 'birth_date', 'department')}),
                ) + AuthUserAdmin.fieldsets
    list_display = ('username', 'name', 'email', 'is_student', 'department', 'age', 'user_class')
    search_fields = ['name', 'department']


admin.site.site_header = 'Productive Bandwidth Allocation'
admin.site.register(SiteUrl)
admin.site.unregister(Group)
