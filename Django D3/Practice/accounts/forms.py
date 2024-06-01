from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import mail_managers
from django.core.mail import EmailMultiAlternatives

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name='common users')
        user.groups.add(common_users)

        subject='Our team is glad to see you in our online store. Thank you for your trust!'
        text=f'{user.username},you have successfully registered!'
        html=(
            f'<b>{user.username}</b>, you have successfully registered in '
            f'<a href="http://127.0.0.1:8000/products">service</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        mail_managers(
            subject='New User!',
            message=f'Пользователь {user.username} registered in our site.'
        )
        return user
