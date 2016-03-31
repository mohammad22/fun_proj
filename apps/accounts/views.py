from __future__ import absolute_import

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic

from braces import views


from .forms import RegistrationForm, LoginForm


class SignUpView(views.AnonymousRequiredMixin, views.FormValidMessageMixin,
                 generic.CreateView):
    form_class = RegistrationForm
    model = User
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

    #def form_valid(self, form):
    #    resp = super(SignUpView, self).form_valid(form)
    #    self.form_valid_message = "Thanks for signing up %s! Go ahead and login." % self.object.username
    #   return resp

    def get_form_valid_message(self):
        return u"Thanks for signing up %s. Go ahead and login." % self.object.username

class LoginView(views.AnonymousRequiredMixin, views.FormValidMessageMixin,
                generic.FormView):
    form_class = LoginForm
    #form_valid_message = "You're logged into your account."
    success_url = reverse_lazy('blog:postbriefs')
    template_name = 'accounts/login.html'
    print "went to login"
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)
    
    def get_form_valid_message(self):
        return u"You are logged in now %s." % self.request.user.username

class LogoutView(views.LoginRequiredMixin, views.MessageMixin,
                 generic.RedirectView):
    url = reverse_lazy('blog:postbriefs')
    permanent = False

    def get(self, request, *args, **kwargs):
        name = request.user.username
        logout(request)
        self.messages.success("%s You've been logged out. Come back soon!" % name)
        return super(LogoutView, self).get(request, *args, **kwargs)

