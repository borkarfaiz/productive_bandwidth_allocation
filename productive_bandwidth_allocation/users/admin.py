from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .models import User, SiteUrl, Usage, UserGroup


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
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    fieldsets = (
                    ('User Profile', {'fields': ('name', 'birth_date', 'department', 'email')}),
                ) + AuthUserAdmin.fieldsets
    list_display = ('username', 'name', 'email', 'is_student', 'department', 'age', 'user_class', 'last_login')
    search_fields = ['name', 'department']


@admin.register(SiteUrl)
class AdminSiteUrl(admin.ModelAdmin):
    list_display = ('user', 'domain_name', 'url', 'user_group')

    def user_group(self, obj):
        return obj.user.user_class()

    user_group.ordering = 'user__user_class'


@admin.register(Usage)
class AdminUsage(admin.ModelAdmin):
    list_display = ('group', 'education', 'education_related', 'other')

    def has_add_permission(self, request):
        return False


@admin.register(UserGroup)
class AdminUserGroup(admin.ModelAdmin):
    list_display = ('group',)


admin.site.site_header = 'Productive Bandwidth Allocation'

# default admin site Group has been removed
admin.site.unregister(Group)
