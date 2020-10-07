from registration.backends.default.views import RegistrationView
from .forms import ProfileForm
from .models import Profile


class MyRegistrationView(RegistrationView):

    form_class = ProfileForm

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)
        fullname = form_class.cleaned_data['fullname']
        address = form_class.cleaned_data['address']
        phone_number = form_class.cleaned_data['phone_number']
        new_profile = Profile.objects.create(user=new_user,fullname=fullname,address=address,phone_number=phone_number)
        new_profile.save()
        return new_user