import webbrowser

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.views.generic.edit import CreateView

from .models import User, SiteUrl, Usage
from .website_classifier import classify_url


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class BrowseView(LoginRequiredMixin, CreateView):
    template_name = "users/browse.html"
    model = SiteUrl
    fields = ['url']
    context_object_name = 'latest_url_list'

    """Save the input with Foreign Key"""

    def save_group_data(self):
        user_group = self.request.user.user_class()
        print(user_group)
        group, created = Usage.objects.get_or_create(group=user_group)
        url = self.request.user.siteurl_set.last(). \
            url.encode()
        print(type(url))
        category_label = classify_url(url=url)
        if category_label == 'Education':
            group.education += 1
        elif category_label == 'Education Related':
            group.education_related += 1
        else:
            group.other += 1
        group.save()

    def open_new_web_page(self):
        last_site = self.request.user.siteurl_set.last()
        webbrowser.open(url=last_site.url)

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.save_group_data()
        # self.open_new_web_page()
        messages.success(self.request, 'You have Successfully visited the site')
        return super(BrowseView, self).form_valid(form)

    def get_success_url(self):
        return reverse('users:browse', )

    def get_context_data(self, **kwargs):
        return dict(
            super(BrowseView, self).get_context_data(**kwargs),
            last_url=self.request.user.siteurl_set.all()[:10]
        )
