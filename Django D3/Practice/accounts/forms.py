from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name='common users')
        user.groups.add(common_users)
        send_mail(
            subject='Our team is glad to see you in our online store. Thank you for your trust!',
            message=f'{user.username}, you have successfully registered!',
            from_email=None,
            recipient_list=[user.email],
        )
        return user
